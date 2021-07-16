# %%
# Sample_15
print("\n[Sample_15]")

data = [80, 60, 50, 57]
print("現在のList\t:", data)

print("最大値 \t:", max(data))
print("最小値 \t:", min(data))
print("合計 \t:", sum(data))
print("ソート(昇順) \t:", sorted(data))
print("ソート(降順) \t:", sorted(data, reverse=True))

data.sort()
print("ソート(昇順) \t:", data)
data.sort(reverse=True)
print("ソート(降順) \t:", data)
