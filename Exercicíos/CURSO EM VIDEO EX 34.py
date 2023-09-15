salario = float(input('Qual o salário do fucionário? '))
if salario > 1250:
    novo = (salario * 0.10) + salario
    print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(salario, novo))
else:
    novo = (salario * 15/100) + salario
    print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(salario, novo))
