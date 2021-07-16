"""
defunction
"""
# %%
# Sample_8
print("\n[Sample_8]")


def a():
    print("a")


def b():
    print("b")


def c():
    print("c")


num = int(input("処理を選択[0-2]"))
defList = [a, b, c]
defList[num]()

"""
lambda(名前のない関数)
"""
# %%
# Sample_8
print("\n[Sample_8]")

data = [1, 2, 3, 4, 5]
for d in map(lambda x: x*2, data):
    print(d)

"""
デコレータ
"""
# %%
# Sample_10
print("\n[Sample_10]")


def deco(func):
    def wapper(x):
        wx = "---" + x + "----"
        return func(wx)
    return wapper


@deco
def printmsg(str):
    print(str)


printmsg("aaaa")
"""
ジェネレータ
"""
# %%


def test(x, y=50):
    while True:
        yield x, y
        x = x+1
        y *= 2


n = test(0)
print(next(n))
print(next(n))
