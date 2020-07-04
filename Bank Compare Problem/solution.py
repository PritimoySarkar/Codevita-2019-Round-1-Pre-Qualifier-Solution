p=int(input())
t=int(input())
na=int(input())
suma=0
for i in range(na):
    s,r=map(float,input().split())
    r=r/12 #If given interest rate is in yearly basis (However it won't change the final output of this code) otherwise remove this line
    emi=p*r/(1-(1/((r+1)**(s*12))))
    suma+=(s*12*emi)
nb=int(input())
sumb=0
for i in range(nb):
    s,r=map(float,input().split())
    r=r/12 #If given interest rate is in yearly basis (However it won't change the final output of this code) otherwise remove this line
    emi=p*r/(1-(1/((r+1)**(s*12))))
    sumb+=(s*12*emi)
if(suma<sumb): print('Bank A')
else: print('Bank B')