"""
Aula 1 - Tipos de dados, input/output, operadores matemáticos
"""

# 1) Tipos de variáveis

# Tipo inteiro (int)
numero_de_filhos = 3
print(numero_de_filhos, type(numero_de_filhos))

# Tipo float (float)
altura = 1.78
print(altura, type(altura))

# Tipo string (str)
nome = "André"
trabalho = 'Ada'
print(nome, trabalho)

trecho_de_livro = 'E aí Joãozinho disse: "Oi, tudo bem?"'
print(trecho_de_livro)

nome_comunidade = "Comunidade Let's Code"
print(nome_comunidade)

# Tipo booleano (bool)
print(True, type(True))
print(False, type(False))

# 2) Comentários
# Esse é um comentário de uma linha

"""
Esse é um comentário de múltiplas linhas.
Pode ser utilizado para documentar funções e classes.
"""

# 3) Saída (output)
print("Olá, mundo!")
numero = 50
nome_do_numero = "cinquenta"
print(numero, nome_do_numero, "OIEEE", sep="__")
print("Olá\nmundo!")

# 4) Entrada (input)
nome_usuario = input("Digite seu nome: ")
print("Bom dia,", nome_usuario)

idade = int(input("Digite sua idade: "))
print("Sua idade em 5 anos será:", idade + 5)

altura_usuario = float(input("Digite sua altura: "))
print("Sua altura:", altura_usuario)

# 5) Operadores matemáticos
print("Soma:", 2 + 2)
print("Subtração:", 10 - 3)
print("Multiplicação:", 4 * 3)
print("Divisão:", 10 / 7)
print("Potência:", 2 ** 3)
print("Divisão inteira:", 10 // 7)
print("Resto da divisão:", 10 % 7)

# Verificação de número par ou ímpar
numero_verificar = int(input("Digite um número para verificar se é par ou ímpar: "))
if numero_verificar % 2 == 0:
    print("O número ", numero_verificar, "é par.")
else:
    print("O número ", numero_verificar, "é ímpar.")

# Concatenação de strings
print("Concatenação:", "let's" + " " + "code")
print("Repetição:", "a" * 4)
