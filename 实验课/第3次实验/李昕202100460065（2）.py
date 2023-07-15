def step(n):
        if n==1:
            return 1;
        if n==2:
            return 2;
        if n==3:
            return 4;
        sum=step(n-1)+step(n-2)+step(n-3);
        return sum; 
n=int(input('请输入台阶数：'))
print(step(n))
