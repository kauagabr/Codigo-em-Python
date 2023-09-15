d = float(input('Qual é a distancia da sua viagem? '))
if d <= 200:
    s = d * 0.50
    print('Você está preste a começar uma viagem de {}Km'.format(d))
    print('E o preço da sua passagem será de R${:.2f}'.format(s))
else:
    s = d * 0.45
    print('Você está prestes a começar uma viagem de {}Km'.format(d))
    print('E o preço da sua passagem será de R${:.2f}'.format(s))
