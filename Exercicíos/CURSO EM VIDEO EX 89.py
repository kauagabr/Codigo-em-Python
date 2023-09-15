from time import sleep
ficha = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) /2
    ficha.append([nome, [nota1, nota2], media])
    rest = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if rest == 'N':
        break
print('-=' * 30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('_' * 26)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
print('_' * 26)
print('ENTRANDO NAS NOTAS...')
while True:
    print("_" * 35)
    sleep(3)
    ops = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if ops == 999:
        print('Finalizando...')
        sleep(3)
        break
    if ops <= len(ficha) - 1:
        print('PROCURANDO NOTAS DO ALUNO...')
        sleep(3)
        print(f'Notas do aluno {ficha[ops][0]} são {ficha[ops][1]}')
print('<<<< VOLTE SEMPRE >>>>')
