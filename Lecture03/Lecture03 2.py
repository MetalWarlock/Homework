from string import digits
i=0
j=0
a=[]
b=[]
print ('Введите первое целое число.')
N=input()
a=list(N)
while i<len(a):
    if a[i] not in digits:
        print('Вы должны ввести целое число.')
        exit()
    i+=1
N=int(N)
print ('Введите второе целое число.')
M=input()
b=list(M)
while j<len(b):
    if b[j] not in digits:
        print('Вы должны ввести целое число.')
        exit()
    j+=1
M=int(M)
if N==0 and M==0:
    print('Хотя бы одно из чисел не должно быть равно нулю')
    exit()
while M != 0 and N != 0:
    if M > N:
        M = M % N
    else:
        N = N % M
 
print(M + N)
