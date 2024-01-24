import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('name.txt', header=None, names=['age', 'score'])
# print(data.describe())
data.plot(kind='scatter', x='age', y='score', figsize=(8, 4))
cols = data.shape[1]
# print(cols)

x = data.iloc[:, 0:2]
print(x)
y = np.matrix(x.values)  # 生成一个矩阵
print(y)
a = np.array([0, 0])
b = np.matrix(a)
data.insert(0, 'cao', 1)
print(y.T)
