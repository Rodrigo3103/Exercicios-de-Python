import math
"""
Exercício Python #006 - Dobro, Triplo, Raiz Quadrada
"""


"""
Crie um algoritmo que leia um número e mostre o seu dobro , triplo e raiz quadrada.
"""

"""
def de calculos
"""
def calculos(num):
    ok = False
    valor = 0
    while True:
        n = str(input(num))
        if n.isnumeric():

            if valor %2==0:
                valor = int(n)

            elif valor %2==1:
                valor = int(n)



        else:
            print(f'\033[0;31mErro Digite apenas números inteiros\033[m')
            if ok:
                break
        return valor



""""""

numero = calculos('Digite um Número inteiro: ')

dobro = (numero*2)
triplo = (numero*3)
raizQuadrada = math.sqrt(numero)

if raizQuadrada% 2==0:
    print(f'O Número digitado foi {numero},\nO dobro é: {dobro},\nO triplo é: {triplo} \nE a raiz quadrada é: {float(raizQuadrada):.0f} ')
else:
    print(f'O Número digitado foi {numero},\nO dobro é: {dobro},\nO triplo é: {triplo} \nE a raiz quadrada é: {float(raizQuadrada):.2f} ')


