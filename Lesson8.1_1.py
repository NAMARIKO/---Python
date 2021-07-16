# %%
# Sample_1
print("\n[Sample_1]")


class Sample1:
    count = 0

    def __init__(self, name, age):

        Sample1.count += 1
        self._name = name
        self._age = age

    def getName(self):
        return self._name

    def getAge(self):
        return self._age

    @classmethod
    def getCount(cls):
        return cls.count


sa = Sample1("namari", 26)
sa2 = Sample1("tanaka", 80)
sa._name = list()

print(sa.getName(), sa.getAge(), sep="\t")
print(sa2.getName(), sa2.getAge(), sep="\t")
print("合計人数は", Sample1.getCount())
