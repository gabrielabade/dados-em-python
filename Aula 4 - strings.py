"""
Aula 4 - Strings em Python

Explorando Strings, Funções de Strings e Formatação de Strings.
"""

def exemplo_strings():
    nome = "André"
    print(nome[0])  # Acessando o primeiro caractere
    print(nome[-1])  # Acessando o último caractere
    print(len(nome))  # Obtendo o comprimento da string
    
    for caractere in nome:
        print(caractere)
    
    for i in range(len(nome)):
        print(nome[i])
    
    # Alteração de caracteres com replace()
    nome = nome.replace("é", "E")
    print(nome)
    
    # Transformação em lista e modificação
    nome_lista = list(nome)
    nome_lista[-1] = "É"
    print("".join(nome_lista))

def operacoes_strings():
    print("a" + "b")  # Concatenação
    print("abc" * 5)  # Repetição
    print("=" * 50)
    print("OLÁ, BEM-VINDOS À ADA TECH".center(50))
    print("=" * 50)

def funcoes_strings():
    boas_vindas_ada = "Bem vindos à Ada!"
    print(boas_vindas_ada.upper())
    print(boas_vindas_ada.lower())
    print(boas_vindas_ada.title())
    print(boas_vindas_ada.capitalize())
    print(boas_vindas_ada.split())
    print(boas_vindas_ada.split("n"))

def limpar_espacos():
    string = "            eu gosto de estudar python   "
    print(string.strip())
    
    string = "            eu    gosto de         estudar python   "
    print(" ".join(string.split()))

def classificar_caracteres():
    fala = "ele disse para o colega: 'nos encontramos amanhã às 14:00??'"
    
    letras, numeros, simbolos = [], [], []
    for char in fala:
        if char.isalpha():
            letras.append(char)
        elif char.isdigit():
            numeros.append(char)
        else:
            simbolos.append(char)
    
    print(letras)
    print(numeros)
    print(simbolos)

def formatacao_strings():
    dia, mes, ano = 1, 2, 2020
    print(f"{dia:02d}/{mes:02d}/{ano:04d}")
    preco = 1499.50
    print(f"Preço: R$ {preco:.2f}")

def validar_estado_civil():
    estados_civis = {
        "S": "Solteiro",
        "C": "Casado",
        "D": "Divorciado",
        "V": "Viúvo"
    }
    
    estado_civil = input("Digite seu estado civil (S, C, D, V ou por extenso): ").strip().upper()
    
    while estado_civil not in estados_civis and estado_civil not in map(str.upper, estados_civis.values()):
        estado_civil = input("Resposta inválida! Digite novamente seu estado civil: ").strip().upper()
    
    if estado_civil in estados_civis:
        print(f"Estado civil: {estados_civis[estado_civil]}")
    else:
        print(f"Estado civil: {estado_civil.capitalize()}")

# Chamadas para testes das funções
if __name__ == "__main__":
    exemplo_strings()
    operacoes_strings()
    funcoes_strings()
    limpar_espacos()
    classificar_caracteres()
    formatacao_strings()
    validar_estado_civil()
