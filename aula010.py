from time import sleep
"""
Exercício Python #010 - Conversor de Moedas
"""

print('Conversor de moeda\n')

dolar = 4.95

real = float(input('Quantos você tem em reais: '))

valor = real / dolar


print('.....Convertendo.....')
sleep(2)
print('-=-='*20)
print(f'Valor Digitado: \033[;32mR${real:.02f}\033[m')
sleep(2)
print(f'Valor Digente do Dolar: \033[;33mUS${dolar:.02f}\033[m em Dolares')
sleep(2)
print(f'Conversão: \033[;34mR${valor:.02f}\033[m')
print('-=-='*20)