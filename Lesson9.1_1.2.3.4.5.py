# %%
# Sample_1
print("\n[Sample_1]")

str = "namari"
print("文字列：", str, sep="\t")
print("0番目の文字：", str[0], sep="\t")
print("逆順の文字列：", str[::-1], sep="\t")
print("文字列の長さ：", len(str), sep="\t")

# %%
# Sample_2
print("\n[Sample_2]")

"My name is {0}. {1}".format("namari", "Hello :)")
# %%
"key:{Key}, val:{Value}".format(Key="13", Value="namaei")
# %%
"{:,}".format(10000000)

# %%
# Sample_3
print("\n[Sample_3]")

name = "namari"
age = 25
print(f"name:\t {name}\t age:\t{age}")
print("{0:<}個{1:>8,}円".format(10, 10000))

# %%
# Sample_4
print("\n[Sample_4]")

str = "namari"
res = str.find("0")
if res != -1:
    print(f"{str}\tの {res} 番目に見つかりました")
else:
    print("見つかりませんでした")
# %%
# Sample_5
print("\n[Sample_5]")

str = "my name is namari"
old = "namari"
new = "Namari"
if old in str:
    str = str.replace(old, new)
    print(str)
