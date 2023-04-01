import numpy as np
import scipy
from scipy import linalg


#矩阵的秩
A_1 = np.array([[1, 1, 0],
              [1, 0, 1]])

A_2 = np.array([[1, 2, -1],
              [2, 4, -2]])

A_3 = np.array([[1, 0],
              [0, 1],
              [0, -1]])

A_4 = np.array([[1, 2],
              [1, 2],
              [-1, -2]])

A_5 = np.array([[1, 1, 1],
              [1, 1, 2],
              [1, 2, 3]])

print(np.linalg.matrix_rank(A_1))
print(np.linalg.matrix_rank(A_2))
print(np.linalg.matrix_rank(A_3))
print(np.linalg.matrix_rank(A_4))
print(np.linalg.matrix_rank(A_5))

print ("矩阵行列式:", np.linalg.det(A_5))
#求矩阵的逆
A = np.array([[1, 35, 0],
              [0, 2, 3],
              [0, 0, 4]])
ainv = np.linalg.inv(A)  
print ('A 的逆ainv：',ainv)

A_n = linalg.inv(A)
print('A 的逆：A_n',A_n)

print(np.dot(A, A_n))
#一个不可逆矩阵
##B = np.array([[1, 0, 2],
##              [0, 1, 3],
##              [1, 1, 5]])
##B_n = linalg.inv(B)
##print(B_n)

#求解线性方程组
A = np.array([[1, 2, 3],
              [1, -1, 4],
              [2, 3, -1]])

y = np.array([14, 11, 5])
x = np.linalg.solve(A,y)
print("线性方程组的解为: x=",x)
x = linalg.solve(A, y)
print("线性方程组的解为: x=",x)

lu, piv = linalg.lu_factor(A)
print(lu)
print(piv)
x = linalg.lu_solve((lu, piv), y)
print("线性方程组的解为: x=",x)

#求矩阵的特征值和特征向量(eigenvalue,eigenvector)
#与笔算结果比较一下
#以下两个例子为特征值两两不等的情况
A = np.array([[2, 1],
              [1, 2]])
evalue, evector = np.linalg.eig(A)
print("特征值：", evalue)
print("特征向量：", evector)
evalue, evector = linalg.eig(A)
print("特征值：", evalue)
print("特征向量：", evector)
print("===================")
A = np.array([[1, 0, 0],
              [0, 2, 0],
              [0, 0, 5]])
evalue, evector = np.linalg.eig(A)
print("特征值：", evalue)
print("特征向量：", evector)
evalue, evector = linalg.eig(A)
print("特征值：", evalue)
print("特征向量：", evector)
print("===================")
#以下的例子有相同的特征值
#这个例子可以找到3个线性无关的特征向量
A = np.array([[1, 6, 0],
              [2, 2, 0],
              [0, 0, 5]])

evalue, evector = np.linalg.eig(A)
print("特征值：", evalue)
print("特征向量：", evector)
evalue, evector = linalg.eig(A)
print("特征值：", evalue)
print("特征向量：", evector)
print("===================")
#下面的例子无法找到3个线性无关的特征向量
A = np.array([[6, -2, 1],
              [0, 4, 0],
              [0,0,6]])

evalue, evector = linalg.eig(A)
print("特征值：", evalue)
print("特征向量：", evector)


#中英文均有的数据，可以考虑用genfromtxt
'''
delimiter: the str used to separate data.
如本例中横纵坐标以 ',' 分割，因此给 delimiter 传入 ','。
skip_header: the number of lines to skip at the beginning of the file.
dtype：数据类型
'''
data2=np.genfromtxt('test2.txt',skip_header=0,dtype='U',delimiter=',')
print(data2)
'''
#中英文均有的数据，用loadtxt处理时会有一些问题，比如下面的就会报错
info = np.loadtxt('test2.txt', dtype=bytes, delimiter=',', unpack=False)
print(info)
'''
