list=[];sum=0;cnt=0
n=int(input('n = '))
for i in range(0,n,1):
    m=int(input())
    if m%2==0:
        cnt+=1
        if cnt!=0:
            sum+=m
print('Sum = ',sum)

