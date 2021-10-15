import random
N=float(input())
a=[]
f=1
for x in range(int(N)):
    a.append(random.randint(0,100))
print(a)
while f>0:
    for i in range(int(N)-1):
        if a[i+1]<a[i]:
            a[i],a[i+1]=a[i+1],a[i]
            f+=1
    if f-1:
        f=1
    else:
        print(a)
        exit()
