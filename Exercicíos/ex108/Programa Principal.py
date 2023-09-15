import módulos

num = float(input('Digite um valor: R$'))
print('A metade de {} é {}'.format(módulos.moeda(num), (módulos.metade(num, True))))
print('O dobro de {} é {}'.format(módulos.moeda(num), (módulos.dobro(num, True))))
print('Aumentando 10%, temos {}'.format((módulos.aumento(num, 10, True))))
print(f'Reduzindo 13%, temos {módulos.diminuir(num, 13, True)}')

