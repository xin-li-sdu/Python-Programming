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
































