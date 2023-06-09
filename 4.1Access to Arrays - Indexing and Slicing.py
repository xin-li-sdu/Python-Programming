import numpy as np
 
a = np.arange(10)
print("a=",a)
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
print("a = ", a)
print("a[0] = ", a[0])
print("a[0][1] = ", a[0][1])
print("a[0,1] = ", a[0,1])       #也可以用逗号，方括号内逗号隔开从左向右依次表示0轴、1轴依次类推
print("a[1,:] = ", a[1,:])       #表示轴0只取第2个元素，轴1方向全取
print("a[1,...] = ", a[1,...])   #用省略号…占住一个轴，该轴的元素全取
print("a[:,0] = ", a[:,0])       #轴0方向全取，但轴1只取第1个元素
print("a[...,0] = ", a[...,0])
print("a[0:2,1:3] = ", a[0:2,1:3])
print("a[0][:] = ", a[0][:])     #相当于一维数组的切片，与a[0,:]一样
#下面这三个例子要注意
print("a[:][0] = ", a[:][0])     #这个又不一样,a[:]相当于整个数组a,所以a[:][0]相当于a[0]
print("a[...][0]=", a[...][0])
print("a[1:][0]=", a[1:][0])
# 从某个索引处开始切割
print("================   二维数组情形   ===================")
a = np.array([[1,2,3],[3,4,5],[4,5,6],[5,6,7],[6,7,8]]) #二维数组
print("a[1:] = ",a[1:])
print("a[1:4:2] = ",a[1:4:2])

print("================   三维数组情形   ===================")
y = np.array([ [[0,0,0,0],[1,1,1,1]], [[1,1,1,1],[2,2,2,2]], [[2,2,2,2],[3,3,3,3]] ])   #创建三维数组
print("y[1:] = ",y[1:])
print("y[:,0,1:3] = ", y[:,0,1:3])  #轴0方向全都要取，轴1方向只取第一个元素，轴2方向取第2、3个元素



