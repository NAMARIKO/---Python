# %%
# Sample_7
# list代入(紐づけ)
print("\n[Sample_7]")

list_1 = [80, 60, 22, 50, 75]
list_2 = list_1
print("list_1:", list_1)
print("list_2:", list_2)

print("list[0]=100 に変更")
list_1[0] = 100
print("list_1:", list_1)
print("list_2:", list_2)

# %%
# Sample_8
# list複製(list,copy)
print("\n[Sample_8]")

print("listで複製")
list_3 = list(list_1)
print("list_1:", list_1)
print("list_3:", list_3)

print("list_3[0]=500 に変更")
list_3[0] = 500
print("list_1:", list_1)
print("list_3:", list_3)

# %%
print("copyで複製")
list_4 = list_1.copy()
print("list_1:", list_1)
print("list_4:", list_4)


print("list_4[0]=400 に変更")
list_4[0] = 400
print("list_1:", list_1)
print("list_4:", list_4)
