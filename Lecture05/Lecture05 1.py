file=open('task1.txt')
a=file.readlines()
answer=open('output1.txt','w')
b=0
for i in range(len(a)):
    if b+int(a[i])<2020:
        b+=int(a[i])
        for j in range(i+1,len(a)):
            if b+int(a[j])<2020:
                b+=int(a[j])
                for k in range(j+1,len(a)):
                    if b+int(a[k])==2020:
                        answer.writelines(int(a[i])*int(a[j])*int(a[k]))
                        b=0
