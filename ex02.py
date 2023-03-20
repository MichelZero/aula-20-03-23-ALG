# autores:
# Cristiano
# Michel 
#
# Data: 20/03/2023
#
#(só entrada e saída) Faça um algoritmo que leia 3 variáveis, do tipo caractere.
# A seguir troque o valor das 3 variáveis A, B e C, de forma que A fique com o 
# valor de B, B com o valor de C e C com o valor de A. Mostre os valores finais.

# entrada
A = '1' 
B = '2'
C = '3'
temp = ''
# processamento
temp = A
A = B
B = C
C = temp 

# Saída
print(f"A: {A}")
print(f"B: {B}")
print(f"C: {C}")