# %%
# Q1
print("\n[Q1]")

data = [74, 85, 69, 77, 81]
print("テストの点数:\t", data)
print("最高:\t", max(data))
print("最低:\t", min(data))
print("平均:\t", sum(data)/len(data))

# %%
# Q2
print("\n[Q2]")

print("テストの点数:\t", data)
print("ソート(昇順):\t", sorted(data))
print("ソート(降順):\t", sorted(data, reverse=True))

# %%
# Q3
print("\n[Q3]")

print("テストの点数:\t", data)
data2 = [val for val in data if val >= 80]
print("80以上の点数:\t", data2)
print("80以上の人数:\t", len(data2))

# %%
# Q3
print("\n[Q3]")

nameList = ["滋賀", "京都", "大阪", "兵庫", "奈良", "和歌山県"]
maxList = [32, 28, 27, 26, 27]
minList = [25, 21, 20, 19, 22]
print("name:\t", nameList)
print("max:\t", maxList)
print("min:\t", minList)

data3 = zip(nameList, maxList, minList)
print("data3:\t", data3)
for val1, val2, val3 in data3:
    print(val1, "の最高気温は", val2, "\t最低気温は", val3)
