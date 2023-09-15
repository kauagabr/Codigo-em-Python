numlista = []
mai = 0
men = 0
for c in range(0, 5):
    numlista.append(int(input(f'Digite um valor para a posição {c}: ')))
    if c == 0:
        mai = men = numlista[c]
    else:
        if numlista[c] > mai:
            mai = numlista[c]
        if numlista[c] < men:
            men = numlista[c]
print('-='*30)
print(f'Você digitou os valores {numlista}')
print(f'O maior valor digitado foi {mai} nas posições ', end='')
for i, v in enumerate(numlista):
    if v == mai:
        print(f'{i}...', end='')
print()
print(f'O menor valor digitado foi {men} nas posições ', end='')
for i, v in enumerate(numlista):
    if v == men:
        print(f'{i}...', end='')
print()
