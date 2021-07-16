import numpy as np
import random
import matplotlib.pyplot as plt
# %%
# Q1
print("\n[Q1]")

data = [8, 17, 0, 11, 6, 21, 16, 6, 17, 11, 7, 9, 6, 13, 12, 16, 3, 14, 13, 12]
plt.title("histogram")
plt.xlabel("value")
plt.ylabel("frequency")
plt.hist(data, bins=8, color="magenta")
plt.show()

# %%
# Q2
print("\n[Q2]")

x = []
y = []

for i in range(100):
    x.append(random.uniform(0, 50))
    y.append(random.uniform(0, 50))
v = [-100, 100, -100, 100]
plt.axis(v)

plt.scatter(x, y, marker="x")
plt.show()

# %%
# Q3
print("\n[Q3]")

data = []
for i in range(1000):
    data.append(random.normalvariate(0, 10))
plt.title("histogram")
plt.hist(data, bins=50)
plt.show()

# %%
# Q4
print("\n[Q4]")

x = np.arange(-8, 8, 0.01)
y = x**2
y2 = 3*x+5

plt.title("y = f(x)")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)

plt.plot(x, y, label="x**2")
plt.plot(x, y2, label="3x+5")
plt.legend()

plt.show()
