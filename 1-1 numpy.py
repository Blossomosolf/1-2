import numpy as np

#1.生成一個等差數列，首數為0，尾數為20，公差為1的數列。

data=np.arange(0.0, 21.0, 1.0, dtype='float64')
print(data)

#2.呈上題，將以上數列取出偶數。

data2=np.arange(0.0, 21.0, 2.0, dtype='float64')
print(data2)

#3.呈1題，將數列取出3的倍數。

data3=np.arange(0.0, 21.0, 3.0, dtype='float64')
print(data3)
