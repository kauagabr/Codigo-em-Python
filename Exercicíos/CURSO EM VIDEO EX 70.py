print('_'*30)
print('     LOJA SUPER BARATÃO')
print('_'*30)
cont = 'S'
total = 0
cont2 = 0
menorp = 0
menorn = ''
pmais1000 = 0
while cont == "S":
    n = str(input('Nome do produto: '))
    p = float(input('Preço: R$ '))
    cont = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    total += p
    if cont2 == 0:
        menorp = p
        menorn = n
    cont2 += 1
    if p < menorp:
        menorp = p
        menorn = n
    if p > 1000:
        pmais1000 += 1

print('---------------FIM DO PROGRAMA---------------')
print('O total de produtos foi {} e vai custa R${:.2f}.'.format(cont2, total))
print(f'Temos {pmais1000} produtos custando mais de R$1000.00.')
print('O produto mais barato foi {} que custa R${:.2f}.'.format(menorn, menorp))


