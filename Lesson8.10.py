# %%
# Q1
print("\n[Q1]")


class Car:
    num = 0
    gas = 0.0

    def __init__(self, num, gas):
        self.num = num
        self.gas = gas
        return

    def getData(self):
        print("ナンバー:", self.num, "ガソリン量:", self.gas, sep="\t")


Car(1234, 25.5).getData()
Car(2345, 30.5).getData()
