cadastro = dict()
cadastro['Nome'] = str(input("Digite seu nome: ")).strip().title()
cadastro['Media'] = float(input(f'Média do {cadastro["Nome"]}: '))
print('-=' * 30)
if cadastro["Media"] >= 7:
    cadastro["Situação"] = 'Aprovado'
elif 5 <= cadastro["Media"] < 7:
    cadastro["Situação"] = 'Recuperação'
else:
    cadastro["Situação"] = 'Reprovado'
for k, v in cadastro.items():
    print(f'< {k} é igual a {v} >')
