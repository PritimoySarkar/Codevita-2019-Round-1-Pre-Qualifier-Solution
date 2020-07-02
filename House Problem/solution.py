l=list(map(int,input().split()))
se=0
so=0
for i in range(0,len(l),2):
    so+=l[i]
for i in range(1,len(l),2):
    se+=l[i]
print(max(so,se))