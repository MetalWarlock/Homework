from string import digits
first=''
second=''
zero='Ноль'
one='один'
two='два'
three='три'
four='четыре'
five='пять'
six='шесть'
seven='семь'
eight='восемь'
nine='девять'
ten='Десять'
eleven='Одиннадцать'
twelve='Двеннадцать'
thirteen='Тринадцать'
fourteen='Четырнадцать'
fivteen='Пятнадцать'
sixteen='Шестнадцать'
seventeen='Семнадцать'
eighteen='Восемнадцать'
nineteen='Девятнадцать'
twenty='Двадцать '
thirty='Тридцать '
fourty='Сорок '
fifty='Пятьдесят '
sixty='Шестьдесят '
seventy='Семьдесят '
eighty='Восемьдесят '
ninty='Девяностно '
print('Введите число от 0 до 99:')
a=input()
if (len(a)==1 and a[0] in digits) or (len(a)==2 and\
                                      a[0] in digits\
                                      and a[1] in digits):
        a=int(a)
        if a>=0 and a<=99:
            if a==0:
                print(zero)
                exit()
            if a%10>=0:
                if a%10==0:
                    second==zero
                elif a%10==1:
                    second=one
                elif a%10==2:
                    second=two
                elif a%10==3:
                    second=three
                elif a%10==4:
                    second=four
                elif a%10==5:
                    second=five
                elif a%10==6:
                    second=six
                elif a%10==7:
                    second=seven
                elif a%10==8:
                    second=eight
                elif a%10==9:
                    second=nine
            if a//10>=0:
                if a//10==1:
                        if a%10==0:
                            print(ten)
                            exit()
                        if a%10==1:
                            print(eleven)
                            exit()
                        if a%10==2:
                            print(twelve)
                            exit()
                        if a%10==3:
                            print(thirteen)
                            exit()
                        if a%10==4:
                            print(fourteen)
                            exit()
                        if a%10==5:
                            print(fivteen)
                            exit()
                        if a%10==6:
                            print(sixteen)
                            exit()
                        if a%10==7:
                            print(seventeen)
                            exit()
                        if a%10==8:
                            print(eighteen)
                            exit()
                        if a%10==9:
                            print(nineteen)
                            exit()
                elif a//10==2:
                        first=twenty
                elif a//10==3:
                        first=thirty
                elif a//10==4:
                        first=fourty
                elif a//10==5:
                        first=fifty
                elif a//10==6:
                        first=sixty
                elif a//10==7:
                        first=seventy
                elif a//10==8:
                        first=eighty
                elif a//10==9:
                        first=ninty        
        else:
            print('Вы должны ввести число от 0 до 99')
            exit()
        if second==zero:
            print(first)
        else:
            print(first+second)
else:
        print('Неправильный ввод \n'
          'Вы должны ввести число от 0 до 99 ')
