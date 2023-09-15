x = "S"
y = 0
s = 0
cont = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
        'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
        'doze', 'treze', 'catorze', 'quinze', 'dezesseis',
        'dezessete', 'dezoito', 'dezenove', 'vinte')
while x == 'S':
    num = int(input('Digite um número entre 0 e 20:'))
    if 0 <= num <= 20:
        print(f'Você digitou o número {cont[num]}')
    x = str(input('Você quer continuar? [S/N]')).strip().upper()[0]
    y += 1
    s = s + num
print(f'Você usou o programa {y} e a soma de todos os valores é {s}')
