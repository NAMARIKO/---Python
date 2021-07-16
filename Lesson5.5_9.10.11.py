"""
listの結合
"""
# %%
# Sample_9
from typing import List


print("\n[Sample_9]")

list_1 = [1, 2, 3, 4, 5, 6]
list_2 = [7, 8, 9, 10, 11, 12]

print("上半期:", list_1)
print("下半期:", list_2)

# listの結合(+)
print("年間:", list_1+list_2)
# listの結合(extend)
list_1.extend(list_2)
print("年間:", list_1)
# listの結合(+=)
list_1 += list_2
print("年間:", list_1)


"""
listのスライス
"""
# %%
# Sample_10
print("\n[Sample_10]")

months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
print("年間\t:", months)
print("上半期\t:", months[0:7])
print("下半期\t:", months[7::])
print("2ヶ月毎\t:", months[1::2])
print("年間\t:", months[::1])
print("年間(逆順)\t:", months[::-1])
print("ボーナス(年3回)\t:", months[3::4])


months[6::] = [0, 0, 0, 0, 0, 0]
print("[6]以降、0を代入\t:", months)

del months[6::]
print("[6]以降、削除\t:", months)

"""
listの逆順
"""
# %%
# Sample_11
print("\n[Sample_11]")

list = [1, 2, 3, 4, 5, 6]

# list[::-1]
print("list[::-1]\t:", list[::-1])
print("現在のList\t:", list)

# reversed(list) : for
print("reversed(list)\t:")
print("\tprint(for) \t:", end=" ")
for item in reversed(list):
    print(item, end=", ")
print()

# reversed(list) : next
it = reversed(list)
print("\tprint(next) \t:", end=" ")
print(next(it), end=", ")
print(next(it), end=", ")
print(next(it), end=", ")
print(next(it), end=", ")
print(next(it), end=", ")
print(next(it), end=", \n")

print("現在のList\t:", list)

# list.reverse()
print("list.reverse\t:")
list.reverse()
print("現在のList\t:", list)
