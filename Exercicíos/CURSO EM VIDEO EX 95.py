from time import sleep
time = list()
jogador = dict()
partidas = list()
while True:
    jogador.clear()
    jogador["nome"] = str(input('Nome do jogador: ')).strip().title()
    tot = int(input(f'Quantas partidas {"nome"} jogou? '))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f'    Quantos gols na partida {c+1}? ')))
    jogador["gols"] = partidas[:]
    jogador["total"] = sum(partidas)
    time.append(jogador.copy())
    while True:
        rest = str(input('Quer continuar? [S/N]')).upper().strip()[0]
        if rest in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if rest == 'N':
        break
print('-=' * 30)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 40)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 40)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com código {busca}')
    else:
        print(f' -- PROCURANDO LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}:')
        sleep(3)
        for i, g in enumerate(time[busca]['gols']):
            print(f'    No jogo {i+1} fez {g} gols')
            sleep(2)
    print('-' * 40)
print('FINALIZANDO O PROGRAMA...')
sleep(3)
print('<< VOLTE SEMPRE >>')
