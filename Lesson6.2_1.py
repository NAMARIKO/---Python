"""
dictionary
... dict()
"""
# %%
# Sample_1
print("\n[Sample_1]")

# ディクショナリを作成
d = {1: 1, 2: 2, 3: 3}
print(type(d), d)
d = {"tuple": (1, 2), "list": [1, 2], "dict": {1, 2}}
print(type(d), d)
data = {
    "25": "滋賀県",
    "26": "京都府",
    "27": "大阪府",
    "28": "兵庫県",
    "29": "奈良県",
    "30": "和歌山県"
}
print("現在のdict\t:", data)

# 値を取得
str = input("何番ですか？")
print(data[str])

str = input("何番ですか？")
if str in data:
    print(data[str])
else:
    print(str, "は見つかりませんでした。")

# %%
data = [1, 1]
print(data)
print("!0 が1つ以上\t:", any(data))  # True
print("!0 が全部\t:", all(data))  # True

data = [0, 1]
print(data)
print("!0 が1つ以上\t:", any(data))  # True
print("!0 が全部\t:", all(data))  # False

data = [0, 0]
print(data)
print("!0 が1つ以上\t:", any(data))  # False
print("!0 が全部\t:", all(data))  # False
