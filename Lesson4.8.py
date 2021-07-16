# %%
# Q1
print("\n[Q1]")

for item in range(1, 11):
    if item % 2 == 0:
        print(item)


# %%
# Q2
print("\n[Q2]")

for item in range(1, 11, 2):
    print(item+1)

# %%
# Q3
print("\n[Q3]")

for i in range(1, 10):
    for ii in range(1, 10):
        print(i*ii, end="\t")
    print()

# %%
# Q4
print("\n[Q4]")

for i in range(1, 6):
    print("*"*i)
