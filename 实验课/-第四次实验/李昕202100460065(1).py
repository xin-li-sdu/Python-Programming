class Pillar:
	def __init__(self,str,num):
		self.key=str
		self.value=num

def Hanoi(num,a,b,c):
    if num==1:
        a.value-=1
        c.value+=1
        print(a.key,"->",c.key)
        print("盘子个数 A:{},B:{},C:{}".format(a.value,b.value,c.value))
    else:
    	Hanoi(num-1,a,c,b)
    	Hanoi(1,a,b,c)
    	Hanoi(num-1,b,a,c)	
def main():
    num=eval(input("A上的盘子有："))
    a=Pillar('A',num)
    b=Pillar('B',0)
    c=Pillar('C',0)
    Hanoi(num,a,b,c)
main()
