import math
n,k=map(int,input().split(','))
f=[]
f.append(1)
f.append(n)
for i in range(2,int(math.sqrt(n))+1):
    if(n%i==0):
        f.append(i)
        f.append(n//i)
if((math.sqrt(n))-(int(math.sqrt(n)))==0): f.remove(int(math.sqrt(n)))
f.sort()
if(k>len(f)): print(-1)
else: print(f[-k])