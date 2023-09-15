soma = 0
maisvelho = 0
nome_velho = ""
cont = 0
for c in range(1, 5):
    print('---------{}ª PESSOA---------'.format(c))
    nome = str(input('NOME: '))
    idade = int(input('IDADE: '))
    sexo = str(input('SEXO [M/F]: ')).strip().upper()
    soma = soma + idade
    if sexo == "M" and idade > maisvelho:
        maisvelho = idade
        nome_velho = nome
    if idade < 20 and sexo == "F":
        cont += 1
print()
print('A média de idade do grupo é de {} anos.'.format(soma/4))
print('O homem mais velho tem {} anos e se chama {}.'.format(maisvelho, nome_velho))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(cont))
