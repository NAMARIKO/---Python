# %%
# Sample_4
print("\n[Sample_4]")

data = {
    "25": "滋賀県",
    "26": "京都府",
    "27": "大阪",
}
data2 = {
    "27": "大阪府",
    "28": "兵庫県",
    "29": "奈良県",
    "30": "和歌山県"
}

# key
for key in data.keys():
    print(key)

# value
print()
for value in data.values():
    print(value)

# item(key,value)
print()
for item in data.items():
    print(item)

print()
for key, value in data.items():
    print(key, value, sep="\t")

# Sample_4
print("\n[Sample_4]")

# 更新/追加/上書き
print("data:\t", data)
print("data2:\t", data2)
print("更新します。")
data.update(data2)
print(data)
