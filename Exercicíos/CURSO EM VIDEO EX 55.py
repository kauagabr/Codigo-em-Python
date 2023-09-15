maior = 0
menor = 0
p1 = 0
p2 = 0
p3 = 0
for c in range(1, 6):
    peso = float(input('Peso da {}ª pessoa: '.format(c)))
    if c == 1:
        maior = peso
        menor = peso
        p1 = c
    if peso > maior:
        maior = peso
        p2 = c
    if peso < menor:
        menor = peso
        p3 = c
    if p1 < p2 and p1 < p3:
        p2 = p1
    if p1 > p2 and p1 > p3:
        p3 = p1
print()
print('O maior peso lido foi da {}ª pessoa com {}Kg'.format(p2, maior))
print('O menor peso lido foi da {}ª pessoa com {}Kg'.format(p3, menor))
