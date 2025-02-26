# Aula 7 - programação orientada a objetos 1

"""
Na aula de hoje, vamos explorar os seguintes tópicos em Python:

- 1) Programação Orientada a Objetos;
- 2) Classes, Atributos, Objetos e Métodos;

_____________

### Problema gerador: como representar uma pessoa em um jogo eletrônico?

Precisamos de uma estrutura pra armazenar todas as informações e ações de um personagem de um jogo. Como fazer isso?

____
____
____

## 1) Programação Orientada a Objetos

O Python, como outras linguagens, é classificada como uma **linguagem de programação orientada a objetos (POO)** (outros exemplos: Java, C++, etc). 

Esta classificação é uma dos chamados "paradigmas de programação". Isso porque uma linguagem de POO é fundamentalmente diferente de linguagens de outros paradigmas.

O grande objetivo da POO é a **reutilização de código**.

Os programas devem ser **modularizados**, de modo que diferentes pessoas possam implementar módulos diferentes e juntá-los ao final, e reaproveitar módulos diferentes.

Dentro de POO, tudo isso é feito de acordo com as seguintes **entidades**:

- **Classes**: São os "moldes" dos objetos, as entidades abstratas. Elas contêm as informações e os comportamentos que os objetos terão. Todos os objetos pertencentes a uma mesma classe terão características em comum. **Ex: Pessoa**

- **Objetos**: São as instâncias concretas das classes, que são abstratas. Os objetos contêm as características comuns à classe, mas cada um tem suas particularidades. **Ex: você!**

- **Atributos**: Cada objeto particular de uma mesma classe tem valores diferentes para as variáveis internas da classe. Essas "variáveis do objeto" chamamos de atributos. **Ex: a cor do seu cabelo**

- **Métodos**: São funções dentro da classe, que não podem ser executadas arbitrariamente, mas deverão ser chamadas necessariamente pelos objetos. Os métodos podem utilizar os atributos e até mesmo alterá-los. **Ex: você pintar seu cabelo para mudar a cor** 

Em POO, há **4 princípios de boas práticas** para a criação das entidades:

- **Encapsulamento**: cada classe deve conter todas as informações necessárias para seu funcionamento, bem como todos os métodos necessários para alterar essas informações.

- **Abstração**: as classes devem apresentar interfaces simples para o uso por outros desenvolvedores e para a interação com outras classes. Todos os detalhes complicados de seu funcionamento devem estar "escondidos" dentro de métodos simples de usar, com parâmetros e retornos bem definidos. 

- **Herança**: se várias classes terão atributos e métodos em comum, não devemos ter que redigitá-los várias vezes. Ao invés disso, criamos uma classe com esses atributos e métodos comuns e as outras classes irão herdá-los.
        
- **Polimorfismo**: objetos de diferentes classes herdeiras de uma mesma classe mãe podem ser tratados genericamente como objetos pertencentes à classe mãe.

Vamos agora a exemplos específicos para ilustrar e concretizar todos os conceitos discutidos acima!
"""

class Pessoa:
    def __init__(self, name, age, res):
        # Inicializar os atributos da classe
        self.nome = name
        self.idade = age
        self.residencia = res
        
        # Inicializar alguns atributos cujos valores são fixados
        self.num_filhos = 0
        self.profissao = None
        self.salario = 0
    
    # Definição de outros métodos
    def fala(self, mensagem):
        print(f"{self.nome} diz: '{mensagem}'")
    
    def consegue_emprego(self, prof, valor_salario):
        self.profissao = prof
        self.salario = valor_salario
    
    def aumenta_salario(self, porcentagem):
        """
        porcentagem: float entre 0 e 1, indicando o percentual de aumento de salario
        """
        self.salario = self.salario * (1 + porcentagem)

# Criação de objeto: instanciando uma classe
maria = Pessoa(name="Maria", age=18, res="Paris")

print(maria.profissao, maria.salario)

maria.consegue_emprego("cientista de dados", 7000)
print(maria.profissao, maria.salario)

maria.aumenta_salario(0.2)
print(maria.profissao, maria.salario)

# Exemplos de métodos em outras classes internas do Python
numero = 4
nome = "ada"
notas = [10, 9, 8, 5, 5, 7, 9.8]

print(nome.upper())
notas.append(10)
print(notas)
print(1 + 2)
print("a" + "b")
