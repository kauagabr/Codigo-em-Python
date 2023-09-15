from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
cont = 0
while cont == 0:
    print('    [ 1 ] Somar')
    print('    [ 2 ] Multiplicar')
    print('    [ 3 ] Maior')
    print('    [ 4 ] Novos números')
    print('    [ 5 ] Sair do programa')
    opcao = int(input('>>>>> Qual é sua opção? '))
    if opcao == 1:
        s = n1 + n2
        print('A soma entre {} + {} = {}'.format(n1, n2, s))
    elif opcao == 2:
        m = n1 * n2
        print('O resultado de {} x {} = {}'.format(n1, n2, m))
    elif opcao == 3:
        if n1 > n2:
            print('Entre {} e {} o maior valor é {}'.format(n1, n2, n1))
        elif n2 > n1:
            print('Entre {} e {} o maior valor é {}'.format(n1, n2, n2))
    elif opcao == 4:
        print('Informe os números novamente: ')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print('Finalizando...')
        sleep(3)
        cont = 1
    else:
        print('Opcão inválida. Tente novamente!')
    print("=-=" * 10)
print('Fim do programa! volte sempre!')
