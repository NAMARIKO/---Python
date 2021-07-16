"""
set
"""
# %%
# Sample_6
print("\n[Sample_6]")

data = {"滋賀県", "京都府", "大阪府", }
data2 = {"大阪府", "兵庫県", "奈良県", "和歌山県"}
print("data\tnew:\t", data)
print("data2\tnew:\t", data2)

# set操作
data.add("兵庫県")
print("data\tadd:\t", data)

data.remove("兵庫県")
print("data\tremove:\t", data)

# Sample_7
print("\n[Sample_7]")

# setで集合演算
print("data & data2\t共通:\t", data & data2)
print("data - data2\tdata のみ:\t", data - data2)
print("data2 - data\tdata2 のみ:\t", data2 - data)
print("data | data2\t全て(+):\t", data | data2)
data3 = {}
print(type(data3))
