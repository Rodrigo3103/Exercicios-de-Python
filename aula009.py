"""
Exercício Python #009 - Tabuada
"""

num = int(input('Digite um numero para ver sua tabuada: '))
cont = 0
print('-' * 15)
for cont in range(0, 10, 1):
    cont = cont + 1
    if (num * cont) < 10:
        print(f'0{num} x 0{cont} = 0{num * cont}')

    else:
        print(f'0{num} x {cont} = {num * cont:2}')

print('-' * 15)
