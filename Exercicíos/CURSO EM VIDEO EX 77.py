palavras = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON',
            'CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR', 'TRABALHAR',
            'MERCADO', 'PROGRAMADOR', 'FUTURO')
for pal in palavras:
    print(f'\nNa palavra {pal} temos ', end='')
    for letra in pal:
        if letra.lower() in 'aeiou':
            print(letra.lower(), end=' ')

