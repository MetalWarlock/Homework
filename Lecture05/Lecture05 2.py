print('Введите количество кубиков:')
N=input()
N=int(N)
print('Введите количество сторон этого кубика:')
M=input()
M=int(M)
a=[]
b=[]
s=0
for i in range(N):
    for j in range(1,M):
        a.append(j)
    a.append(M)
print(a)
for k in range(M):
    for l in range(M):
        s=int(a[k])+int(a[l])
        b.append(s)
print(b)
maxs=0
for m in range(len(b)):
    if b[m]>maxs:
        maxs=b[m]
mins=maxs
for n in range(len(b)):
    if b[n]<mins:
        mins=b[n]
for o in range(mins,maxs+1):
    ver=b.count(o)/int(len(b))
    print(o, '=', 100*ver, '%')
