def fatorial(n, show=False):
    """
    -> Calcula o fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) mostra ou não a conta.
    :return: O valor do fatorial de um número n.
    Função criada por Kauã Gabriel
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


#programa principal
print('=' * 60)
print(f'{"CALCULO DE FATORIAL":~^60}')
print('=' * 60)
num = int(input('Qual o número que você quer saber o fatorial?'))
print(fatorial(num, show=True))
