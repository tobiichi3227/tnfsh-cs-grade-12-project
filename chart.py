import matplotlib.pyplot as plt

data = [
    {"date": 1130414, "values": [6, 5, 4]},
    {"date": 1130413, "values": [16, 8, 12]},
    {"date": 1130412, "values": [14, 8, 9]},
    {"date": 1130411, "values": [14, 6, 6]},
    {"date": 1130410, "values": [10, 7, 6]},
    {"date": 1130409, "values": [7, 5, 4]},
    {"date": 1130408, "values": [0, 4, 0]},
    {"date": 1130407, "values": [0, 6, 0]},
    {"date": 1130406, "values": [1, 7, 0]},
    {"date": 1130405, "values": [0, 8, 0]},
    {"date": 1130404, "values": [3, 7, 0]},
    {"date": 1130403, "values": [30, 9, 20]},
    {"date": 1130402, "values": [6, 7, 2]},
    {"date": 1130401, "values": [0, 7, 0]},
    {"date": 1130331, "values": [4, 6, 0]},
    {"date": 1130330, "values": [8, 7, 1]},
    {"date": 1130329, "values": [4, 5, 0]},
    {"date": 1130328, "values": [20, 8, 14]},
    {"date": 1130327, "values": [9, 6, 4]},
    {"date": 1130326, "values": [13, 7, 3]},
    {"date": 1130325, "values": [5, 7, 1]},
    {"date": 1130324, "values": [6, 8, 1]},
    {"date": 1130323, "values": [13, 6, 4]},
    {"date": 1130322, "values": [36, 6, 13]},
    {"date": 1130321, "values": [32, 5, 20]},
    {"date": 1130320, "values": [15, 10, 6]},
    {"date": 1130319, "values": [9, 10, 2]},
    {"date": 1130318, "values": [9, 5, 3]},
    {"date": 1130317, "values": [4, 7, 1]},
    {"date": 1130316, "values": [10, 8, 6]},
    {"date": 1130315, "values": [11, 8, 4]},
    {"date": 1130314, "values": [26, 10, 18]},
    {"date": 1130313, "values": [10, 9, 4]},
    {"date": 1130312, "values": [2, 5, 0]},
    {"date": 1130311, "values": [8, 6, 0]},
    {"date": 1130310, "values": [7, 5, 2]},
    {"date": 1130309, "values": [9, 5, 4]},
    {"date": 1130308, "values": [9, 5, 1]},
    {"date": 1130307, "values": [8, 5, 1]},
    {"date": 1130306, "values": [14, 8, 0]},
    {"date": 1130305, "values": [0, 0, 0]},
    {"date": 1130304, "values": [16, 7, 10]},
    {"date": 1130303, "values": [21, 6, 10]},
    {"date": 1130302, "values": [9, 8, 4]},
    {"date": 1130301, "values": [10, 6, 3]},
    {"date": 1130229, "values": [19, 7, 12]},
    {"date": 1130228, "values": [15, 11, 3]},
    {"date": 1130227, "values": [10, 6, 0]},
    {"date": 1130226, "values": [11, 5, 2]},
    {"date": 1130225, "values": [4, 4, 0]},
    {"date": 1130224, "values": [9, 9, 0]},
    {"date": 1130223, "values": [11, 6, 2]},
    {"date": 1130222, "values": [11, 6, 5]},
    {"date": 1130221, "values": [10, 6, 6]},
    {"date": 1130220, "values": [24, 8, 11]},
    {"date": 1130219, "values": [7, 7, 1]},
    {"date": 1130217, "values": [7, 5, 0]},
    {"date": 1130216, "values": [8, 7, 1]},
    {"date": 1130215, "values": [21, 6, 14]},
    {"date": 1130214, "values": [4, 4, 1]},
    {"date": 1130213, "values": [2, 4, 1]},
    {"date": 1130212, "values": [2, 4, 0]},
    {"date": 1130211, "values": [6, 4, 1]},
    {"date": 1130210, "values": [5, 4, 2]},
    {"date": 1130209, "values": [7, 5, 3]},
    {"date": 1130208, "values": [0, 4, 0]},
    {"date": 1130207, "values": [9, 5, 0]},
    {"date": 1130206, "values": [25, 6, 13]},
    {"date": 1130205, "values": [2, 5, 0]},
    {"date": 1130204, "values": [7, 4, 1]},
    {"date": 1130203, "values": [10, 5, 0]},
    {"date": 1130202, "values": [8, 5, 3]},
    {"date": 1130201, "values": [33, 6, 14]},
    {"date": 1130131, "values": [7, 4, 0]},
    {"date": 1130130, "values": [9, 4, 0]},
    {"date": 1130129, "values": [7, 6, 0]},
    {"date": 1130128, "values": [9, 6, 2]},
    {"date": 1130127, "values": [33, 6, 13]},
    {"date": 1130126, "values": [10, 4, 2]},
    {"date": 1130125, "values": [18, 6, 4]},
    {"date": 1130124, "values": [7, 5, 0]},
    {"date": 1130123, "values": [7, 3, 1]},
    {"date": 1130122, "values": [4, 4, 0]},
    {"date": 1130121, "values": [3, 4, 0]},
    {"date": 1130120, "values": [10, 4, 2]},
    {"date": 1130119, "values": [12, 4, 1]},
    {"date": 1130118, "values": [24, 5, 11]},
    {"date": 1130117, "values": [9, 3, 2]},
    {"date": 1130116, "values": [15, 3, 2]},
    {"date": 1130115, "values": [6, 4, 1]},
    {"date": 1130114, "values": [0, 4, 0]},
    {"date": 1130113, "values": [8, 6, 1]},
    {"date": 1130112, "values": [10, 6, 2]},
    {"date": 1130111, "values": [15, 4, 2]},
    {"date": 1130110, "values": [8, 5, 1]},
    {"date": 1130109, "values": [10, 4, 2]},
    {"date": 1130108, "values": [9, 4, 1]},
    {"date": 1130107, "values": [8, 6, 0]},
    {"date": 1130106, "values": [13, 0, 1]},
    {"date": 1130105, "values": [8, 4, 2]},
    {"date": 1130104, "values": [6, 6, 1]},
    {"date": 1130103, "values": [9, 4, 2]},
    {"date": 1130102, "values": [4, 3, 1]},
    {"date": 1130101, "values": [4, 4, 1]},
    {"date": 1121231, "values": [3, 4, 1]},
    {"date": 1121230, "values": [7, 4, 0]},
    {"date": 1121229, "values": [22, 4, 12]},
    {"date": 1121228, "values": [9, 4, 0]},
    {"date": 1121227, "values": [10, 5, 3]},
    {"date": 1121226, "values": [8, 5, 3]},
    {"date": 1121225, "values": [2, 4, 0]},
    {"date": 1121224, "values": [22, 7, 11]},
    {"date": 1121223, "values": [7, 2, 3]},
    {"date": 1121222, "values": [9, 2, 3]},
    {"date": 1121221, "values": [8, 3, 0]},
    {"date": 1121220, "values": [8, 3, 1]},
    {"date": 1121219, "values": [4, 3, 0]},
    {"date": 1121218, "values": [6, 2, 1]},
    {"date": 1121217, "values": [0, 3, 0]},
    {"date": 1121216, "values": [27, 9, 10]},
    {"date": 1121215, "values": [12, 9, 2]},
    {"date": 1121214, "values": [9, 9, 3]},
    {"date": 1121213, "values": [7, 7, 1]},
    {"date": 1121212, "values": [20, 9, 1]},
    {"date": 1121211, "values": [10, 11, 1]},
    {"date": 1121210, "values": [12, 7, 4]},
    {"date": 1121209, "values": [10, 7, 2]},
    {"date": 1121208, "values": [26, 10, 15]},
    {"date": 1121207, "values": [10, 6, 2]},
    {"date": 1121206, "values": [7, 5, 0]},
    {"date": 1121205, "values": [0, 7, 0]},
    {"date": 1121204, "values": [5, 5, 0]},
    {"date": 1121203, "values": [4, 6, 0]},
    {"date": 1121202, "values": [5, 4, 0]},
    {"date": 1121201, "values": [24, 6, 12]},
    {"date": 1121130, "values": [12, 5, 0]},
]


dates = []
for o in data:
    dates.append(str(o["date"]))
values = []
for o in data:
    v1, v2, v3 = o["values"]
    values.append((v1, v2, v3))

# 將數據分離成3組值
plains = [v[0] for v in values]
ships = [v[1] for v in values]
enter_azid_plains = [v[2] for v in values]

plt.figure(figsize=(20, 10))
plt.plot(dates, plains, label="plane", marker="o")
plt.plot(dates, ships, label="ship", marker="o")
plt.plot(dates, enter_azid_plains, label="adiz", marker="o")

plt.xlabel("Date")
plt.ylabel("Values")
plt.title("Values Over Time")

# add icon
plt.legend()

# show result
plt.grid(True)
plt.tight_layout()
plt.show()
