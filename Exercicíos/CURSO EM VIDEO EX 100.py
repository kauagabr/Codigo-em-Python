from random import sample
from time import sleep


def sorteia(lista):
    print('Sorteando 5 valor da lista: ', end='')
    n = sample(range(1, 21), 5)
    for valor in n:
        print(f'{valor} ', end='', flush=True)
        sleep(0.4)
    print('PRONTO!')
    lista.append(n)


def somapar():
    cont = 1
    soma = 0
    lista = []
    while cont <= 5:
        num = int(input(f'Digite o {cont}º número a cima: '))
        if num % 2 == 0:
            soma = soma + num
            lista.append(num)
        cont += 1
    print(f'A soma dos valores pares {lista} a cima é {soma}')


# Program principal
numeros = list()
sorteia(numeros)
somapar()
