# %%
# import
print("\n[import]")


class module_1:
    count = 0

    def __init__(self, name, age):

        module_1.count += 1
        self.name = name
        self.age = age

    def getName(self):
        return self.name

    def getAge(self):
        return self.age


class module_2(module_1):
    def __init__(self, name, age, ad, tel):
        super().__init__(name, age)
        self.ad = ad
        self.tel = tel

    def getName(self):
        return "顧客 : "+self.name

    def getAge(self):
        return "年齢 : "+str(self.age)

    def getAddress(self):
        return "e-Mail : "+self.ad

    def getTel(self):
        return "TEL : "+self.tel

    def getData(self):
        print(self.getName(), self.getAge(),
              self.getAddress(), self.getTel(), sep="\t")
