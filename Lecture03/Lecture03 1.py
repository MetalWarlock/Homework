from string import digits
i=2
k=0
x=0
a=[]
f=[]
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
while i<=N:
    a.append(i)
    f.append(False)
    i+=1
while x<N//2:
    n=a[x]
    i=x+n
    while i<len(a):
        f[i]=True
        i+=n
    x+=1
    while x<len(f) and f[x]:
        x+=1
i=0
while i<len(a):
    if f[i]:
        i+=1
        continue
    print(a[i],f[i])
    i+=1

