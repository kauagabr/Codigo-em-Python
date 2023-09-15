from datetime import date
ano = date.today().year
maiores = 0
menores = 0

for c in range(1, 8):
    num = int(input('Em que ano a {}° pessoa nasceu? '.format(c)))
    idade = ano - num
    if idade >= 21:
        maiores += 1
    else:
        menores += 1
print()
print('Ao total tivemos {} pessoas maiores de idade.'.format(maiores))
print('E também tivemos {} pessoas menores de idade.'.format(menores))

