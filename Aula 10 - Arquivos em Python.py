# Aula 10 - Arquivos em Python

# Na aula de hoje, vamos explorar os seguintes tópicos em Python:
#
# - 1) Arquivos em Python
# - 2) Arquivos csv

# Problema gerador: como podemos processar um arquivo com as notas de alunos?

# 1) Arquivos em Python

# Todos os programas que fizemos até o momento tinham variáveis, input e output **temporários**, guardados na memória RAM do computador **enquanto o programa é executado**.

# Após o programa ser finalizado, todas as variáveis, inputs e outputs eram perdidos.

# Muitas vezes queremos que esses valores sejam armazenados, que os dados processados pelo programa sejam preservados. O termo para esta característica é **persistência de dados**.

# A persistência se dá através de **arquivos**: documentos criados para **armazenar dados em uma memória permanente**, como o **disco rígido**, um **USB** ou um **servidor web**.

# O Python tem algumas funções padrão para a manipulação de arquivos. Vamos vê-las!

# A função `open()` é usada para abrir arquivos existentes ou criar um arquivo novo. 

# Ela possui 2 argumentos: o primeiro é o caminho do arquivo, com seu nome (se apenas o nome do arquivo for passado, isso é interpretado como o arquivo estando na mesma pasta que o código!); e o segundo é o modo de operação. Os modos são:

# - r - lê um arquivo existente
# - w - cria um novo arquivo
# - a - abre um arquivo existente para adicionar informações ao seu final
# - \+ - ao ser combinado com outros modos, permite alteração de arquivo já existente (ex: r+ abre um arquivo existente e permite modificá-lo)

# O terceiro argumento é o "encoding", que dá a codificação do arquivo. Para evitar problemas, é legal sempre usar `encoding="utf-8"`

arquivo = open("ola_mundo.txt", "w", encoding="utf-8")

# Se analisarmos a variável "arquivo" (é o retorno da função `open()`), note que há algumas coisas estranhas... É assim que o python entende seu arquivo, mas não precisa se preocupar muito com isso

print(arquivo)

# Uma vez aberto o arquivo, podemos escrever alguma coisa nele. Para isso, usamos o método `write()`

# Essa função aceita apenas um argumento, que é o que queremos escrever no arquivo -- e **deve ser uma string**!

arquivo.write("olá, mundo!")

# Após abrirmos (ou criarmos) um arquivo, e fazer as operações desejadas com ele, devemos fechá-lo usando o método `close()`. Essa etapa é importante por 2 motivos:

# - Se alteramos o arquivo mas não o fechamos, as alterações não serão salvas.
# - Se esquecermos de fechar um arquivo, outros programas podem ter problemas de acesso a ele.

# Por isso, **nunca se esqueça de fechar os arquivos abertos!**

arquivo.close()

# Fazendo todas as operações em uma única célula

f = open("ola_mundo2.txt", "w", encoding="utf-8")

f.write("olá, mundo!\nEsse é meu segundo arquivo!")

f.close()

# Apesar desta ser uma forma clara e direta, existe um procedimento mais robusto e mais seguro, que é utilizando o ambiente `with`.

# O `with` garante que, quando o bloco de código em seu interior for executado, todos os recursos que foram criados (indicados após o `as`) serão liberados!

# No nosso caso, o recurso é justamente um arquivo! Com o `with`, nós garantimos que **o arquivo será aberto e fechado**, independente se ocorra qualquer erro antes do arquivo ser fechado! Isso é muito importante, pois garante maior segurança e robustez ao nosso código!

with open("ola_mundo3.txt", "w", encoding="utf-8") as f:
    f.write("olá, mundo!\nEsse é meu segundo arquivo!\né UM TERCEIRO ARQUIVO, usando o with!")

# Como essa maneira é mais robusta, vamos usá-la daqui para frente. (Mas, lembre-se que a opção que apresentamos primeiro também é possível!)

# 2) Arquivos CSV

# Um tipo de arquivo muito comum é o **csv**

# A sigla CSV significa **Comma-Separated Values**, ou **"valores separados por vírgula"**. 

# Este formato é uma forma padrão de representar tabelas usando arquivos de texto simples: cada elemento é separado por uma vírgula (ou ponto-e-vírgula, ou, qualquer outro separador), e cada linha é separada por uma quebra de linha. 

# Em Python, podemos entender um arquivo CSV como uma lista de listas. 

# Imagine que queremos armazenar um arquivo csv. Começamos com uma lista de listas:

tabela = [['Aluno', 'Nota 1', 'Nota 2', ' Presença'],
          ['Luke', 7, 9, 75],
          ['Han', 4, 7, 100],
          ['Leia', 9, 9, 50]]

import csv

with open("alunos_star_wars.csv", "w", encoding="utf-8") as f:
    csv.writer(f, delimiter=",", lineterminator="\n").writerows(tabela)

# Vamos agora processar esse arquivo que acabamos de ler?

# Imagina que queremos calcular qual é a média de determinado aluno, a partir do seu nome!

with open("alunos_star_wars.csv", "r", encoding="utf-8") as f:
    tabela_lida = [linha for linha in csv.reader(f, delimiter=",", lineterminator="\n")]

lista_nome_alunos = [linha[0] for linha in tabela_lida]

aluno = input(f"Digite o nome do aluno cuja média você quer saber.\nOpções: {lista_nome_alunos[1:]} ")

dados_aluno = tabela_lida[lista_nome_alunos.index(aluno)]

nota1 = float(dados_aluno[1])
nota2 = float(dados_aluno[2])

media = (nota1 + nota2) / 2

print(f"\nA média do(a) aluno(a) {aluno} é: {media}")

# É possível fazer o **processamento de arquivos** de forma muito mais simples e natural do que foi feito acima, ao utilizarmos uma biblioteca própria para isso: o pandas! Vamos introduzi-la nas aulas seguintes!
