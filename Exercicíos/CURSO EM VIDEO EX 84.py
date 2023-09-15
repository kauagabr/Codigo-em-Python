nome_peso = []
dado = []
peso = []
while True:
    dado.append(str(input('Nome: ')))
    dado.append(float(input('Peso: ')))
    peso.append(dado[1])
    nome_peso.append(dado[:])
    dado.clear()
    cont = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if cont == 'N':
        break

print('-=' * 30)
print(f'Ao todo, Você cadastrou {len(nome_peso)} pessoas.')
print(f'O maior peso foi de {max(peso):.2f}Kg. Peso de ', end='')
for p in nome_peso:
    if p[1] == max(peso):
        print(f'[{p[0]}] ', end='')
print()
print(f'O menor peso foi de {min(peso):.2f}Kg. Peso de ', end='')
for p in nome_peso:
    if p[1] == min(peso):
        print(f'[{p[0]}] ', end='')
print()
