#推荐系统 6.1节
import numpy as np

scoreData = np.mat([
[5,2,1,4,0,0,2,4,0,0,0],
[0,0,0,0,0,0,0,0,0,3,0],
[1,0,5,2,0,0,3,0,3,0,1],
[0,5,0,0,4,0,1,0,0,0,0],
[0,0,0,0,0,4,0,0,0,4,0],
[0,0,1,0,0,0,1,0,0,5,0],
[5,0,2,4,2,1,0,3,0,1,0],
[0,4,0,0,5,4,0,0,0,0,5],
[0,0,0,0,0,0,4,0,4,5,0],
[0,0,0,4,0,0,1,5,0,0,0],
[0,0,0,0,4,5,0,0,0,0,3],
[4,2,1,4,0,0,2,4,0,0,0],
[0,1,4,1,2,1,5,0,5,0,0],
[0,0,0,0,0,4,0,0,0,4,0],
[2,5,0,0,4,0,0,0,0,0,0],
[5,0,0,0,0,0,0,4,2,0,0],
[0,2,4,0,4,3,4,0,0,0,0],
[0,3,5,1,0,0,4,1,0,0,0]
])

def cosSim(vec_1, vec_2):
    dotProd = float(np.dot(vec_1.T, vec_2))
    normProd = np.linalg.norm(vec_1)*np.linalg.norm(vec_2)
    return 0.5+0.5*(dotProd/normProd)

#估计第userIndex个顾客对第itemIndex个菜品的评分
#需要计算第itemIndex个菜品与顾客userIndex打过分的其他菜品的相似度
def estScore(scoreData,scoreDataRC,userIndex,itemIndex):
    n = np.shape(scoreData)[1]
    simSum = 0               #记录itemIndex菜品与其他已打分菜品相似度的和
    simSumScore = 0          #记录itemIndex菜品与其他已打分菜品的加权相似度之和，其中权重是用户打分值
    for i in range(n):
        userScore = scoreData[userIndex,i]
        if userScore == 0 or i == itemIndex:#如果顾客userIndex没有对第i道菜打分 或者 是要估计的菜品
            continue
        sim = cosSim(scoreDataRC[:, i], scoreDataRC[:, itemIndex]) #scoreDataRC[:, i]：第i道菜的所有分数
        simSum = float(simSum + sim)
        simSumScore = simSumScore + userScore * sim
    if simSum == 0:
        return 0
    return simSumScore / simSum

#利用奇异值分解对原始打分矩阵进行降维
#1. 奇异值分解，scoreData是18*11矩阵，所以U是18*18,VT为11*11
U, sigma, VT = np.linalg.svd(scoreData)

#2. 找出占优势的k个奇异值
sigmaSum = 0
k_num = 0
for k in range(len(sigma)):
    sigmaSum = sigmaSum + sigma[k] * sigma[k]
    if float(sigmaSum)/float(np.sum(sigma ** 2)) > 0.9: #阈值设为0.9
        k_num = k+1
        break
print("需要{}个奇异值".format(k_num))
sigma_K = np.mat(np.eye(k_num)*sigma[:k_num])  #本例需要6个奇异值。先形成一个由6个奇异值形成的对角矩阵
#U.T[:k_num, :]是U.T这个矩阵的前k_num行构成的矩阵，本例中为6*18矩阵
#scoreDataRC 是6*11矩阵    从18*11降维到6*11
scoreDataRC = sigma_K * U.T[:k_num, :] * scoreData #  乘以sigma_K是为了赋予权重
print("=================  scoreDataRC  ===================\n")
print(scoreDataRC)
print("=================  ============  ===================\n")

n = np.shape(scoreData)[1] #原始打分表里有多少列n
userIndex = 17  #我们想估计最后一个人对菜品的打分

for i in range(n): #对每一道菜，
    userScore = scoreData[userIndex, i] #判断最后一个用户是否对第i道菜打过分
    if userScore != 0:  #打过分的菜不需要参与评估
        continue
    print("index:{},score:{}".format(i, estScore(scoreData, scoreDataRC, userIndex, i)))

'''
#图像压缩
from PIL import Image
def loadImage(path):
    # 读取图片
    im = Image.open(path)
    # 显示图片
    #im.show()
    #转换为黑白图片
    im = im.convert("L")
    #显示黑白图片
    im.show()
    return im

def max (n):
    #将奇异值换成对角矩阵
    data_val_any = np.diag(data_val[: n])
    mat_new_any = data_vec1[:, 0:n]@data_val_any@data_vec2[0:n, :]
    return Image.fromarray(mat_new_any).show()

im = loadImage("eg.png")
data = im.getdata()
#转换为矩阵
data = np.array(data)
data =data.reshape(547, 547)

#取奇异值（data_val是一个奇异值的一维数组）
data_vec1, data_val, data_vec2 = np.linalg.svd(data)
print(len(data_val))
    
max(150)  #max(10), max(20), max(50)

'''
'''
#图像压缩 6.2节
import numpy as np
from PIL import Image

def imgCompress(channel,percent):
    U, sigma, V_T = np.linalg.svd(channel)
    m = U.shape[0]
    n = V_T.shape[0]
    reChannel = np.zeros((m,n))

    for k in range(len(sigma)):
        reChannel = reChannel + sigma[k]* np.dot(U[:,k].reshape(m,1),V_T[k,:].reshape(1,n))
        if float(k)/len(sigma) > percent:
            #测试数组中的每个元素看是否小于0或大于255
            reChannel[reChannel < 0] = 0
            reChannel[reChannel > 255] = 255
            break

    return np.rint(reChannel).astype("uint8") #rint舍入，astype将数组元素变为某种类型


oriImage = Image.open(r'test.png', 'r')
imgArray = np.array(oriImage)

R = imgArray[:, :, 0]
G = imgArray[:, :, 1]
B = imgArray[:, :, 2]
A = imgArray[:, :, 3]

for p in [0.001,0.005,0.01,0.02,0.03,0.04,0.05,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]:
    reR = imgCompress(R, p)
    reG = imgCompress(G, p)
    reB = imgCompress(B, p)
    reA = imgCompress(A, p)
    #reR,...,reA都是二维数组
    #用np.stack变为一个三维数组，axis=2时
    reI = np.stack((reR, reG, reB, reA), 2)

    Image.fromarray(reI).save("{}".format(p)+"img.png") 
'''
