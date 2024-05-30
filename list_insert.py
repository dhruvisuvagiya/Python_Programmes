a=[]
b=[]
c=[]

n1=int(input('Enter length of list = '))
n2=int(input('Enter length of list1 = '))

for i in range(0,n1,1):
    m=int(input('Enter list = '))
    a.append(m)

for i in range(0,n2,1):
    n=int(input('Enter list1 = '))
    b.append(n)
    
for i in range(0,n1,1):
    b[i]=a[i]
    
for i in range(0,n2,1):
    j=i
    c[j]=b[i]
    j+=1
    
for i in range(0,n1+n2,1):
    print('Mergerd List = ',c[i])

