# %%
# Q1
print("\n[Q1]")


def rpast(num):
    print("*"*num)


num = int(input("個数入力してください。"))
rpast(num)

# %%
# Q2
print("\n[Q2]")

str = input("文字列を入力してください。")
num = int(input("個数入力してください。"))


def rpstr(num, str="*"):
    print(str*num)


print("あり")
rpstr(num, str)
print("なし")
rpstr(num)

# %%
# Q3
print("\n[Q3]")

start = int(input("開始値を入力してください。"))
stop = int(input("終了値を入力してください。"))


def addNum(x):
    while True:
        yield x
        x += 1


num = addNum(start)
for i in range(start, stop):
    print(next(num))
