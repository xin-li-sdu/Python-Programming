 def step(n):
        if n==1:
            return 1;
        if n==2:
            return 2;
        if n==3:
            return 4;
        sum=step(n-1)+step(n-2)+step(n-3);
        return sum;
    
def way(n,list,i=0):
        if n==1:
            list[i].append(1);
            return;
        if n==2:
            list[i].append(2);
            list[i+1].extend([1,1]);
            return;
        if n==3:
            list[i].append(3);
            list[i+1].extend([1,1,1]);
            list[i+2].extend([1,2]);
            list[i+3].extend([2,1]);
            return;
        for j in range(i,step(n-1)):
            list[j].append(1);
        way(n-1,list,i);
        i=i+step(n-1);
        for j in range(i,i+step(n-2)):
            list[j].append(2);
        way(n-2,list,i);
        i=i+step(n-2);
        for j in range(i,i+step(n-3)):
            list[j].append(3);
        way(n-3,list,i);
def way_achieve(n,list):
        #list=[];
        for j in range(step(n)):
            list.append([]);
        way(n,list); 
k=int(input('请输入台阶数：'))
p=[]
way_achieve(k,p) 
print(p)
