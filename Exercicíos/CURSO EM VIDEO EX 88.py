"""from random import randint
from time import sleep
lista = []
jogos = []
print('-' * 30)
print('      JOGA NA MEGA SENA      ')
print('-' * 30)
quant = int(input('Quantos jogos você quer que eu sorteie? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont == 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-=' * 3, f' SORTEANDO {quant} JOGOS ', '-=' * 3)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(2)"""

from random import sample
q = int(input('Quantas apostas você quer gerar? '))
nums = [sample(range(1, 61), k=6) for x in range(0, q)]
for i in range(0, q):
    print(f'Aposta {i+1}: {sorted(nums)[i]}')

