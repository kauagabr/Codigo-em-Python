"""co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = (co ** 2 + ca ** 2) ** 0.5 #ou (1/2)
print('A hipotenusa vai medir {:.2f}'.format(hi))"""

import math #ou from math import hypot por que só está usando uma import
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = math.hypot(co, ca) #ou hi = hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))
