def area():
    print(f'{"CONTROLE DE TERRENO":-^30}')
    print('-'*30)
    a = float(input('LARGURA (m): '))
    b = float(input('COMPRIMENTO (m): '))
    calculo = a * b
    print('A área do terreno {:.1f}x{:.1f} é de {:.1f}m².'.format(a, b, calculo))


area()

