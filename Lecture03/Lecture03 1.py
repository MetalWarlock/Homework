from string import digits
i=0
k=0
b=[]
c=[]
print ('Введите целое число большее 2:')
N=input()
c=list(N)
while k<len(c):
    if c[k] not in digits:
        print('Вы должны ввести целое число.')
        exit()
    k+=1
N=int(N)
if N<=2:
    print('Вы должны ввести число большее двух.')
    exit()
a=list(range(N))
del a[0]
del a[0]
a.append(N)
while i<len(a):
    j=2
    while j<=a[i]:
        if a[i]%j==0:
            b.append(j)
        j+=1
    if len(b)==1:
        print(a[i])
    i+=1
    b=[]

