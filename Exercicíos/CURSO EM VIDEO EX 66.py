cont = s = n = 0
while True:
    n = int(input('Digite um número (Digite 999 para parar):'))
    if n == 999:
        break
    cont += 1
    s += n
print(f'A soma dos {cont} números foi {s}!')
