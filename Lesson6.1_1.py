# %%
# Sample_1
print("\n[Sample_1]")

t = 1, 2, 3
print(type(t), t)
t = (4, 5, 6)
print(type(t), t)
t = ()
print(type(t), t)
list = [1, 2, 3]
t = tuple(list)
print(type(t), t)

print(t[0])
# t[0] = 3 # Error
