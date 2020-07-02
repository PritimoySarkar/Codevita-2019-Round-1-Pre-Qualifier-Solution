from bisect import bisect_right
from bisect import bisect_left
n,r=map(int,input().split())
l=list(map(int,input().split()))
l.sort()
for i in range(r):
    low,high=map(int,input().split())
    lb=bisect_right(l,low)
    ub=bisect_left(l,high)
    print(ub-lb,end=" ")