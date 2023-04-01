import numpy as np 

#有如下几种方式创建ndarray数组:
'''
(1) 用np.array从列表、元组创建
'''
print("==================   np.array   ==================")
# 从list创建array
a = np.array([1,2,3,4,5,6])
print(a)  # array([1, 2, 3, 4, 5, 6])
a = np.array((1,2,3,4))   
print(a)  # array([1, 2, 3, 4])
print(a.dtype)
a = np.array((1,2,3,4),dtype =  np.int8)   
print(a)  # array([1, 2, 3, 4])
print(a.dtype)

'''
(2) 指定起止范围及间隔创建
(2.1) numpy 包中的使用 arange 函数创建数值范围并返回 ndarray 对象，函数格式如下：numpy.arange(start, stop, step, dtype)
start：起始值，默认为0； 
stop：终止值（不包含）
step：步长，默认为1；   
dtype：ndarray中的数据类型，如果没有提供，则会使用输入数据的类型。
例如：通过指定start, stop，step来产生一个一维的ndarray
'''
print("==================   np.arange   ==================")
a = np.arange(5)  
print (a)

# 设置了 dtype
a = np.arange(5, dtype =  float)  
print (a)

a = np.arange(0, 20, 2) 
print(a)  #array([ 0,  2,  4,  6,  8, 10, 12, 14, 16, 18])

'''
(2.2) numpy.linspace 函数用于创建一个一维数组，数组是一个等差数列构成的，
格式如下：np.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None)
start：序列的起始值
stop：序列的终止值，如果endpoint为true，该值包含于数列中
num：要生成的等步长的样本数量，默认为50
endpoint：值为 true 时，数列中包含stop值，反之不包含，默认是True。
retstep：如果为 True ，生成的数组中会显示间距，反之不显示。默认是False。
dtype：ndarray的数据类型
'''
print("==================   np.linspace   ==================")
#设置起始点为 1 ，终止点为 10，数列个数为 10。
a = np.linspace(1,10,10,retstep = True)
print(a)
a = np.linspace(1,10,10)
print(a)
#设置元素全部是1的等差数列：
a = np.linspace(1,1,10)
print(a)
print(a.dtype)

'''
(2.3) numpy.logspace 函数用于创建一个等比数列。格式如下：
np.logspace(start, stop, num=50, endpoint=True, base=10.0, dtype=None)
start：序列的起始值为：base ** start
stop：序列的终止值为：base ** stop。如果endpoint为true，该值包含于数列中。
num：要生成的等步长的样本数量，默认为50
endpoint：值为 true 时，数列中包含stop值，反之不包含，默认是True。
base：对数 log 的底数。
dtype：ndarray的数据类型
'''
print("==================   np.logspace   ==================")
# 默认底数是 10
a = np.logspace(1.0,  2.0, num =  10)  
print (a)
#将对数的底数设置为 2 :
a = np.logspace(0,9,10,base=2)
print (a)
'''
(3) numpy.empty方法用来创建一个指定形状（shape）、数据类型（dtype）
   且未初始化的数组：numpy.empty(shape, dtype = float, order = 'C')
order有"C"和"F"两个选项,分别代表行优先和列优先，在计算机内存中的存储元素的顺序。
 shape : int or tuple of int
'''
print("==================   np.empty   ==================")
x = np.empty([3,2], dtype = int) 
print (x)
x = np.empty((3,2), dtype = int) 
print (x)
y = np.empty([4,2], dtype = int) 
print (y)

'''
(4) numpy.zeros创建指定大小的数组，数组元素以 0 来填充：
numpy.zeros(shape, dtype = float, order = 'C')
'''
print("==================   np.zeros   ==================")
a = np.zeros([3,3])
print(a)
'''
(5) numpy.ones创建指定形状的数组，数组元素以 1 来填充：
'''
print("==================   np.ones   ==================")
a = np.ones([3,3])
print(a)
'''
(6) numpy.eye创建单位矩阵数组
'''
print("==================   np.eye   ==================")

a = np.eye(5)
print(a)

'''
(7) numpy.random.randn创建标准正态分布数组：
# randn(size) 创建服从 X~N(0,1) 的正态分布随机数组
'''
print("==================   np..random.randn   ==================")
a = np.random.randn(2,3)
print(a)

'''
(8) numpy.random.randint([low,high],size)创建随机分布整数型数组。
利用 randint([low,high],size) 创建一个整数型指定范围在 [low.high] 之间的数组
'''
print("==================   np.random.randint   ==================")

a = np.random.randint(100,200,(3,3))
print(a)

'''
(9) 从已有的数组创建数组
(9.1) numpy.asarray
numpy.asarray类似numpy.array，格式为：
numpy.asarray(a, dtype = None, order = None)
'''
print("==================   np.asarray   ==================")

#将列表转换为 ndarray:
x =  [1,2,3] 
a = np.asarray(x)  
print (a)

#将元组转换为 ndarray:
x =  (1,2,3) 
a = np.asarray(x)  
print (a)

#设置了 dtype 参数：
x =  [1,2,3] 
a = np.asarray(x, dtype =  float)  
print (a)
'''
(9.2) numpy.frombuffer 用于实现动态数组。
numpy.frombuffer(buffer, dtype = float, count = -1, offset = 0)
buffer	可以是任意对象，会以流的形式读入。
dtype	返回数组的数据类型，可选
count	读取的数据数量，默认为-1，读取所有数据。
offset	读取的起始位置，默认为0。
注意：buffer 是字符串的时候，frombuffer要求是字节串
而Python3 默认 str 是 Unicode 类型，
所以要转成 bytestring 在原 str 前加上 b。
'''
print("==================   np.frombuffer   ==================")
s =  b'Hello World'
a = np.frombuffer(s, dtype =  'S1')  
print (a)

'''
(9.3) numpy.fromiter 方法从可迭代对象中建立 ndarray 对象，返回一维数组。
numpy.fromiter(iterable, dtype, count=-1)
iterable	可迭代对象
dtype	返回数组的数据类型
count	读取的数据数量，默认为-1，读取所有数据
'''
print("==================   np.fromiter   ==================")

# 使用 range 函数创建列表对象  
lst=range(5)
it=iter(lst)
 
# 使用迭代器创建 ndarray 
a=np.fromiter(it, dtype=float)
print(a)

#使用reshape
print("==================   np.reshape   ==================")

a=np.array([[1,2,3],[4,5,6]])
b=a.reshape((6,)) #array([1, 2, 3, 4, 5, 6])
print(b)
c=a.reshape(6) #array([1, 2, 3, 4, 5, 6])
print(c)
b[0]=100        #array([100,   2,   3,   4,   5,   6])
print(a)

a = np.arange(1,25).reshape(2,3,4) #3个参数，三维数组
print(a)

y6 = np.arange(1,9).reshape(-1,2)
print(y6)  






















