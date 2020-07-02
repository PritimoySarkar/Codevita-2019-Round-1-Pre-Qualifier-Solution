import math
def sqf(n):
    bkp=n
    prime=[2,3,5,7,11,13,17,19]
    for j in prime:
        if(n%j==0): n=n//j
        if(n%j==0): return False
        n=bkp
    return True  
n=int(input())
l=[]
l.append(n)
for i in range(2,int(math.sqrt(n))+1):
    if((n%i)==0): 
        l.append(i)
        l.append(n//i)
l.sort()
count=0
print("Factors: ",l)
for i in l:
    if(sqf(i)): count+=1
print(count)