import statistics

# %%
# Sample_1
print("\n[Sample_1]")

data = [8, 17, 0, 11, 6, 21, 16, 6, 17, 11, 7, 9, 6, 13, 12, 16, 3, 14, 13, 12]

print(f"平均値: \t{statistics.mean(data)}")
print(f"中央値: \t{statistics.median(data)}")
print(f"最頻値: \t{statistics.mode(data)}")
print(f"分散:   \t{statistics.pvariance(data)}")
print(f"標準偏差: \t{statistics.pstdev(data)}")
