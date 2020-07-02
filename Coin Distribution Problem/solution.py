n=int(input())
d=[]
d.append(0)
d.append(0)
d.append(0)
if(n>5):
    d[1]=2
    d[2]=1
    n-=5
    d[0]+=n//5
    if(n%5!=0):
        n=n%5
        d[1]+=n//2
        if(n%2!=0):
            n=n%2
            d[2]+=1
else:
    d[1]+=n//2
    if(n%2!=0): n=n%2
    d[2]+=1
print(d[0]+d[1]+d[2],end=" ")
for i in d: print(i,end=" ")