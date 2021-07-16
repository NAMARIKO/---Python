"""
listの操作
"""

# %%
# Sample_4
# list変更
print("\n[Sample_4]")

list = [80, 60, 22, 50, 75]
print(list)

i = int(input("何番のデータを変更しますか？"))
num = int(input("変更後のすうちを入力してください。"))

list[i] = num
print(i, "番のデータを", num, "に変更しました。")
print(list)

# %%
# Sample_5
# list追加,挿入
print("\n[Sample_5]")

print("現在のデータ:", list)

print("末に[100]追加")
list.append(100)
print("現在のデータ:", list)

print("list[3]に[300]追加")
list.insert(3, 300)
print("現在のデータ:", list)

# %%
# Sample_6
# list削除
print("\n[Sample_6]")

print("現在のデータ:", list)

print("del で list[0] 削除")
del list[0]
print("現在のデータ:", list)

print("remove で 300 のデータを削除")
list.remove(300)
print("現在のデータ:", list)
