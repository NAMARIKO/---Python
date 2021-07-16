prefectureName = [
    "滋賀県",
    "京都府",
    "大阪府",
    "兵庫県",
    "奈良県",
    "和歌山県",
]
prefectureNum = [
    25,
    26,
    27,
    28,
    29,
    30,
]

"""
リスト組み合わせ
"""
# %%
# Sample_12
print("\n[Sample_12]")

print("都道府県\t:", prefectureName)
print("都道府県番号\t:", prefectureNum)

# enumerate
print("prefectureName -> (key, name)")
for data in enumerate(prefectureName):
    print(data)

# zip
print("(prefectureNum, prefectureName) -> (num, name)")
for data in zip(prefectureNum, prefectureName):
    print(data)

"""
リスト分解
"""
# %%
# Sample_13
print("\n[Sample_13]")

for num, name in zip(prefectureNum, prefectureName):
    print("番号:", num, "\t都道府県名:", name)


"""
・アンパック(代入)
・リスト内包表記
"""
# %%

# %%
# アンパック(代入)
data = [1, 2, 3]
data1, data2, data3 = data  # 配列数と一致しないとエラー

print(data1)
print(data2)
print(data3)

# %%
# リスト内包表記
# Sample_13
print("\n[Sample_13]")

print("現在のList\t:", data)
data = [i*2 for i in data if i != 3]
# 上記の内容
#  for k, v in enumerate(data):
#     if v != 3:
#         data[k] = v*2
print("現在のList\t:", data)
