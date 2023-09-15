def voto(ano):
    """
    -> Faz a avaliação da idade do usuário para saber se o voto é
    obrigatorio, opcional ou não precisa votar.
    :param ano: Vai receber o ano de nascimento do usuário.
    :return: Vai retornar a resposta.
    Função criada por Kauã Gabriel
    """
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA.'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL.'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.'


#Programa principal
print('=-' * 30)
print(f'{"AVALIAMENTO DE IDADE PARA O VOTO":-^60}')
print('=-' * 30)
nasc = int(input('Em que ano você nasceu? '))
print(voto(nasc))
#help(voto)
