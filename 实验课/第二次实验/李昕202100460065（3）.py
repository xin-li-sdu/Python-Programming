def sduxhplus(): #循环遍历不输出（3，3，3）
    for i in range(5):
        for j in range(5):
            for k in range(5):
                if(i==3 & j==3 & k==3):
                    continue
                else:
                    print(i,j,k)
sduxhplus