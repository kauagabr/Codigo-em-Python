time = ('Atlético-MG', 'Palmeiras', 'Fortaleza', 'Flamengo', 'Bragantino', 'Atlético-PR', 'Atlético-GO', 'Ceará SC',
        'Corinthians', 'Internacional', 'Santos', 'Juventude', 'Cuiabá', 'Bahia', 'São Paulo', 'Fluminence', 'Grêmio',
        'Sport Recife', 'América-MG', 'Chapecoence')
print('-='*15)
print(f'Lista de times do brasileirão:{time}')
print('-='*15)
print(f'Os 5 primeiros são: {time[0:5]}')
print('-='*15)
print(f'Os 4 último são: {time[-4:]}')
print('-='*15)
print(f'Times em ordem alfabética: {sorted(time)}')
print('-='*15)
print(f'O Chapecoense está na {time.index("Chapecoence")+1}ª posição')
