import math
from sympy import diff, symbols, cos, sin

def indirect():
        indirect=input('Введите формулу значения, для которого рассчитывается косвенная погрешность:')
        num=int(input('Введите кол-во прямых измерений:'))
        x=[0]*num
        summ=0
        for i in range(num):
                x[i]=str(input('Введите название переменной:'))
        for j in range(len(x)):
                a = symbols(str(x[j]))
                b = diff(indirect,a)
                c = ((b*float(input('Введите значение прямой погрешности:')))**2)
                summ+=c
        for k in range(len(x)):
                d=x[k]
                e = input('Введите значение переменной:')
                summ = str(summ)
                summ = summ.replace(str(d),str(e))

        answer = math.sqrt(eval(summ))
        print(answer)

