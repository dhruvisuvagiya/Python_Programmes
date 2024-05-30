list=[]
n=int(input('n = '))
for i in range(0,n,1):
    m=int(input())
    list.append(m)
print(list)

for i in range(0,n,1):
    for j in range(0,n,1):
            if list[i]<list[j]:
                x=list[i]
                list[i]=list[j]
                list[j]=x
print('Ascending List = ',list)