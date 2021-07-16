# %%
# Sample_6
print("\n[Sample_6]")

for i in range(5):
    for ii in range(3):
        print("i: ", i, ", ii :", ii)


# %%
# Sample_7
print("\n[Sample_7]")

v = False
for i in range(5):
    for ii in range(5):
        if v == False:
            print("*", end="")
            v = True
        else:
            print("-", end="")
            v = False
    print()
