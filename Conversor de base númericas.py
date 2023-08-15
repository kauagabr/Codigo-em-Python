print(f'{"CONVERSOR DE BASES NÚMERICAS":-^60}')
cont = 0
while cont == 0:
    print('DECIMAL > BINÁRIO = 1')
    print('DECIMAL > OCTAL = 2')
    print('DECIMAL > HEXADECIMAL = 3')
    print('BINÁRIO > DECIMAL = 4')
    print('OCTAL > DECIMAL = 5')
    print('HEXADECIMAL > DECIMAL = 6')
    print('Se deseja sair = 7')
    conv = int(input('Qual conversão você deseja fazer?'))
    if conv == 1:
        num = int(input('Qual é o número DECIMAL você quer converter para BINÁRIO?'))
        n2 = format(num, "b")
        print('NÚMERO BINÁRIO-> {}'.format(n2))
    elif conv == 2:
        num = int(input('Qual é o número DECIMAL você quer converter para OCTAL?'))
        n8 = format(num, "o")
        print('NÚMERO OCTAL-> {}'.format(n8))
    elif conv == 3:
        num = int(input('Qual é o número DECIMAL você quer converter para HEXADECIMAL?'))
        n16 = format(num, "x")
        print('NÚMERO HEXADECIMAL-> {}'.format(n16))
    elif conv == 4:
        num = (input('Qual é o número BINÁRIO você quer converter para DECIMAL?'))
        n2 = int(num, 2)
        print('NÚMERO DECIMAL-> {}'.format(n2))
    elif conv == 5:
        num = (input('Qual é o número OCTAL você quer converter para DECIMAL?'))
        n8 = int(num, 8)
        print('NÚMERO DECIMAL-> {}'.format(n8))
    elif conv == 6:
        num = (input('Qual é o número HEXADECIMAL você quer converter para DECIMAL?'))
        n16 = int(num, 16)
        print('NÚMERO HEXADECIMAL-> {}'.format(n16))
    elif conv == 7:
        print(f'{"OBRIGADO":-^60}')
        cont = 1
    else:  
        print('OPÇÃO NEGADA!!!')
        print('Tente novamente!')
    
