num = int(input('Digite um número: '))
total = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[1;4;33m', end='')
        total += 1
    else:
        print('\033[1;4;31m', end='')
    print('\033[1;4m{}\033[m '.format(c), end='')
print('\n\033[4;33mO número {} foi divisível {} vezes.\033[m '.format(num, total))
if total == 2:
    print('\033[4;33mE por isso ele é PRIMO!\033[m')
else:
    print('\033[4;33mE por isso ele não é PRIMO!\033[m')
