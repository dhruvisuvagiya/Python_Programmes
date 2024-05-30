class prime:
    cnt=0
    n=int(input('n = '))
    for i in range(1,n+1,1):
        if n%i==0:
            cnt+=1

    # if cnt==2:
    #     print("Prime")
    # else:
    #     print('Not Prime')
            
p=prime()
if p.cnt==2:
        print("Prime")
else:
        print('Not Prime')


