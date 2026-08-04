# Fundamentos de Programação 
#   1. Variáveis e Tipos de dados 
# Uma variáveis serve para guardar um valor, podem ser
# eles numeros com ou sem virgula, textos, true or false,
# entre outros. 
# Numeros sem vírgula: int (15, 90, -2011)
# Numeros com vírgula: float (-3.43, 8.09, 23.0)
# Texto == boolean (Verdadeiro ou Falso)
#       int
A = int(input())
B = int(input())
SUBTRAÇÃO = A - B 
print (f"X = {SUBTRAÇÃO}")
#Subtração, adição, divisão, multiplicação, etc. numeros sem virgula

#       float
peso = float(input())
print ("Seu peso é:", peso)
#peso ou altura, numeros com virgula

#       string 
nome = (input("Digite seu nome:"))
print ("Olá,",nome)
#sequencia de caracteres ou seja, nomes, textos.

#       boolean
maior_de_idade = False
print(maior_de_idade)

#verdadeiro ou falso 
#   2. Entrada de Dados 
#   3. Saida de dados
#Entrada: é quando eu envio dados de fora para dentro. Ou seja eu usuaria mando uma informação para o cumputador e espero ele me retornar ou seguir meu comando 
#Saída: mesma coisa, só que agora quem me manda informações é o próprio computador e eu usuaria recebo elas na minha tela.
#       Entrada 
(input("Digite seu nome:"))
# é como se eu falasse com o computador, mando uma informação para ele 

#       Saída
print ("Olá,",nome)
# agora é o computador falando comigo, ele me mostra uma informação 

#   4. Estruturas de Repetição
#   5. Estruturas de Condição
#Condição: o próprio nome diz "condição", então se uma infomação for verdadeira acontece uma coisa, mas se não for acontece outra coisa.
#Repetição: de novo, autoexplicativo , ele executa algo varias vezes ou até que alguma outra coisa aconteça.
#   Condição
nota = 10
if nota >= 6:
    print("Aprovado")
else:
    print("Reprovado")

#   Repetição
for i in range(5):
    print(i)

#   6.Sub-rotinas
# é quando você cria um bloco de instruções com um nome, e ele pode ser usado varias vezes durante o código, que faz com que não haja muitas repetições de código.

def ola(): #Defina (ola)
    print("Olá!")

ola()