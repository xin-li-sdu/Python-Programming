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

