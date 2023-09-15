import módulos

num = float(input('Digite um valor: R$'))
print(f'A metade de {módulos.moeda(num)} é {módulos.metade(num, True)}')
print(f'O dobro de {módulos.moeda(num)} é {módulos.dobro(num, True)}')
print(f'Aumentando 10%, temos {módulos.aumento(num, 10, True)}')
print(f'Reduzindo 13%, temos {módulos.diminuir(num, 13, True)}')

