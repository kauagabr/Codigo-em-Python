print('-=-'*20)
print('Analizandor de triângulos')
print('-=-'*20)
n1 = float(input('Primeiro segmento: '))
n2 = float(input('Segundo segmento: '))
n3 = float(input('Terceiro segmento: '))
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('Os segmento acima PODE FORMA triângulo!')
else:
    print('Os segmento acima NÃO PODE FORMA triângulo!')
