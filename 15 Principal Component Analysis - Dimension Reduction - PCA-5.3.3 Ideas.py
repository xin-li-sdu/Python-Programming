import numpy as np
from scipy import linalg

#先看hstack,vstack
#hstack(数组序列):按水平方向拼接
#数组序列中的每个数组对应元素拼接
#如果数组序列中的数组是一维的,则元素个数可以不一样
arrayseq = ([1,2,3,3,4],[3,4,5,8,6,6,7])
print(np.hstack(arrayseq))
'''
#如果数组序列中的数组不是一维的,
#则整体上,数组的元素个数要一样；
#下面这样就会出错
array1 = [[1,2,3],[2,3,4]] 
array2 = [[1,2]]           
arrayseq = (array1,array2)
print(np.hstack(arrayseq))

#但数组每一个元素如果还是数组的话，
#那么如果最后拼接那一下是一维数组拼接，元素个数可以不一样
#否则必须一样
#比如下面四个例子，第一个例子里最后拼接那一下是一维数组拼接
#第二个例子里最后拼接那一下不是一维数组拼接
'''
array1 = [[1,2,3],[2,3,4]] 
array2 = [[1,2],[2,3]]     
arrayseq = (array1,array2)
print(np.hstack(arrayseq))

#下面是诸如[[1,2,3],[2,3,4]]和[[11,12,13]]拼接成[[1,2,3],[2,3,4],[11,12,13]]
#此时要求。。。。。
array1 = [ [[1,2,3],[2,3,4]], [[5,6,7],[6,7,8]] ] 
array2 = [ [[11,12,13]], [[15,16,17]] ]     
arrayseq = (array1,array2)
print(np.hstack(arrayseq))
'''
#如果是这样就会出错
#很显然[[1,2,3],[2,3,4]]和[[12,13]]拼接成[[1,2,3],[2,3,4],[12,13]]是不允许的
array1 = [ [[1,2,3],[2,3,4]], [[5,6,7],[6,7,8]] ] 
array2 = [ [[11,12]], [[15,16]] ]     
arrayseq = (array1,array2)
print(np.hstack(arrayseq))
'''
print("hstack test over...........")
#================================

#vstack(数组序列):按竖直方向拼接
#数组序列中的每个数组整体拼接
#如果数组序列中的数组是一维的,则元素个数必须一样
#这很好理解，如下面的例子[1,2,3]和[3,4,3]拼接为[[1,2,3],[3,4,3]]
#显然要求元素个数一致
array1 = [1,2,3] 
array2 = [3,4,3]
arrayseq = (array1,array2)
print(np.vstack(arrayseq))

'''
#下面会出错
array1 = [1,2,3] 
array2 = [2,3]
arrayseq = (array1,array2)
print(np.vstack(arrayseq))
'''
#如果数组序列中的数组不是一维的,
#则整体上,数组的元素个数可以不一样；
array1 = [[1,2,3],[3,4,3]] 
array2 = [[1,3,4]]
arrayseq = (array1,array2)
print(np.vstack(arrayseq))

print("vstack test over...........")
#====================================
print("测试均值、方差")
eng, mat, phy = np.loadtxt('score.csv', delimiter=',',
                           usecols=(0, 1, 2), unpack=True)
print("eng:",eng)
print("mat:",mat)
print("phy:",phy)
print(eng.mean(), mat.mean(), phy.mean())
print(np.cov(eng), np.cov(mat), np.cov(phy))
print("测试均值、方差 over.............")
#=================================
#下面开始PCA

x = [2,2,4,8,4]
y = [2,6,6,8,8]
#零均值化，将样本变为均值为0的新样本
x = x - np.mean(x)
y = y - np.mean(y)

S = np.vstack((x,y))
print(S)
C = np.cov(S) #计算零均值化后的样本的协方差矩阵
print(C)

evalue, evector = linalg.eig(C)#求协方差矩阵的特征值与特征向量，特征向量线性无关
print(evalue)
print(evector)
#特征向量构成新的线性无关的基(正交)
P = np.vstack((evector.transpose()))
print(P)
Sproj = np.dot(P,S) #样本值向量在新的基下的投影
print(Sproj)
'''
A = np.vstack((x,y))
p_1 = [0.707, 0.707]
p_2 = [-0.707, 0.707]
P = np.vstack((p_1,p_2))
print(A)
print(np.dot(P,A))
'''
