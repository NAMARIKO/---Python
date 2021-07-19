# %%
# Sample_1
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn import linear_model
from sklearn import datasets
print("\n[Sample_1]")


np.random.seed(0)

x, y = datasets.make_regression(n_samples=100, n_features=1, noise=30)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)

e = linear_model.LinearRegression()
e.fit(x_train, y_train)
print(e.coef_)
print(e.intercept_)
y_pred = e.predict(x_test)
print(e.score(x_test, y_test))
print(e.score(x_train, y_train))
plt.scatter(x_train, y_train, label="train")
plt.scatter(x_test, y_test, label="test")

plt.plot(x_test, y_pred, color="magenta")
plt.legend()

plt.show()
