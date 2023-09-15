print("========== LOJAS KGSL ==========")
preço = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] À vista dinheiro/cheque
[ 2 ] À vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opção = int(input("Qual é a opção? "))
if opção == 1:
    desconto = preço - preço * 0.10
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final. '.format(preço, desconto))
elif opção == 2:
    desconto = preço - preço * 0.05
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final. '.format(preço, desconto))
elif opção == 3:
    print('Sua compra será parcelada em 2x de R${:.2f} SEM JUROS.'.format(preço/2))
    print('Sua compra vai custar R${:.2f} no final.'.format(preço))
elif opção == 4:
    parcelas = int(input('Quantas parcelas? '))
    juros = preço * 0.20 + preço
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS.'.format(parcelas, juros/parcelas))
    print('Sua compra de R${:.2f} vai curtar R${:.2f} no final.'.format(preço, juros))
else:
    print('OPÇÃO INVÁLIDA de pagamento. Tente novamente!')