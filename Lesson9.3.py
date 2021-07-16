# %%
# Q1
import re
print("\n[Q1]")

listA = ["Sample.csv", "Sample.exe", "Sample1py",
         "Sample2.py", "Sample.txt", "index.html"]
listB = []
print("ファイルのリストは以下です。")
print(listA)

extension = input("拡張子を入力してください。")
print("該当するファイルのリストは以下です。")
extension = f"\.{extension}$"
pt = re.compile(extension)
for val in listA:
    if pt.search(val) is not None:
        print(val)
