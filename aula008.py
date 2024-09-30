"""
Exercício Python #008 - Conversor de Medidas
"""

numero = float(input('Digite Um número em metros: '))

cm = numero * 100
mm = numero * 1000

print(f'A media de {int(numero)}M Corresponde a {int(cm)}Cm e {int(mm)}Mm')
