# %%
# Sample_1
print("\n[Sample_1]")

# ファイル書き込み
f = open("Lesson10.txt", "w")
f.write("Hello\n")
f.write("Python\n")
f.close()

# ファイル書き込み
with open("Lesson10.txt", "w") as f:
    f.write("Hello.\n")
    f.write("Python.\n")

# ファイル書き込み(追記)
f = open("Lesson10.txt", "a")
f.write("Hello!\n")
f.write("Python!\n")
f.close()

# ファイル読み込み
f = open("Lesson10.txt", "r")
lines = f.readlines()
for line in lines:
    print(line, end="")
    f.close()
