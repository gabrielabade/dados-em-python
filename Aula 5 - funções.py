# Aula 5 - Funções

# Função para exibir uma saudação simples
def fala_oi():
    print("Oi!")

# Função que recebe um nome e imprime uma saudação personalizada
def fala_oi_pra_alguem(nome_de_alguem):
    print(f"Oi {nome_de_alguem}, que bom te ver!")

# Função que recebe um nome e uma parte do dia, e imprime um cumprimento
def cumprimenta_parte_do_dia(nome, parte_do_dia):
    '''
    Esta função recebe um nome e uma parte do dia, e imprime na tela um
    cumprimento de acordo com esses dois argumentos

    - nome (str): qualquer nome próprio;
    - parte_do_dia (str): deve ser unicamente uma das três opções: ["manhã", "tarde", "noite"]
    '''
    if parte_do_dia == "manhã":
        cumprimento = "Bom dia"
    elif parte_do_dia == "tarde":
        cumprimento = "Boa tarde"
    elif parte_do_dia == "noite":
        cumprimento = "Boa noite"
    else:
        raise ValueError(f"A parte do dia informada ({parte_do_dia}) não é válida!")

    cumprimento = f"{cumprimento}, {nome}"
    print(cumprimento)
    return cumprimento

# Funções de operações aritméticas simples
def calcula_soma(n1, n2):
    return n1 + n2

def calcula_subtracao(n1, n2):
    return n1 - n2

def calcula_multiplicacao(n1, n2):
    return n1 * n2

def calcula_divisao(n1, n2):
    '''
    Esta função calcula o quociente entre o primeiro argumento e o segundo

    - n1 (float), numerador
    - n2 (float), denominador, deve ser != 0
    '''
    return n1 / n2

# Função de calculadora que recebe dois números e uma operação e retorna o resultado
def calcula_operacao(n1, n2, op):
    '''
    - n1 (float)
    - n2 (float)
    - op (str): indicando a operação a ser feita ["+", "-", "*", "/"]

    returns:

    n1 [op] n2, onde [op] é a operação correspondente à string op
    '''
    if op == "+":
        return calcula_soma(n1, n2)
    elif op == "-":
        return calcula_subtracao(n1, n2)
    elif op == "*":
        return calcula_multiplicacao(n1, n2)
    elif op == "/":
        return calcula_divisao(n1, n2)
    else:
        raise ValueError(f"A operação informada ({op}) não é válida!")

# Exemplos de uso das funções
fala_oi()

fala_oi_pra_alguem("André")

resultado = cumprimenta_parte_do_dia("André", "tarde")
print(resultado)

# Chamando a função de calculadora com soma
resultado_soma = calcula_operacao(2, 3, "+")
print(f"Resultado da soma: {resultado_soma}")

# Chamando a função de calculadora com divisão
resultado_divisao = calcula_operacao(10, 2, "/")
print(f"Resultado da divisão: {resultado_divisao}")

# Exemplo de erro ao passar operação inválida
try:
    calcula_operacao(2, 3, "%")
except ValueError as e:
    print(e)
