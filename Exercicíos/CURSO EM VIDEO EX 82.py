lista = []
listapa = []
listaim = []
while True:
    n = int(input('Digite um número: '))
    lista.append(n)
    if n % 2 == 0:
        listapa.append(n)
    else:
        listaim.append(n)
    cont = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    if cont == 'N':
        break
lista.sort()
listapa.sort()
lista.sort()
print('-='*30)
print(f'A lista completa é {lista}')
print(f'A lista de pares é {listapa}')
print(f'A lista de ímpares é {listaim}')
