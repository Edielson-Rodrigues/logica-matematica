import math

""" Questão 01 """

# try: 
#   A = input("Digite valor lógico de A: ")
#   B = input("Digite valor lógico de B: ")
#   C = input("Digite valor lógico de C: ")

#   valorLogicoA = (A or B) and not(C)
#   valorLogicoB = not(valorLogicoA)

#   print(f"Valor lógico de A: {valorLogicoA}\nValor lógico de B: {valorLogicoB}")
# except: 
#   print("Error ao calcular valores lógicos")

""" Questão 02 """

# try: 
#   while True: 
#     num = int(input("Digite o número: "))
#     if (not(num)):
#       print("Programa encerrado")
#       break

#     numQuadrado = int(math.pow(num, 2))
#     if (num % 2):
#       if (numQuadrado % 2):
#         print(f"O número {num}, tem o quadrado {numQuadrado}. Logo ambos são ímpares.\n")
#     else: 
#       print(f"O número digitado é par\n")
# except: 
#   print("Erro na rotina")

""" Questão 04 """

# try: 
#   A = True
#   B = False
#   C = True

#   print(f"A ^ (B v C): {A and (B or C)}")
#   print(f"(A ^ B) v C: {(A and B) or C}")
#   print(f"(A ^ B)’ v C: {not(A and B) or C}")
#   print(f"A’ v ( B’ ^ C)’: {not(A) or not( not(B) and C)}")
#   print(f"A v ( B v C)’: {A or not( B or C)}")
# except: 
#   print("Erro na consulta")