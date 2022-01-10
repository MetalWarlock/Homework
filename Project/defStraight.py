import math
def straight():
    typeoferror=int(input('Выберите: 1 - только сист. погрешность, 2 - только сл. погрешность, 3 - полная погрешнсть:'))

    if typeoferror==1:
              alpha=float(input('Введите доверительный интервал:'))
              cd=float(input('Введите цену деления:'))
              a=alpha*cd/2
              print(a)
              
    if typeoferror==2:
              sr=0
              summ=0
              student=float(input('Введите коэф. Стьюдента:'))
              num=int(input('Введите кол-во измерений:'))
              x=[0]*num
              for i in range(num):
                  x[i]=float(input('Измерение ' + str(i+1) + ':'))
              for j in range(len(x)):
                  sr+=x[j]
              srz=sr/num
              for k in range(len(x)):
                    summ+=((x[k]-srz)**2)
              b=student*(math.sqrt(summ*((num*(num-1))**-1)))
              print(b)
    if typeoferror==3:
              alpha=float(input('Введите доверительный интервал:'))
              cd=float(input('Введите цену деления:'))
              a=alpha*cd/2
              
              sr=0
              summ=0
              student=float(input('Введите коэф. Стьюдента:'))
              num=int(input('Введите кол-во измерений:'))
              x=[0]*num
              for i in range(num):
                  x[i]=float(input('Измерение ' + str(i+1) + ':'))
              for j in range(len(x)):
                  sr+=x[j]
              srz=sr/num
              for k in range(len(x)):
                    summ+=((x[k]-srz)**2)
              b=student*(math.sqrt(summ*((num*(num-1))**-1)))
              c=math.sqrt(b**2+a**2)
              print(c)
