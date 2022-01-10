import defStraight
import defIndirect
error=int(input('Выберите тип погрешности: 1 - прямая, 2 - косвенная.'))
if error==1:
    defStraight.straight()
if error==2:
    defIndirect.indirect()
