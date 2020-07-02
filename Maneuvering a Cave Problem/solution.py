T=int(input())
for i in range(T):
    n,m=map(int,input().split())
    a=[]
    a.append([1]*n)
    for j in range(m):
        a.append([1])
    for x in range(1,m):
        for y in range(1,n):
            a[x].append(a[x-1][y]+a[x][y-1])
    print(a[m-1][n-1])