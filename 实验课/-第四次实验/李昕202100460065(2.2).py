#包含yeild
def conflict(state, newx):
    for i, newy in enumerate(state):
        if abs(newx-newy) in (len(state)-i, 0):   # 判断表达式
            return False
    return True
 
def queens(num, state=list()): 
    for m in range(num):
        if conflict(state, m): 
            if len(state) == num-1:
                yield [m] 
            else:
                for k in queens(num,state+[m]):
                    yield [m] + k

def prettyprint(i):
    def line(pos,length=len(i)):
        return  '.'*(pos)+'X'+'.'*(length-pos-1)
    for pos in i:
        print(line(pos))
n=int(input("请输入皇后的个数："))
for i in queens(n):
    print(i)
for i in queens(n):
    prettyprint(i)
    print(' ')
    print('--------------------------')
print(' ')
