dado = [[], [], []]
for c in range(0, 3):
    n0 = int(input(f'Digite um valor [0, {c}]: '))
    dado[0].append(n0)
for c in range(0, 3):
    n1 = int(input(f'Digite um valor [1, {c}]: '))
    dado[1].append(n1)
for c in range(0, 3):
    n2 = int(input(f'Digite um valor [2, {c}]: '))
    dado[2].append(n2)
print('-=' * 30)
print(f'[{dado[0][0]:^5}][{dado[0][1]:^5}][{dado[0][2]:^5}]')
print(f'[{dado[1][0]:^5}][{dado[1][1]:^5}][{dado[1][2]:^5}]')
print(f'[{dado[2][0]:^5}][{dado[2][1]:^5}][{dado[2][2]:^5}]')
