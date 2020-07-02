from bisect import bisect_right
T=int(input())
for i in range(T):
    n=int(input())
    l=list(map(int,input().split()))
    l.sort()
    s=0
    while(len(l)>1):
        new=l[0]+l[1]
        l.remove(l[0])
        l.remove(l[0])
        ind=bisect_right(l,new)
        l.insert(ind,new)
        s+=new
    print(s)