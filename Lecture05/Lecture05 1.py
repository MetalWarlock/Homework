a=open('task1.txt')
a=a.readlines()
a=list(map(lambda b: str(b)[:-1], a))
a=[int(b) for b in a]
res=[]
for b in a:
    for c in a:
        for d in a:
            if (b+c+d)==2020:
                res.append(b*c*d)
res = list(set(res))
with open('output1.txt', 'w') as file:
    for b in res:
        file.write(str(b))
        file.write('\n')
file.close()
