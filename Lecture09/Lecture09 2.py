from collections import OrderedDict

def roman(num):
    roman = OrderedDict()
    roman[1000]="M"
    roman[900]="CM"
    roman[500]="D"
    roman[400]="CD"
    roman[100]="C"
    roman[90]="XC"
    roman[50]="L"
    roman[40]="XL"
    roman[10]="X"
    roman[9]="IX"
    roman[5]="V"
    roman[4]="IV"
    roman[1]="I"

    def roman_num(num):
        for r in roman.keys():
            x,y=divmod(num, r)
            yield roman[r]*x
            num-=(r * x)
            if num<=0:
                break

    return "".join([a for a in roman_num(num)])

class Number:
    n=0

    def __init__(self, number):
        self.n = number
        self.bin = bin(self.n)
        self.hex = hex(self.n)
        self.dec = self.n
        self.roman = roman(self.n)

    def __add__(self, other):
        if isinstance(other, Number):
            return Number(self.n + other.n)

n = Number(228)
n = n + Number(69)
print(n.dec)
print(n.bin)
print(n.hex)
print(n.roman)
