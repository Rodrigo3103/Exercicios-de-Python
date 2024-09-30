"""
Exercício Python #004 - Dissecando uma Variável

"""

algo = input('Digite alguma coisa: ')
print('O tipo primitivo desse valor é: ', type(algo))
print('Só tem espaços? ', algo.isspace())
print('é Número? ', algo.isnumeric())
print('é alfabetico? ', algo.isalpha())
print('é alfanumerico', algo.isnumeric())
print('é maiúscula? ', algo.isupper())
print('é minúscula? ', algo.islower())
print('esta capitalizada? ', algo.istitle())