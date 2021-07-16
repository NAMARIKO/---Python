# %%
# Sample_3
print("\n[Sample_3]")

num = int(input("売上を入力してください。"))
num2 = int(input("人数を入力してください。"))

if num >= 100 and num2 >= 30:
    print("最高")
elif num >= 100:
    print("良")
elif num >= 50:
    print("普通")
else:
    print("悪")

print("処理終了")
