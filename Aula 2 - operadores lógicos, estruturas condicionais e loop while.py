# Aula 2 - Operadores Lógicos, Estruturas Condicionais e Loop While

# 1) Operadores Lógicos
numero = 200
print(numero < 100)  # False
print(numero > 100)  # True
print(numero == 100)  # False
print(numero != 100)  # True

numero2 = 100
print(numero > numero2)  # True

numero3 = 3.14
print(numero2 < numero3)  # False
print(numero2 != numero3)  # True
print(10 == 10.0)  # True

s1 = "abacate"
s2 = "abacaxi"
print(s1 == s2)  # False
print(s1 > s2)  # False
print(s1 < s2)  # True
print(s2 > s1)  # True

print(ord("t"))  # 116
print(10 != 10.0)  # False
print(10 > 3.14)  # True
print(10 == "10")  # False

# Operadores de Conjunção
print(True and False)  # False
print(False and False)  # False
print(True and True)  # True
print(True or False)  # True
print(False or False)  # False

# 2) Estruturas Condicionais
media = 3
if media >= 5:
    print("Aprovado!")
else:
    print("Reprovado")

media = 4
frequencia = 50
if media >= 9:
    print("Aprovado")
elif media >= 6 and frequencia >= 75:
    print("Aprovado")
elif media >= 6 and frequencia < 75:
    print("Recuperação")
elif media < 6 and frequencia >= 75:
    print("Recuperação")
else:
    print("Reprovado")

# 3) Laços de Repetição (while)
cont = 1
while cont <= 10:
    print(cont)
    cont += 1

num = float(input("Digite um número maior que 10: "))
while num <= 10:
    num = float(input("Número menor ou igual a 10! Digite novamente: "))
print("Número digitado:", num)

num = float(input("Digite um número entre 0 e 10: "))
while not (0 <= num <= 10):
    num = float(input("Número fora do intervalo! Digite novamente: "))
print("Número digitado:", num)

estado_civil = input("Digite seu estado civil (S, C, D, V): ")
while estado_civil not in ["S", "C", "D", "V"]:
    estado_civil = input("Resposta inválida! Digite novamente (S, C, D, V): ")
print("Estado civil:", estado_civil)
