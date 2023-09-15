frase = str.upper(input('Digite um frase: ')).strip()
print('A letra A aparece {} vezes na frase.'.format(frase.count("A")))
print('A primeira letra A aparaceu na posição {}'.format(frase.find("A")+1))
print('A última letra A apareceu na posição {}'.format(frase.rfind("A")+1))



