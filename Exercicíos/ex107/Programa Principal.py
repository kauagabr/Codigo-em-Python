import módulos

num = float(input('Digite um valor: R$'))
print('A metade de R${:.1f} é R${:.1f}'.format(num, módulos.metade(num)))
print('O dobro de R${:.1f} é R${:.1f}'.format(num, módulos.dobro(num)))
print('Aumentando 10%, temos R${:.1f}'.format(módulos.aumento(num, 10)))
