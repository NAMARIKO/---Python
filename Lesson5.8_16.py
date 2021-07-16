# %%
# Sample_16
print("\n[Sample_16]")

data = [
    [25, "滋賀県"],
    [26, "京都府"],
    [27, "大阪府"],
    [28, "兵庫県"],
    [29, "奈良県"],
    [30, "和歌山県"],
]
print("現在のList\t:", data)
for dat in data:
    print("都道府県データ:\t", dat)
    for val in dat:
        print(val, end="\t")
    print()

print(data[0][0], data[0][1])
