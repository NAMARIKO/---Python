# %%
# Sample_3
print("\n[Sample_3]")


def sell(name, a=100, set=500):
    print(name, "支店の販売が行われました", set)


sell("大阪", set=100)
sell("東京")


def test(*test):
    print(test)


f_test = test
f_test(1, 2, 3, 4, 5, 6)
