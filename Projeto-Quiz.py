from time import sleep

green = "\033[1;42m"
red = "\033[1;41m"
ciano = "\033[1;46m"
amarelo = "\033[1;43m"
cinza = "\033[1;47m"
final = "\033[m"

contador = 1
resp_corretas = []


def linigl(cont):
    print('=' * cont)


def traço(cont):
    print("-" * cont)


def acerto(lista):
    porce = 10 * len(lista)
    if porce >= 80:
        print(f'{green}Parabéns, seu desempenho foi excelente!, com {porce}% das respostas certas{final}')
    elif 60 <= porce < 80:
        print(f'{amarelo}Parabéns, seu desempenho foi bom!, com {porce}% das respostas certas{final}')
    elif porce < 60:
        print(f'{red}Atenção, você precisa estudar mais sobre esse tema!, voce acertou apenas  {porce}% das respostas.{final}')

print()
linigl(60)
print(f'{ciano}{"CENTRAL DO QUIZ":-^60}{final}')
linigl(60)
print()

while contador == 1:
    print("1º - São tipos de Hardware, exceto: ")
    print('A) Memória RAM\n'
          'B) SSD\n'
          'C) Free Fire\n'
          'D) SATA\n'
          'E) Placa Mãe')
    resp1 = str(input("Informe uma opção: ")).strip().upper()
    print(f"{cinza}AVALIANDO SUA RESPOSTA...{final}")
    sleep(3)
    print()

    if resp1 == "A" or resp1 == "B" or resp1 == "C" or resp1 == "D" or resp1 == "E":
        if resp1 == "C":
            resp_corretas.append(resp1)
            print(f"{green}RESPOSTA CORRETA!{final}")
        else:
            print(f"{red}RESPOSTA ERRADA!{final}")
        contador = 2
    else:
        print(f"{amarelo}NÃO TEM ESSA OPÇÃO! TENTE NOVAMENTE!{final}")
        print()

traço(60)

while contador == 2:
    print("2º - Qual a alternativa que apresenta a maior medida em Bytes? ")
    print('A) GB\n'
          'B) KB\n'
          'C) MB\n'
          'D) TB\n'
          'E) PB')
    resp2 = str(input("Informe uma opção: ")).strip().upper()
    print(f"{cinza}AVALIANDO SUA RESPOSTA...{final}")
    sleep(3)
    print()
    if resp2 == "A" or resp2 == "B" or resp2 == "C" or resp2 == "D" or resp2 == "E":
        if resp2 == "E":
            resp_corretas.append(resp2)
            print(f"{green}RESPOSTA CORRETA!{final}")
        else:
            print(f"{red}RESPOSTA ERRADA!{final}")
        contador = 3
    else:
        print(f"{amarelo}NÃO TEM ESSA OPÇÃO! TENTE NOVAMENTE!{final}")
        print()

traço(60)

while contador == 3:
    print("3º - O que é Windows da Microsoft?")
    print('A) É um sistema operacional\n'
          'B) É um Driver\n'
          'C) É um navegador de internet\n'
          'D) É um vírus\n'
          'E) Nenhuma das opções')
    resp3 = str(input("Informe uma opção: ")).strip().upper()
    print(f"{cinza}AVALIANDO SUA RESPOSTA...{final}")
    sleep(3)
    print()
    if resp3 == "A" or resp3 == "B" or resp3 == "C" or resp3 == "D" or resp3 == "E":
        if resp3 == "A":
            resp_corretas.append(resp3)
            print(f"{green}RESPOSTA CORRETA!{final}")
        else:
            print(f"{red}RESPOSTA ERRADA!{final}")
        contador = 4
    else:
        print(f"{amarelo}NÃO TEM ESSA OPÇÃO! TENTE NOVAMENTE!{final}")
        print()

traço(60)

while contador == 4:
    print("4º - Na ordem cronológica, marque a alternativa correta.")
    print('A) Ábaco, Eniac, Chip, Transistor e Microprocessador.\n'
          'B) Eniac, Ábaco, Chip, Transistor e Microprocessador.\n'
          'C) Ábaco, Eniac, Chip, Microprocessador e Transistor.\n'
          'D) Ábaco, Eniac, Transistor, Chip e Microprocessador.\n'
          'E) Transistor, Eniac, Ábaco, Chip e Microprocessador.')
    resp4 = str(input("Informe uma opção: ")).strip().upper()
    print(f"{cinza}AVALIANDO SUA RESPOSTA...{final}")
    sleep(3)
    print()
    if resp4 == "A" or resp4 == "B" or resp4 == "C" or resp4 == "D" or resp4 == "E":
        if resp4 == "D":
            resp_corretas.append(resp4)
            print(f"{green}RESPOSTA CORRETA!{final}")
        else:
            print(f"{red}RESPOSTA ERRADA!{final}")
        contador = 5
    else:
        print(f"{amarelo}NÃO TEM ESSA OPÇÃO! TENTE NOVAMENTE!{final}")
        print()

traço(60)

while contador == 5:
    print("5º - Qual componente não faz parte do pacote Office?")
    print('A) Excel\n'
          'B) Blender\n'
          'C) Access\n'
          'D) Powerpoint\n'
          'E) Word')
    resp5 = str(input("Informe uma opção: ")).strip().upper()
    print(f"{cinza}AVALIANDO SUA RESPOSTA...{final}")
    sleep(3)
    print()
    if resp5 == "A" or resp5 == "B" or resp5 == "C" or resp5 == "D" or resp5 == "E":
        if resp5 == "B":
            resp_corretas.append(resp5)
            print(f"{green}RESPOSTA CORRETA!{final}")
        else:
            print(f"{red}RESPOSTA ERRADA!{final}")
        contador = 6
    else:
        print(f"{amarelo}NÃO TEM ESSA OPÇÃO! TENTE NOVAMENTE!{final}")
        print()

traço(60)

while contador == 6:
    print("6º - O que é o Youtube?")
    print('A) É um site de apenas filmes famosos\n'
          'B) É um site de propagandas\n'
          'C) É exclusivo apenas para editores de vídeos\n'
          'D) É um site de vídeos diversos\n'
          'E) É um site infantil')
    resp6 = str(input("Informe uma opção: ")).strip().upper()
    print(f"{cinza}AVALIANDO SUA RESPOSTA...{final}")
    sleep(3)
    print()
    if resp6 == "A" or resp6 == "B" or resp6 == "C" or resp6 == "D" or resp6 == "E":
        if resp6 == "D":
            resp_corretas.append(resp6)
            print(f"{green}RESPOSTA CORRETA!{final}")
        else:
            print(f"{red}RESPOSTA ERRADA!{final}")
        contador = 7
    else:
        print(f"{amarelo}NÃO TEM ESSA OPÇÃO! TENTE NOVAMENTE!{final}")
        print()

traço(60)

while contador == 7:
    print("7º - Qual dos periféricos abaixo é um periférico de entrada de dados?")
    print('A) Datashow.\n'
          'B) Impressora.\n'
          'C) Teclado.\n'
          'D) Caixas de Som.\n'
          'E) Gabinete.')
    resp7 = str(input("Informe uma opção: ")).strip().upper()
    print(f"{cinza}AVALIANDO SUA RESPOSTA...{final}")
    sleep(3)
    print()
    if resp7 == "A" or resp7 == "B" or resp7 == "C" or resp7 == "D" or resp7 == "E":
        if resp7 == "C":
            resp_corretas.append(resp7)
            print(f"{green}RESPOSTA CORRETA!{final}")
        else:
            print(f"{red}RESPOSTA ERRADA!{final}")
        contador = 8
    else:
        print(f"{amarelo}NÃO TEM ESSA OPÇÃO! TENTE NOVAMENTE!{final}")
        print()

traço(60)

while contador == 8:
    print("8º - Qual palavra é mais apropriada para definir a evolução da informatização?")
    print('A) Inclusão Digital.\n'
          'B) Mobilidade.\n'
          'C) Internet.\n'
          'D) Computação.\n'
          'E) Tablets.')
    resp8 = str(input("Informe uma opção: ")).strip().upper()
    print(f"{cinza}AVALIANDO SUA RESPOSTA...{final}")
    sleep(3)
    print()
    if resp8 == "A" or resp8 == "B" or resp8 == "C" or resp8 == "D" or resp8 == "E":
        if resp8 == "A":
            resp_corretas.append(resp8)
            print(f"{green}RESPOSTA CORRETA!{final}")
        else:
            print(f"{red}RESPOSTA ERRADA!{final}")
        contador = 9
    else:
        print(f"{amarelo}NÃO TEM ESSA OPÇÃO! TENTE NOVAMENTE!{final}")
        print()

traço(60)

while contador == 9:
    print("9º - São sistemas operacionais, EXCETO:")
    print('A) Windows 7\n'
          'B) Mozilla Firefox\n'
          'C) Ubuntu\n'
          'D) Windows 8\n'
          'E) Android')
    resp9 = str(input("Informe uma opção: ")).strip().upper()
    print(f"{cinza}AVALIANDO SUA RESPOSTA...{final}")
    sleep(3)
    print()
    if resp9 == "A" or resp9 == "B" or resp9 == "C" or resp9 == "D" or resp9 == "E":
        if resp9 == "B":
            resp_corretas.append(resp9)
            print(f"{green}RESPOSTA CORRETA!{final}")
        else:
            print(f"{red}RESPOSTA ERRADA!{final}")
        contador = 10
    else:
        print(f"{amarelo}NÃO TEM ESSA OPÇÃO! TENTE NOVAMENTE!{final}")
        print()

traço(60)

while contador == 10:
    print("10º - Qual é o principal componente de um computador?")
    print('A) Placa mãe\n'
          'B) Memória\n'
          'C) Processador\n'
          'D) Teclado\n'
          'E) Monitor')
    resp10 = str(input("Informe uma opção: ")).strip().upper()
    print(f"{cinza}AVALIANDO SUA RESPOSTA...{final}")
    sleep(3)
    print()
    if resp10 == "A" or resp10 == "B" or resp10 == "C" or resp10 == "D" or resp10 == "E":
        if resp10 == "A":
            resp_corretas.append(resp10)
            print(f"{green}RESPOSTA CORRETA!{final}")
        else:
            print(f"{red}RESPOSTA ERRADA!{final}")
        contador = 11
    else:
        print(f"{amarelo}NÃO TEM ESSA OPÇÃO! TENTE NOVAMENTE!{final}")
        print()

traço(60)
print(f'{cinza}CALCULANDO A PORCENTAGEM DE ACERTOS...{final}')
sleep(3)
print()
acerto(resp_corretas)

print()
linigl(60)
print(f'{ciano}{"OBRIGADO!!!":-^60}{final}')
linigl(60)
print()
