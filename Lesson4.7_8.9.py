# %%
# Sample_8
print("\n[Sample_8]")

num = int(input("何月で停止させますか？[1-12]"))
for month in range(1, 13):
    print(month, "月")
    if month == num:
        break
# %%
# Sample_9
print("\n[Sample_9]")

num = int(input("何月をスキップしますか？[1-12]"))
for month in range(1, 13):
    if month == num:
        continue
    print(month, "月")
