import re
import copy

import cv2
import numpy as np
import requests
import pytesseract
from bs4 import BeautifulSoup

AIRFORCE_URL = "https://air.mnd.gov.tw"
AIRFORCE_NEWS_LIST_URL = "https://air.mnd.gov.tw/TW/News/News_List.aspx?CID=213"
NEWS_INDEX_QUERY = "ctl00$ContentPlaceHolder1$TableList$lbutC00000000{}"

def get_img_from_url(url):
    resp = requests.get(url, stream=True).raw
    img = np.asarray(bytearray(resp.read()), dtype="uint8")

    return cv2.imdecode(img, cv2.IMREAD_COLOR)

def get_count_from_img(img):
    text = pytesseract.image_to_string(img)
    text = text.replace('\n', ' ')
    # print(text)

    try:
        f = r"([\d]*) PLA aircraft"
        plain = re.search(f, text)
        plain_cnt = 0
        if plain is not None and (cnt := plain.group(1)) != '':
            plain_cnt = int(cnt)
            
            
        f = r"([\d]*) PLAN vessels"
        ship = re.search(f, text)
        ship_cnt = 0
        if ship is not None and (cnt := ship.group(1)) != '':
            ship_cnt = int(cnt)
            
        f = r"([\d]*) of the"
        adiz = re.search(f, text)
        adiz_cnt = 0
        if adiz is None:
            if re.search(r"One of the", text):
                adiz_cnt = 1
            elif re.search(r"Two of the", text):
                adiz_cnt = 2
        else:
            cnt = adiz.group(1)
            if cnt != '':
                adiz_cnt = int(cnt)

    except Exception as e:
        import traceback
        print(text, e)
        traceback.print_exc()

    return (plain_cnt, ship_cnt, adiz_cnt)

def get_air_activity(url) -> tuple[str, str]:
    html = requests.get(url).text

    soup = BeautifulSoup(html, 'html.parser')
    img = soup.select_one('span#ContentPlaceHolder1_lab_Descr > p > img')

    if img is None:
        img = soup.select_one('span#ContentPlaceHolder1_lab_Descr > div > div > p > img')

    if img is None:
        img = soup.select_one('span#ContentPlaceHolder1_lab_Descr > div > p > img')

    if img is None:
        img = soup.select_one('span#ContentPlaceHolder1_lab_Descr > div > div > img')
        
    if img is None:
        plain = re.search(r"([\d]*)架次", html)

        if plain is not None:
            print(plain.group(1))

        ship = re.search(r"([\d]*)艘次", html)
        if ship is not None:
            print(ship.group(1))
            
        return None, None
    
    date = re.search(r"([\d]*)", img['alt']).group()
    img_url = img['src']

    return date, AIRFORCE_URL + img_url[8:]

def get_aspx_hidden_value(url):
    html = requests.get(url).text
    
    viewstate = re.findall(r'<input type="hidden" name="__VIEWSTATE" id="__VIEWSTATE" value="(.*?)" />', html, re.I)
    eventvalidation = re.findall(r'<input type="hidden" name="__EVENTVALIDATION" id="__EVENTVALIDATION" value="(.*?)" />', html, re.I)
    viewstategenerator = re.findall(r'input type="hidden" name="__VIEWSTATEGENERATOR" id="__VIEWSTATEGENERATOR" value="(.*?)" />', html, re.I)

    return viewstate[0], eventvalidation[0], viewstategenerator[0]

def main():
    for i in range(7, 20):
        viewstate, eventvalidation, viewstategenerator = get_aspx_hidden_value(AIRFORCE_NEWS_LIST_URL)

        data = {
            "__EVENTTARGET": NEWS_INDEX_QUERY.format(str(i).zfill(2)),
            "__EVENTVALIDATION": eventvalidation,
            "__VIEWSTATE": viewstate,
            "__VIEWSTATEGENERATOR": viewstategenerator,
            "__EVENTARGUMENT": "",
            "ctl00$txb_s": "",
        }

        html = requests.post(AIRFORCE_NEWS_LIST_URL, data=data, headers={
            "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.13) Gecko/20080311 Firefox/2.0.0.13"
        }).text

        soup = BeautifulSoup(html, 'html.parser')
        for link in soup.select("ul#ContentPlaceHolder1_TableList_ul_List > li > a"):
            date, img_url = get_air_activity(AIRFORCE_URL + link['href'])
            if date is None and img_url is None:
                continue

            img = get_img_from_url(img_url)
            height, width, _ = img.shape

            print(date, get_count_from_img(img))

if __name__ == "__main__":
    main()
