import numpy as np  # 矩阵处理库
import pandas as pd  # 数据读取处理
import matplotlib.pyplot as plt  # 画图

path = 'ex1data1.txt'
data = pd.read_csv(path, header=None, names=[
                   'Population', 'Profit'])  # 以csv模式打开txt文件
data.head()  # 默认前5行数据
data.describe()  # 数据表描述性统计，如最大最小值，均值等
data.plot(kind='scatter', x='Population', y='Profit',
          figsize=(12, 8))  # kind表示你要创建的图表类型,figsize表示显示大小s
plt.show()  # 展示图标


def computeCost(X, y, theta):
    # 此函数将第一个输入数组中的元素作为底数，计算它与第二个输入数组中相应元素的幂
    # 矩阵.T是矩阵的转置
    inner = np.power(((X * theta.T) - y), 2)
    # sum(a, axis=None, dtype=None, out=None, keepdims=np._NoValue)
    # 对应1/2m,sum对向量或者矩阵求和，可得到总和，或者压缩行和压缩列
    return np.sum(inner) / (2 * len(X))


# Dataframe.insert(loc, column, value, allow_duplicates=False): 在Dataframe的指定列中插入数据。
# 0表示在第一列插入数据，ones表示列名，1表示插入的值全为一，也可以是list和array
data.insert(0, 'Ones', 1)
# set X (training data) and y (target variable)
# data.shape返回的是元组
# data.shape[0]是行数
# data.shape[1]是列数

cols = data.shape[1]
#data.iloc[ A:B ,C:D ]
# 从A行/列开始取（包括自己本身），取到B列（不包括B那一列）
# 用法：逗号前面表示的是取哪些行，逗号后面表示取哪些列

X = data.iloc[:, 0:cols-1]  # X是所有行，去掉最后一列,前面的冒号就是取行数，后面的冒号是取列数
y = data.iloc[:, cols-1:cols]  # X是所有行，最后一列
X = np.matrix(X.values)
y = np.matrix(y.values)
theta = np.matrix(np.array([0, 0]))  # 这是一个行向量

computeCost(X, y, theta)


def gradientDescent(X, y, theta, alpha, iters):
    temp = np.matrix(np.zeros(theta.shape))
    parameters = int(theta.ravel().shape[1])
    cost = np.zeros(iters)

    for i in range(iters):
        error = (X * theta.T) - y

        for j in range(parameters):
            term = np.multiply(error, X[:, j])
            temp[0, j] = theta[0, j] - ((alpha / len(X)) * np.sum(term))

        theta = temp
        cost[i] = computeCost(X, y, theta)

    return theta, cost


alpha = 0.01
iters = 1000
g, cost = gradientDescent(X, y, theta, alpha, iters)
print(g)
computeCost(X, y, g)
x = np.linspace(data.Population.min(), data.Population.max(), 100)
f = g[0, 0] + (g[0, 1] * x)

fig, ax = plt.subplots(figsize=(12, 8))
ax.plot(x, f, 'r', label='Prediction')
ax.scatter(data.Population, data.Profit, label='Traning Data')
ax.legend(loc=2)
ax.set_xlabel('Population')
ax.set_ylabel('Profit')
ax.set_title('Predicted Profit vs. Population Size')
plt.show()
fig, ax = plt.subplots(figsize=(12, 8))
ax.plot(np.arange(iters), cost, 'r')
ax.set_xlabel('Iterations')
ax.set_ylabel('Cost')
ax.set_title('Error vs. Training Epoch')
plt.show()
