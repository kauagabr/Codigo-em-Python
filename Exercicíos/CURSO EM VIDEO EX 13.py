sa = float(input('Qual é o salário do Funcionário? R$'))
#salario = (sa*15/100)+sa
print('Um funcionário que ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}'.format(sa, (sa*0.15)+sa))
