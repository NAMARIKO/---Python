# %%
# Sample_3
import csv
print("\n[Sample_3]")

# CSV書き込み
f = open("Lesson10.csv", "w", encoding="utf-8", newline="")
w = csv.writer(f)
w.writerow(["東京", "鉛筆", 25],)
w.writerows([
    ["大阪", "ノート", 30],
    ["名古屋", "定規", 100],
    ["福岡", "ノート", 73]])
f.close()

# CSV読み込み
f = open("Lesson10.csv", "r", encoding="utf-8")
rd = csv.reader(f)

for row in rd:
    print(f"{row[0]:<10}\t{row[1]:<10}\t{row[2]:<10}")

f.close()
