def count(n):
    if(n<=1): return 1
    return (count(n-1)+count(n-2))
n=int(input())
print(count(n))