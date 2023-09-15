n = str(input("insira uma frase ou nome: ")).strip().upper()
junto=(n.replace(" ", ""))
inverso= ""
for letra in range(len(junto)-1, -1, -1):
    inverso+=junto[letra]
if junto == inverso:
    print("temos um palindromo")
else:
    print("frase ou palavra digitada não é um palindromo")
print(junto, inverso)
