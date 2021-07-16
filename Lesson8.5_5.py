# %%
# Sample_5
print("\n[Sample_5]")


class Sample1:
    count = 0

    def __init__(self, name, age):

        Sample1.count += 1
        self.name = name
        self.age = age

    def getName(self):
        return self.name

    def getAge(self):
        return self.age


class Sample5(Sample1):
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


sp5 = Sample5("namari", 27, "email@gmail.com", "000-0000-0000")
print(sp5.getName(), sp5.getAge(), sp5.getAddress(), sp5.getTel(), sep="\t")
