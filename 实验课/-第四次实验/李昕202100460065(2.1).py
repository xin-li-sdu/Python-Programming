def queen(state,a): #a为当前行
    m=len(state)
    if a == m:
        print(state)
        return 0
    for k in range(m):
        state[a], flag = k, True
        for row in range(a):
            if (state[row] == k or abs(k - state[row]) == a - row): 
                flag = False
                break
        if flag:
            queen(state, a+1)
n=int(input("请输入皇后的个数："))
queen([None]*n,0)

