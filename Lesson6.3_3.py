# %%
# Sample_3
print("\n[Sample_3]")

data = {
    "25": "滋賀県",
    "26": "京都府",
}
print(data)
print("data[27]に\"未記入\"を追加")
data["27"] = "未記入"
print(data)

print("data[27]を\"福島\"に変更")
data["27"] = "大阪府"
print(data)

print("data[27]を削除")
del data["27"]
print(data)
