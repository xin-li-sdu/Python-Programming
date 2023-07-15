def sduxh(): #循环遍历
    tag=True
    for i in range(5):
        if(tag==False):
                break
        for j in range(5):
            if(tag==False):
                break
            for k in range(5):
                if(i==3 & j==3 & k==3):
                    print("it's over")
                    tag=False
                    break
                else:
                    print(i,j,k)
sduxh()