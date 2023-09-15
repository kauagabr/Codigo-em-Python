totalp = homem = mulheres = 0
cont = 'S'
while cont == "S":
    print('_'*30)
    print('     CADASTRE UMA PESSOA')
    print('_'*30)
    idade = int(input('Idade: '))
    sexo = str(input('Sexo? [M/F] ')).strip().upper()[0]
    cont = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if idade >= 18:
        totalp += 1
    if sexo == 'M':
        homem += 1
    if sexo == 'F' and idade < 20:
        mulheres += 1
print(f'Total de pessoas com mais de 18 anos: {totalp}')
print(f'Ao todo temos {homem} homens cadastrados.')
print(f'E temos {mulheres} mulheres com menos de 20 anos.')
