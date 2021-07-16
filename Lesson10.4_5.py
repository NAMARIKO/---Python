# %%
# Sample_5
print("\n[Sample_5]")

try:
    f = open("Lesson11.txt", "r")
except BaseException as e:
    print(e)
    print("ファイルをオープン出来ませんでした")
else:
    for data in f.readlines():
        print(data, end="")
finally:
    print("処理終了しました")
