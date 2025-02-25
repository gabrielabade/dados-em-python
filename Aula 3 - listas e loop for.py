"""
Aula 3 - Listas e Loop For
Exploração de listas, funções de listas e laços de repetição (for) em Python.
"""

# 1) Listas
# Exemplos de criação de listas
lista_numeros = [2, 5, 4.2, -6]
lista_strings = ["andré", "ada", "python"]
lista_mista = ["ada", 10, -4.5]
lista_aninhada = [10, ["ada", "python"], True]

def acessar_elementos():
    minha_lista = ["a", "b", "c", 42, 5, 7, [True, "Ada"], 3.14]
    print(minha_lista[0])  # Primeiro elemento
    print(minha_lista[-1])  # Último elemento
    print(minha_lista[1:4])  # Slice de elementos

# Operações com listas
def operacoes_listas():
    l1 = [1, 2, 3]
    l2 = ["4", 5, "6"]
    print(l1 + l2)  # Concatenação
    print(l1 * 4)  # Repetição
    print(list("André"))  # Transformação de string para lista

# 2) Funções de listas
def manipular_listas():
    lista = []
    lista.append(5)
    lista.append(10)
    lista.insert(1, True)
    lista[2] = "andré"
    lista.remove(10)
    lista.append(15)
    print(lista.pop(2))  # Remove pelo índice
    print(sorted([10, 2, -6, 4.2, 8, 3.14]))  # Ordenação

# Cálculo de média
def calcular_media():
    num_notas = int(input("Digite o número de notas: "))
    notas = [float(input("Digite a nota: ")) for _ in range(num_notas)]
    print("\nA média é:", sum(notas) / len(notas))

# 3) Laço For
def usar_for():
    lista_num = [10, 2, -6, 4.2, 8, 3.14, -6]
    for item in lista_num:
        print(item)

# Separação de números positivos e negativos
def separar_numeros():
    lista_num = [-10, 2, -6, 4.2, -8, 3.14, -6, 0]
    lista_pos = [x for x in lista_num if x > 0]
    lista_neg = [x for x in lista_num if x < 0]
    lista_neutro = [x for x in lista_num if x == 0]
    print(lista_pos, lista_neg, lista_neutro)

# Uso do zip para somar listas
def somar_listas():
    l1, l2 = [1, 2, 3], [4, 5, 6]
    lista_soma = [a + b for a, b in zip(l1, l2)]
    print(lista_soma)

# Compreensão de listas
def list_comprehension():
    lista_num = [4, 7, 13, 15, 1, 8, 16, 20, 3]
    lista_par_ou_impar = ["par" if x % 2 == 0 else "ímpar" for x in lista_num]
    print(lista_par_ou_impar)

# Chamando as funções para demonstração
if __name__ == "__main__":
    acessar_elementos()
    operacoes_listas()
    # calcular_media()  # Descomente para executar a entrada do usuário
    usar_for()
    separar_numeros()
    somar_listas()
    list_comprehension()
