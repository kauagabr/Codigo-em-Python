num = 0     # ou num = cont = soma = 0
cont = 0
soma = 0
while num != 999:
    num = int(input('Digite um número [999 para parar]: '))
    soma = soma + num
    cont += 1
print('Você digitou {} números e a soma entre eles foi {}.'.format(cont-1, soma-999))
