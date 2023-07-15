
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

########################################
import numpy as np
 
a = np.arange(10)
b = a[2:7:2]   # 从索引 2 开始到索引 7 停止，间隔为 2
print ("a[2:7:2] = ", b)
print("================================")
'''
如果只放置一个参数，如 [2]，将返回与该索引相对应的单个元素。
如果为 [2:]，表示从该索引开始以后的所有项都将被提取。
如果使用了两个参数，如 [2:7]，那么则提取两个索引(不包括停止索引)之间的项。
'''
b = a[2]   
print ("a[2] = ", b)
b = a[2:]   
print ("a[2:] = ", b)
b = a[2:7]   
print ("a[2:7] = ", b)
print("================================")
 
'''
多维数组
'''
a = np.array([[1,2,3],[3,4,5],[4,5,6]]) #二维数组
print("a[0] = ", a[0])
print("a[0][1] = ", a[0][1])
print("a[0,1] = ", a[0,1])       #也可以用逗号，方括号内逗号隔开从左向右依次表示0轴、1轴依次类推
print("a[1,:] = ", a[1,:])       #表示轴0只取第2个元素，轴1方向全取
print("a[1,...] = ", a[1,...])   #用省略号…占住一个轴，该轴的元素全取
print("a[:,0] = ", a[:,0])       #轴0方向全取，但轴1只取第1个元素
print("a[...,0] = ", a[...,0])
print("a[0:2,1:3] = ", a[0:2,1:3])
print("a[0][:] = ", a[0][:])     #相当于一维数组的切片
print("a[:][0] = ", a[:][0])     #这个又不一样,a[:]相当于整个数组a,所以a[:][0]相当于a[0]
 
# 从某个索引处开始切割
print("================   二维数组情形   ===================")
a = np.array([[1,2,3],[3,4,5],[4,5,6],[5,6,7],[6,7,8]]) #二维数组
print("a[1:] = ",a[1:])
print("a[1:4:2] = ",a[1:4:2])
 
print("================   三维数组情形   ===================")
y = np.array([ [[0,0,0,0],[1,1,1,1]], [[1,1,1,1],[2,2,2,2]], [[2,2,2,2],[3,3,3,3]] ])   #创建三维数组
print("y[1:] = ",y[1:])
print("y[:,0,1:3] = ", y[:,0,1:3])  #轴0方向全都要取，轴1方向只取第一个元素，轴2方向取第2、3个元素


################
import numpy as np
 
x = np.array([[1,2],[3,4], [5,6]])
#[0,1,2]:0轴上取得元素位置，[0,1,0]:1轴上取得元素位置
#所以取的是x[0][0],x[1][1],x[2][0]
print("x[[0,2]] = ", x[ [0,2] ])
print ("x[[0,1,2], [0,1,0]] = ")
print(x[[0,1,2],[0,1,0]])  # [1 4 5]
print("\n")
 
a = np.array(np.arange(0,16).reshape(4,4))
print("a = ", a)
print("\n")
print("a[[0,1,2,3],[0,1,2,3]] = ")
print(a[[0,1,2,3],[0,1,2,3]])
print("\n")
print("a[[1,3], [1,3]] = ")
print(a[[1,3], [1,3]])
print("\n")
print("a[[3,2,1,0]] = ")
print(a[[3,2,1,0]])  #取a的第3、2、1、0行元素
 
print("===============  借助切片, 与索引数组组合  =================")
'''
如果想取某些行的某几个元素，比如第0，2行的1，2，3元素
则可以借助切片, 与索引数组组合
'''
print("a[[1,3], 1:3] = ") 
print(a[[1,3], 1:3])         #第1，3行的1，2元素
print("\n")
print("a[1:3, [1,3]] = ")
print(a[1:3, [1,3]])         #第1，3列的1，2元素
print("\n")
#或者
#np.ix_函数就是输入两个数组，产生笛卡尔积的映射关系
print("a[np.ix_([1,3],[1,2])] = ") #取(1,1),(1,2),(3,1),(3,2) 4个元素
print(a[np.ix_([1,3],[1,2])])
print("\n")
print("a[np.ix_([1,2],[1,3])] = ")
print(a[np.ix_([1,2],[1,3])])
print("\n")
print("a[np.ix_([0,2],[1,2,3])] = ")
print(a[np.ix_([0,2],[1,2,3])])
print("================================")
 
'''
布尔索引
'''
print("===============  布尔索引  =================")
print("a[[True,False,False,True]] = ")
print(a[[True,False,False,True]])
print("\n")
print("a[ :, [True,False,False,True] = ")
print(a[ :, [True,False,False,True]])
print("\n")
print("a[[True,True,False,True],[True,True,False,True]] = ")
print(a[[True,True,False,True],[True,True,False,True]])
print("\n")
print("a>5 返回:", a>5)
print("a[a>5] = ")
print(a[a>5])
print("\n")
#
names = np.array(['Bob', 'Tom', 'Joy', 'Bob', 'Mark'], dtype='<U4')
data = np.array([[0.53907488, 0.08239029, 0.49606765, 0.84466126, 0.78326342],
                 [0.64214005, 0.2917917 , 0.96583067, 0.377151  , 0.34873902],
                 [0.82531799, 0.61300945, 0.58824431, 0.16859125, 0.42529735],
                 [0.96789188, 0.08368161, 0.25979403, 0.95384036, 0.77921917],
                 [0.83331394, 0.60851424, 0.10917665, 0.04371444, 0.6726732 ]])
print("========== all man ==========")
print(names)
 
print("========== all data ==========")
print(data)
 
print("========== Tom\'s data ==========")
print(names=="Tom") #[False  True False False False]
print(data[names=='Tom'])
 
print("========== Bob\'s data ==========")
print(data[names=='Bob'])
 
print("========== Tom\'s first and second data ==========")
print(data[names=='Tom', :2]) #与切片配合
 
print("========== data except Tom\'s ==========")
print(data[names!='Tom'])
 
print(data[~(names=='Tom')])
 
print("========== Tom and Bob\'s  data ==========")
print(data[(names=='Bob') & (names=='Tom')])
 
print("========== Tom or Bob\'s data ==========")
print(data[(names=='Bob') | (names=='Tom')])
 
 
x=np.array([1,-1,-2,3])
x[x<0]+=20  #所有小于0的x中的元素+20
print("==========  X ===========")
print(x)
 ######################

 import numpy as np
 
'''
numpy.reshape 函数可以在不改变数据的条件下修改形状
'''
print("===============   numpy.reshape()  ==================")
a = np.arange(8)
print ('原始数组：')
print (a)
print ('\n')
 
b = a.reshape(4,2)
print ('修改后的数组：')
print (b)
b[0][1]=100
print (b)
print (a)
 
'''
numpy.ndarray.flat 是一个数组元素迭代器
'''
print("===============   numpy.ndarray.flat  ==================")
a = np.arange(9).reshape(3,3) 
print ('原始数组：')
print(a)
for row in a:#迭代每一行
    print (row)
 
#对数组中每个元素都进行处理，可以使用flat属性，该属性是一个数组元素迭代器：
print ('迭代后的数组：')
for element in a.flat:
    print (element)
 
'''
numpy.ndarray.flatten 返回一份数组展开后的拷贝，即，变为一维的，
对拷贝所做的修改不会影响原始数组
'''
print("===============   numpy.ndarray.flatten()  ==================")
a = np.arange(8).reshape(2,4)
print ('原数组：')
print (a)
print ('\n')
# 默认按行
print ('展开的数组：')
b = a.flatten()
print (b)
b[0] = -1
print("修改flatten后的数组后")
print("a = ", a)
print("b = ", b)
print ('\n')
 
print ('以 F 风格顺序（按列）展开的数组：')
print (a.flatten(order = 'F'))
 
'''
numpy.ravel() 展开数组元素，顺序通常是"C风格"（按行），
返回的是数组视图，
修改会影响原始数组。
'''
print("===============   numpy.ndarray.ravel()  ==================")
a = np.arange(8).reshape(2,4)
print ('原数组：')
print (a)
print ('\n')
print ('调用 ravel 函数之后：')
b = a.ravel()
print (b)
b[0] = -1
print("修改ravel后的数组后")
print("a = ", a)
print("b = ", b)
print ('\n')
 
print ('以 F 风格顺序（按列）调用 ravel 函数之后：')
print (a.ravel(order = 'F'))
 
'''
numpy.transpose 函数用于对换数组的维度，格式如下：
numpy.transpose(arr, axes)
arr：要操作的数组
axes：整数列表，对应维度，通常所有维度都会对换。
主要就是：转置，当然只有在矩阵里才叫转置
'''
print("===============   numpy.transpose()  ==================")
a = np.arange(12).reshape(3,4) 
print ('原数组：')
print (a )
print ('\n')
 
print ('transpose转置后的数组：')
print (np.transpose(a))
#numpy.ndarray.T 类似 numpy.transpose：
print ('数组a.T：')
print (a.T)
print ('\n')
 
'''
numpy.concatenate 函数用于沿指定轴连接相同形状的两个或多个数组，
格式：numpy.concatenate((a1, a2, ...), axis)
参数说明：
a1, a2, ...：相同类型的数组
axis：沿着它连接数组的轴，默认为 0
'''
print("===============   numpy.concatenate()  ==================")
a = np.array([[1,2],[3,4]]) 
print ('第一个数组：')
print (a)
print ('\n')
b = np.array([[5,6],[7,8]])
 
print ('第二个数组：')
print (b)
print ('\n')
# 两个数组的维度相同 
print ('沿轴 0 连接两个数组：')
print (np.concatenate((a,b)))
print ('\n')
 
print ('沿轴 1 连接两个数组：')
print (np.concatenate((a,b),axis = 1))
 
'''
numpy.stack 函数用于沿新轴连接数组序列，格式如下：
numpy.stack(arrays, axis)
参数说明：
arrays相同形状的数组序列
axis：数组中的轴，输入数组沿着它来连接
返回的结果比arrays多一个维度
'''
print("===============   numpy.stack()  ==================")
a = np.array([[1,2],[3,4]]) 
print ('第一个数组：')
print (a)
print ('\n')
b = np.array([[5,6],[7,8]])
 
print ('第二个数组：')
print (b)
print ('\n')
 
print ('沿轴 0 堆叠两个数组：')
print (np.stack((a,b),0))
print ('\n')
 
print ('沿轴 1 堆叠两个数组：')
print (np.stack((a,b),1))
 
'''
numpy.hstack 是 numpy.stack 函数的变体，它通过水平堆叠来生成数组。
其实更像是数组连接concatenate
'''
print("===============   numpy.hstack()  ==================")
a = np.array([[1,2],[3,4]]) 
print ('第一个数组：')
print (a)
print ('\n')
b = np.array([[5,6],[7,8]]) 
print ('第二个数组：')
print (b)
print ('\n') 
print ('水平堆叠：')
c = np.hstack((a,b))
print (c)
print ('\n')
 
'''
numpy.vstack 是 numpy.stack 函数的变体，它通过垂直堆叠来生成数组。
其实更像是数组连接concatenate
'''
print("===============   numpy.vstack()  ==================")
a = np.array([[1,2],[3,4]]) 
print ('第一个数组：')
print (a)
print ('\n')
b = np.array([[5,6],[7,8]]) 
print ('第二个数组：')
print (b)
print ('\n') 
print ('竖直堆叠：')
c = np.vstack((a,b))
print (c)
 
'''
numpy.resize 函数返回指定大小的新数组。
如果新数组大小大于原始大小，则包含原始数组中的元素的副本。
numpy.resize(arr, shape)
参数说明：
arr：要修改大小的数组
shape：返回数组的新形状
'''
print("===============   numpy.resize()  ==================")
a = np.array([[1,2,3],[4,5,6]]) 
print ('第一个数组：')
print (a)
print ('\n') 
print ('第一个数组的形状：')
print (a.shape)
print ('\n')
b = np.resize(a, (3,2)) 
print ('第二个数组：')
print (b)
print ('\n') 
print ('第二个数组的形状：')
print (b.shape)
print ('\n')
# 要注意 a 的第一行在 b 中重复出现，因为尺寸变大了.
# 广播？
print ('修改第二个数组的大小：')
b = np.resize(a,(3,3))
print (b)
 
'''
numpy.append 函数在数组的末尾添加值。 追加操作会分配整个数组，并把原来的数组复制到新数组中。
此外，输入数组的维度必须匹配否则将生成ValueError。
numpy.append(arr, values, axis=None)
参数说明：
arr：输入数组
values：要向arr添加的值，需要和arr形状相同（除了要添加的轴）
axis：默认为 None。当axis无定义时，是横向加成，返回总是为一维数组！
当axis有定义的时候，分别为0和1的时候（列数要相同）。当axis为1时，数组是加在右边（行数要相同）。
'''
print("===============   numpy.append()  ==================")
a = np.array([[1,2,3],[4,5,6]]) 
print ('第一个数组：')
print (a)
print ('\n') 
print ('向数组添加元素：')
print (np.append(a, [7,8,9]))
print ('\n') 
print ('沿轴 0 添加元素：')
print (np.append(a, [[5,5,5],[7,8,9]],axis = 0))
print ('\n') 
print ('沿轴 1 添加元素：')
print (np.append(a, [[5,5,5],[7,8,9]],axis = 1))
 
'''
numpy.insert 函数在给定索引之前，沿给定轴在输入数组中插入值。
如果值的类型转换为要插入，则它与输入数组不同。
插入没有原地的，函数会返回一个新数组。
此外，如果未提供轴，则输入数组会被展开。
numpy.insert(arr, obj, values, axis)
参数说明：
arr：输入数组
obj：在其之前插入值的索引
values：要插入的值
axis：沿着它插入的轴，如果未提供，则输入数组会被展开
'''
print("===============   numpy.insert()  ==================")
a = np.array([[1,2],[3,4],[5,6]]) 
print ('第一个数组：')
print (a)
print ('\n') 
print ('未传递 axis 参数。 在插入之前输入数组会被展开。')
print (np.insert(a,3,[11,12]))
print ('\n')
print ('传递了 axis 参数。 会广播值数组来匹配输入数组。') 
print ('沿轴 0 广播：')
print (np.insert(a,1,[11],axis = 0))
print ('\n') 
print ('沿轴 1 广播：')
print (np.insert(a,1,11,axis = 1))
 
'''
numpy.delete 函数返回从输入数组中删除指定子数组的新数组。
与 insert() 函数的情况一样，如果未提供轴参数，则输入数组将展开。
numpy.delete(arr, obj, axis)
参数说明：
arr：输入数组
obj：可以被切片，整数或者整数数组，表明要从输入数组删除的子数组(索引)
axis：沿着它删除给定子数组的轴，如果未提供，则输入数组会被展开
'''
print("===============   numpy.delete()  ==================")
a = np.arange(12).reshape(3,4)
a[1] = np.array([20,21,22,23])
print ('第一个数组：')
print (a)
print ('\n') 
print ('未传递 axis 参数。 在删除之前输入数组会被展开。')
print (np.delete(a,5))
print ('\n')
print ('删除第一行：')
print (np.delete(a,0,axis = 0))
print ('\n') 
print ('删除第二列：')
print (np.delete(a,1,axis = 1))
print ('\n') 
print ('包含从数组中删除的替代值的切片：')
a = np.array([1,2,3,4,5,6,7,8,9,10])
print (np.delete(a, np.s_[::2]))  #np.s_[::2]构造一个切片，从头到尾，步长为2
 
'''
numpy.unique 函数用于去除数组中的重复元素。
numpy.unique(arr, return_index, return_inverse, return_counts)
arr：输入数组，如果不是一维数组则会展开
return_index：如果为true，返回新列表元素在旧列表中的位置（下标），并以列表形式储
return_inverse：如果为true，返回旧列表元素在新列表中的位置（下标），并以列表形式储
return_counts：如果为true，返回去重数组中的元素在原数组中的出现次数
'''
print("===============   numpy.unique()  ==================")
a = np.array([5,2,6,2,7,5,6,8,2,9]) 
print ('第一个数组：')
print (a)
print ('\n') 
print ('第一个数组的去重值：')
u = np.unique(a)
print (u)
print ('\n') 
 
u,indices = np.unique(a, return_index = True)
print ('新列表{}各元素在旧列表中的位置为：{}'.format(u,indices))
print ('\n') 
 
u,indices = np.unique(a,return_inverse = True)
print ('旧列表{}各元素在新列表{}中的位置为：\n{}'.format(a,u,indices))
print ('\n') 
 
print ('使用下标重构原数组：')
print (u[indices])
print ('\n') 
 
u,count = np.unique(a,return_counts = True)
print ('新列表{}各元素在旧列表{}中的数量为：\n{}'.format(u,a,count))




##############
import numpy as np
 
'''
数组的+、-、*、/、//运算，要求参与运算的数组要同样大小，即维度和元素个数相同。
即，对应元素进行运算
'''
#对应元素进行运算
A = np.array([[1, 2],
              [3, 4],
              [5, 6]])
B = np.array([[10, 20],
              [30, 40],
              [50, 60]])
print("A+B = ", A+B)
print("A*B = ", A*B)
 
#每个元素都进行同样的运算
print("A+2 = ", A+2)
print("A*2 = ", A*2)
b = [[2,2],[2,2],[2,2]]
print("A+b = ", A+b)
#支持+=、／=、-=、*=这类运算符号
#并不会创建一个新的数组，而是直接对原来数组的元素值进行修改。
A += 2
print("A+=2后, A =  ", A)
 
#如果将二维数组视为矩阵，那么矩阵乘法为np.dot：
A = np.array([[1, 2],
              [3, 4],
              [5, 6],
              [7, 8]])
B = np.array([[2, 3, 4, 5],
                [6, 7, 8, 9]])
print(np.dot(A, B))
 
#数组向量乘
A = np.array([[1, 2],
               [3, 4],
               [5, 6]])
x = np.array([[4, 5]]).T
print(np.dot(A, x))


import numpy as np
 
a = np.array([1,2,3])
b = 2
print("a = ", a)
print("b = ", b)
print("a * b = ", a*b)
print("=====================")
 
a = np.zeros((2,3,4))
b = np.zeros((3,4))
print("a.shape = ", a.shape)
print("b.shape = ", b.shape)
print("(a+b).shape = ",(a+b).shape) # 输出 (2, 3, 4)
a = np.array([[[1,1,1,1],[2,2,2,2],[3,3,3,3]],[[4,4,4,4],[5,5,5,5],[6,6,6,6]]])
print("a = ", a)
print("a.shape = ", a.shape)
b = np.array([[1,1,1,1],[2,2,2,2],[3,3,3,3]])
print("b = ", b)
print("b.shape = ", b.shape)
c = a + b
print("a + b = ", c)
print("(a+b).shape = ", c.shape)
print("=====================")
 
a = np.array([[0],[1],[2],[3]])
print("a = ", a)
print("a.shape = ", a.shape)
b = np.array([1,2,3])
print("b = ", b)
print("b.shape = ", b.shape)
c = a + b
print("a + b = ", c)
print("(a+b).shape = ", c.shape)
print("=====================")
 
import numpy as np
 
array2 = np.arange(1,5)   #创建一维数组
print("array2 = ", array2)             
print(array2.ndim)         #输出array2的维数为1
print(array2.shape)        #输出array2的形状，行为4元素，列无
print(type(array2))        #输出array2的类型，N维数组类型
 
mat5 = np.mat(array2)      #利用mat()对一维数组创建矩阵mat5
print("mat5 = ", mat5)     #输出mat5
print(type(mat5)) 
print(mat5.ndim)           #输出mat5的维数为2
print(mat5.shape)          #输出mat5的形状，1行4列
print("\n")
 
list1 = [[1,2,3,4],[5,6,7,8]]
array1 = np.array(list1)
print("array1 = ", array1)
mat4 = np.mat(array1)
print("mat4 = ", mat4)
mat4[0,0] = -100
print("更改mat4[0,0]后的新mat4 = ", mat4) 
print("此时array1 = ", array1)  #说明np.mat返回视图
print("\n")
 
array2 = np.array([1,2,3,4])
mat5 = np.mat(array2)
print("mat5 = ", mat5)
mat5[0]=-100
print("更改mat5[0]=-100后的新mat5 = ", mat5)
print("此时数组array2 = ", array2) #说明np.mat返回视图
print("\n")
 
array2 = [1,2,3,4]
mat5 = np.mat(array2)
print("mat5 = ", mat5)
mat5[0]=-100
print("更改mat5[0]=-100后的新mat5 = ", mat5)
print("此时列表array2 = ", array2) #不影响序列
 
print("====================================")
'''
列表、数组、矩阵间的相互转换
'''
list1 = [[0,1,2,3],[4,5,6,7]]
array1 = np.array(list1)  #列表转为数组
print("array1 type = ", type(array1))
print("array1 = ", array1)
mat1 = np.mat(array1)     #数组转为矩阵
print("mat1 type = ", type(mat1))
print("mat1 = ", mat1)
array2 = np.array(mat1)   #矩阵转为数组
print("array2 type = ", type(array2))
print("array2 = ", array2)
array3 = mat1.getA()     #矩阵转为数组
print("array3 type = ", type(array3))
print("array3 = ", array3)
list2 = mat1.tolist()   #矩阵转为列表
print("list2 from mattolist type = ", type(list2))
print("list2 = ", list2)
list3 = array3.tolist()  #数组转为列表
print("list3 from arraytolist type = ", type(list3))
print("list3 = ", list3)
#array1(mat)--> mat1 (np.array(mat1)) --> array2
array2[0]=-999
print("new array2 = ", array2)
print("array1 = ", array1)
#array1(mat)--> mat1 (getA) --> array3
array3[0]=-100
print("new array3 = ", array3)
print("array1 = ", array1)



import numpy as np
'''
矩阵的加减乘运算
'''
a = np.mat(np.arange(1,7).reshape(2,3))
 
b = a
print("a = ", a)
print("b = ", b)
print("a + b = ", a + b)       #矩阵相加，同型矩阵
 
print("a - b = ", a - b)        #矩阵相减，同型矩阵
 
print("======================================")
 
c = np.mat(np.arange(1,7).reshape(3,2))
print("c = ", c)
 
print("a * c = ", a * c)  #矩阵相乘，a的列数等于矩阵c的行数
print("np.dot(a,c) = ", np.dot(a,c))
print("2 * a = ", 2 * a)         #数乘矩阵
print("a * 2 = ", a * 2)
 
'''
矩阵的转置和求逆
'''
print("a.T = ", a.T)         #矩阵转置
print("a.I = ", a.I)         #求逆矩阵
 
'''
矩阵的求和及索引
'''
print("矩阵每一列的和 = ", a.sum(axis = 0))    #计算矩阵每一列的和
 
print("矩阵每一行的和 = ", a.sum(axis = 1))    #计算矩阵每一行的和
 
print("矩阵每一列的最大值 = ", a.max(axis = 0))    #计算矩阵每一列的最大值
 
print("矩阵每一行的最大值 = ", a.max(axis = 1))    #计算矩阵每一行的最大值
 
print("矩阵每一列的最大值索引 = ", a.argmax(axis = 0)) #计算矩阵每一列的最大值索引
 
print("矩阵矩阵每一行的最大值索引 = ", a.argmax(axis = 1)) #计算矩阵每一行的最大值索引
 
'''
矩阵的分割和合并
'''
print("========================  矩阵的分割和合并  ================")
mat1 = np.mat(np.arange(20).reshape(4,5))
print("矩阵mat1 = ", mat1)
 
#分割出行2（含）到最后行；列3（含）到最后列，所有元素
mat2 = mat1[2:,3:] 
print("矩阵mat1 行2（含）到最后行；列3（含）到最后列的所有元素 = \n", mat2)
 
#分割出开始到行2（不含）；所有列，所有元素
mat3 = mat1[:2,:]
print("矩阵mat1 开始到行2（不含）；所有列，所有元素, mat3= \n", mat3)
 
#分割出行2（含）到最后行；所有列，所有元素
mat4 = mat1[2:,:]
print("矩阵mat1 行2（含）到最后行；所有列，所有元素 = \n", mat4)
 
#分割出行2（含）到最后行；所有列，所有元素
mat4 = mat1[2:]
print("矩阵mat1 行2（含）到最后行；所有列，所有元素, mat4 = \n", mat4)
 
'''
#沿着第一个轴（轴0）堆叠数组。
#即列数不变，拼起每一行
如果是一维数组进行堆叠，则数组长度必须相同；
除此之外，其它数组堆叠时，除数组第一个轴的长度可以不同，
其它轴长度必须一样。
'''
mat5 = np.vstack((mat3,mat4))
print("mat3,mat4按轴0堆叠合并 = ", mat5)
 
'''
#沿着第二个轴（轴1）堆叠数组。
#即行数不变，拼起每一列
除了一维数组的堆叠可以是不同长度外，
其它数组堆叠时，除了第二个轴的长度可以不同外，其它轴的长度必须相同。
'''
mat6 = np.hstack((mat3,mat4))
print("mat3,mat4按轴1堆叠合并 = ", mat6)
 