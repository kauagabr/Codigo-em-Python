from time import sleep


def maior(*num):
    cont = maior = 0
    print('-=' * 30)
    print('\nAnalisando os valores passados...')
    sleep(2)
    for valor in num:
        print(f'{valor} ', end='', flush=True)
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'\nForam informados {cont} valores ao todo.')
    print(f'O maior valor é informado foi {maior}')


# Program principal
maior(2, 9, 5, 3, 4, 6, 7)
maior(4, 9, 0)
maior(1, 2)
maior(6)
maior()
