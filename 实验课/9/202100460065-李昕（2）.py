import numpy as np
def cosSim(vec_1, vec_2): #衡量菜谱之间的相似性，采用余弦相似度的方法
    dotProd = float(np.dot(vec_1.T, vec_2))
    normProd = np.linalg.norm(vec_1)*np.linalg.norm(vec_2) 
    return 0.5+0.5*(dotProd/normProd) 



def estScore(scoreData,scoreDataRC,userIndex,itemIndex):
    simSum = 0 
    simSumScore = 0 
    for i in range(n):
        userScore = scoreData[userIndex,i]
        if userScore == 0 or i == itemIndex: 
            continue
        sim = cosSim(scoreDataRC[:, i], scoreDataRC[:, itemIndex]) 
        simSum = float(simSum + sim)
        simSumScore = simSumScore + userScore * sim 
    if simSum == 0:
        return 0
    return simSumScore / simSum

scoreData= np.array([[5, 2, 1, 4, 0, 0, 2, 4, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0],
                    [1, 0, 5, 2, 0, 0, 3, 0, 3, 0, 1],
                    [0, 5, 0, 0, 4, 0, 1, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 4, 0, 0, 0, 4, 0],
                    [0, 0, 1, 0, 0, 0, 1, 0, 0, 5, 0],
                    [5, 0, 2, 4, 2, 1, 0, 3, 0, 1, 0],
                    [0, 4, 0, 0, 5, 4, 0, 0, 0, 0, 5],
                    [0, 0, 0, 0, 0, 0, 4, 0, 4, 5, 0],
                    [0, 0, 0, 4, 0, 0, 1, 5, 0, 0, 0],
                    [0, 0, 0, 0, 4, 5, 0, 0, 0, 0, 3],
                    [4, 2, 1, 4, 0, 0, 2, 4, 0, 0, 0],
                    [0, 1, 4, 1, 2, 1, 5, 0, 5, 0, 0],
                    [0, 0, 0, 0, 0, 4, 0, 0, 0, 4, 0],
                    [2, 5, 0, 0, 4, 0, 0, 0, 0, 0, 0],
                    [5, 0, 0, 0, 0, 0, 0, 4, 2, 0, 0],
                    [0, 2, 4, 0, 4, 3, 4, 0, 0, 0, 0],
                    [0, 3, 5, 1, 0, 0, 4, 1, 0, 0, 0]])
U,sigma,VT = np.linalg.svd(scoreData)
sigma_K = np.mat(np.eye(6)*sigma[:6]) 
scoreDataRC = sigma_K * U.T[:6,:] * scoreData 

n = np.shape(scoreData)[1] #菜品总数
userlndex = 17
for i in range(n):
    userScore = scoreData[userlndex, i] 
    if userScore != 0:  
        continue
    print("index:{},score:{}".format(i, estScore(scoreData, scoreDataRC, userlndex, i)))

