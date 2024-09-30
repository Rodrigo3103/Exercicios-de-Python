"""
Exercício Python #007 - Média Aritmética
"""

nome = ''
n1 = n2 = media = 0

nome = str(input('Digite o Nome do aluno: ')).strip().upper()

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

print(f'A soma das Notas do aluno(a): {nome},\nA primeira nota é: {n1},\nA segunda nota {n2}, soma das notas é: {n1+n2}, por fim,\nA média foi: {((n1+n2)/2)}')