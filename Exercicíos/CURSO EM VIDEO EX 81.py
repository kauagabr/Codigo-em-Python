lista = []
cont = 0
while True:
    lista.append(int(input('Digite um valor: ')))
    cont += 1
    continuar = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    if continuar == 'N':
        break
lista.sort(reverse=True)
print(f'Você digitou {cont} números.')
print(f'Os valores em ordem decrescente são {lista}')
print('-='* 30)
if 5 in lista:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi encontrado na lista!')
