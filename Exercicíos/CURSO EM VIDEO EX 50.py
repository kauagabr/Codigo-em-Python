s = 0
cont = 0
for c in range(1, 7, 1):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        s = s + n
        cont = cont +1
print('Você informou {} números PARES e a soma foi {}'.format(cont, s))
