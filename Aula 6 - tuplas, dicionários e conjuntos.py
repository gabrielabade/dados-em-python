# Aula 6 - Tuplas, Dicionários e Conjuntos

# 1) Tuplas
# Definindo uma tupla com diferentes tipos de dados
tupla = (1, 4.2, True, "ada", [1, 2, 3])
print(tupla)

# Verificando o comprimento da tupla
print(len(tupla))

# Definindo uma tupla sem parênteses
tupla2 = 1, 2, 3, "a", "b"
print(tupla2)

# Tupla Unpacking
x, y = 2, 3
print(x, y)

# Acessando elementos de uma tupla
print(tupla[1])
print(tupla[-2])

# Iterando sobre a tupla
for elemento in tupla:
    print(elemento)

# Tentando modificar um elemento de uma tupla (causa erro)
# tupla[0] = "Um"  # Isso causará um erro

# Alterando a tupla (procedimento forçado)
lista = list(tupla)
lista[0] = "um"
tupla_modificada = tuple(lista)
print(tupla_modificada)

# Função que retorna múltiplos valores
def valor_valor_quadrado_valor_cubo(x):
    return x, x**2, x**3

print(valor_valor_quadrado_valor_cubo(2))

# 2) Dicionários
# Definindo um dicionário
dicionario = {"a": 2, "b": 6, "c": 9}
print(dicionario["b"])

# Criando um cadastro de pessoas
cadastro_dict = {
    "nomes": ["José", "Maria", "Marta"],
    "idades": [20, 30, 15],
    "cidades": ["SP", "RJ", "Salvador"]
}
print(cadastro_dict["nomes"])

# Adicionando novos elementos ao dicionário
cadastro_dict["alturas"] = [1.8, 1.7, 1.6]
print(cadastro_dict)

# Removendo um elemento do dicionário
cadastro_dict.pop("alturas")
print(cadastro_dict)

# Alterando elementos do dicionário
cadastro_dict["cidades"][1] = "JP"
print(cadastro_dict)

# Adicionando elementos a listas dentro do dicionário
cadastro_dict["nomes"].append("Joaquim")
cadastro_dict["idades"].append(18)
cadastro_dict["cidades"].append("Santo André")
print(cadastro_dict)

# Iterando sobre o dicionário
for chave in cadastro_dict:
    print(cadastro_dict[chave][2])

# Utilizando compreensão de listas
lista_marta = [cadastro_dict[chave][2] for chave in cadastro_dict]
print(lista_marta)

# Utilizando keys() e values()
print(list(cadastro_dict.keys()))
print(list(cadastro_dict.values()))

# Spoiler: pandas
import pandas as pd
print(pd.__version__)

df = pd.DataFrame(cadastro_dict)
print(df)
print(df["nomes"])
print(df.loc[1])

# 3) Conjuntos
# Definindo um conjunto
conjunto = {"a", True, 42, 3.14}
print(conjunto)

# Iterando sobre o conjunto
for elemento in conjunto:
    print(elemento)

# Adicionando e removendo elementos do conjunto
conjunto.add(14)
print(conjunto)
conjunto.remove(14)
print(conjunto)

# Trabalhando com elementos únicos em um conjunto
notas = [9, 0, 6, 6, 0, 8, 2, 0, 3, 9, 2, 3, 5, 4, 3, 9, 8, 5, 6, 2,
         7, 3, 5, 5, 9, 6, 3, 7, 3, 9, 7, 2, 9, 5, 5, 4, 6, 6, 5, 5]
notas_unicas = set(notas)
print(list(notas_unicas))

# Operações entre conjuntos
l1 = ["ada", "python", "dados", 2, 4]
l2 = ["web", "python", "devops", 42, 4]

# Intersecção entre conjuntos
print(set(l1).intersection(set(l2)))

# União entre conjuntos
print(set(l1).union(set(l2)))

# Diferença entre conjuntos
print(set(l1).difference(set(l2)))
print(set(l2).difference(set(l1)))
print(set(l2) - set(l1))
