import numpy as np
from matplotlib import pyplot as plt

mean_1 = np.array([3, 4])
mean_2 = np.array([0.0, 0.0])
cov_1 = np.array([[1.0, -0.5], [-0.5, 1.0]])
cov_2 = np.array([[0.45, 0.5], [-0.5, 0.6]])
data_1 = np.random.multivariate_normal(mean_1, cov_1, 200)
data_2 = np.random.multivariate_normal(mean_2, cov_2, 200)

plt.figure(0)
for i in range(data_1.shape[0]):
    plt.scatter(data_1[i][0], data_1[i][1], color='yellow')
for i in range(data_2.shape[0]):
    plt.scatter(data_2[i][0], data_2[i][1], color='pink')
plt.show()

f = open('appleLemon.txt', 'w')
for i in range(data_1.shape[0]):
    f.write(str(data_1[i][0]) + ' ' + str(data_1[i][1]) + ' ' + str(0.0) + '\n')
for i in range(data_2.shape[0]):
    f.write(str(data_2[i][0]) + ' ' + str(data_2[i][1]) + ' ' + str(1.0) + '\n')
f.close()
