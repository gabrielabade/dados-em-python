# Aula 8  - Programação Orientada a Objetos 2

# Na aula de hoje, vamos explorar os seguintes tópicos em Python:
# 1) Métodos Mágicos

# Problema gerador: como operar com dados de horário?
# Vamos definir uma classe para representar horários. Mas, e se eu quiser somar tempo, como podemos fazer isso?

class Horario:
    def __init__(self, hora, min, seg):
        self.h = hora
        self.m = min
        self.s = seg

    def __repr__(self):
        return f"{self.h:02d}:{self.m:02d}:{self.s:02d}"

    def __str__(self):
        return f"O horário é: {self.h:02d}:{self.m:02d}:{self.s:02d}"

    def __add__(self, other):
        se = self.s + other.s
        mi = self.m + other.m
        ho = self.h + other.h

        if se >= 60:
            mi += 1
            se -= 60
        if mi >= 60:
            ho += 1
            mi -= 60
        if ho >= 24:
            ho -= 24

        return Horario(ho, mi, se)

    def __gt__(self, other):
        if self.h > other.h:
            return True
        elif self.h == other.h and self.m > other.m:
            return True
        elif self.h == other.h and self.m == other.m and self.s > other.s:
            return True
        return False

# Criando instâncias da classe Horario
h1 = Horario(15, 12, 30)
h2 = Horario(7, 38, 41)

# Testando representação
print(h1)
print(h2)

# Testando soma de horários
h3 = h1 + h2
print(f"Entrei às {h1}\nTrabalhei por {h2}\nVou sair às {h3}")

# Testando comparação
print(h1 > h2)
print(h1 < h2)

# Métodos mágicos aritméticos
n1 = 2
n2 = 4
print(n1 + n2)
print(n1.__add__(n2))

# Métodos mágicos aplicados a strings
print("abacate" + "abacaxi")
print("abacate".__add__("abacaxi"))
print("ada" * 3)
print("ada".__mul__(3))

# Métodos mágicos lógicos
print("abacate" > "abacaxi")
print("abacate".__gt__("abacaxi"))
