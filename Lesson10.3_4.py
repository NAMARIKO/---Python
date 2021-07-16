# %%
# Sample_3
import json
print("\n[Sample_3]")

# json書き込み
f = open("Lesson10.json", "w", encoding="utf-8")
w = json.dump(
    r"{'関東': {'東京': 100, '横浜': 200}, '関西': {'大阪': 300, '奈良': 400}}", f)
f.close()

# json読み込み
f = open("Lesson10.json", "r", encoding="utf-8")
data = json.load(f)
print(data)

f.close()
