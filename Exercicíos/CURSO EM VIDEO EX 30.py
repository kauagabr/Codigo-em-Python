n = int(input('\033[35mMe diga um número qualquer:\033[m'))
s = n % 2
if s == 0:
    print('O número \033[1;32m{}\033[m é \033[36mPAR\033[m'.format(n))
else:
    print('O número \033[1;32m{}\033[m é \033[36mÍMPAR\033[m'.format(n))
