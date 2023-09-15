import random
n1 = str(input('primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
lista = [n1, n2, n3, n4] #para fazer uma lista você coloca ela em cochetes
escolhido = random.choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))

