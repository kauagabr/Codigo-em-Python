n = str(input('Informe seu sexo [M/F] ')).upper().strip()[0]
while n not in 'MF':
    n = str(input('Dados inválidos. Por favor, informe seu sexo: ')).upper().strip()[0]
print('Sexo {} registrado com sucesso.'.format(n))
