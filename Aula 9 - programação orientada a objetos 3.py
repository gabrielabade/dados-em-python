# Aula 9  - Programacao Orientada a Objetos 3

# Na aula de hoje, vamos explorar os seguintes topicos em Python:
# - 1) Heranca e Polimorfismo

# Problema gerador: como aproveitar classes ja criadas para criar classes derivadas?

# 1) Heranca e Polimorfismo

# Imagine que voce tenha varias classes com os mesmos atributos, os mesmos metodos e mesmos parametros.
# Reescreve-los varias vezes e um desperdicio de tempo! Alem disso, se precisarmos atualizar um metodo, 
# precisaremos fazer a modificacao multiplas vezes. 

# Para solucionar esta questao, trataremos dos conceitos de **heranca** e **polimorfismo**.

# Heranca
# E possivel criar **classes filhas** que herdem atributos e metodos de uma **classe mae** atraves de **heranca**.
# Para herdar, colocamos o **nome da classe mae entre parenteses** na frente do nome da classe filha em sua definicao.
# Se necessario, podemos redefinir um metodo na classe filha.

class Animal:
    def __init__(self, nome):
        self.nome = nome
    
    def fala(self):
        print(f"{self.nome} faz barulho!")

a1 = Animal("grilo")
a1.fala()

class Cachorro(Animal):
    def fala(self):
        print(f"{self.nome} late!")

c1 = Cachorro("leo")
c1.fala()

class Gato(Animal):
    def fala(self):
        print(f"{self.nome} mia!")

g1 = Gato("fred")
g1.fala()

# Imagine agora que queremos herdar um metodo **parcialmente**, com a possibilidade de altera-lo.
# (Isso e importante, pois se apenas copiassemos o metodo original, qualquer alteracao nele teria de ser feita 
# em todos os locais onde ele e copiado...)

# Para isso, usamos o metodo `super()`

class Cachorro(Animal):
    def __init__(self, nome, raca, cor_do_pelo):
        super().__init__(nome)
        self.raca = raca
        self.cor_do_pelo = cor_do_pelo
    
    def fala(self):
        super().fala()
        print(f"Mas, por ser um cachorro, {self.nome} late!")

c2 = Cachorro("leo", "poodle", "branco")
c2.fala()

# Polimorfismo
# Do grego, **"varias formas"**. A ideia e que um objeto de uma certa classe pode se comportar como objeto de outras classes. 
# Mais especificamente, **objetos de uma classe filha podem tambem ser tratados como se pertencessem a classe mae**.

# O metodo `isinstance` recebe 2 parametros: um objeto e uma classe. 
# Ele retorna True caso o objeto pertença a classe, e False caso nao pertença.

# Isso e util porque uma funcao que seja feita para lidar com Animal sera capaz de lidar com qualquer classe herdeira de Animal 
# com a mesma facilidade.

g2 = Gato("fred")
c2 = Cachorro("leo", "poodle", "branco")

print(isinstance(g2, Gato))       # True
print(isinstance(c2, Cachorro))   # True
print(isinstance(g2, Animal))     # True
print(isinstance(c2, Animal))     # True
print(isinstance(g2, Cachorro))   # False
print(isinstance(c2, Gato))       # False

nome = "ada"
print(isinstance(nome, int))      # False
