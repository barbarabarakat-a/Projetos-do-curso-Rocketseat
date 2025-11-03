# This is my first Python program
from collections import deque
import getpass
import math
print("Hello World!")
print("It's really good.")

# Variables: string, integer, float, boolean:

# String
first_name = "Barbara"
email = "barbara123@fake.com"

print(first_name)
print(f"Hello {first_name}")
print(f"Your email is: {email}")

# Integer
age = 30
print(f"You are {age} years old")

# Float
price = 10.99
print(f"The price is: {price}")

# Boolean
is_student = True

print(f"Are you a student? {is_student}")

if is_student:
    print("You are a student")
else:
    print("You are not a student.")

for_sale = False

if for_sale:
    print("That item is for sale")
else:
    print("That item is not for sale")


# Typecasting: the process of converting a variable from one data type to another
"""str()
   int()
   float()
   bool()"""

name = "Barbara Bana"  # str
age = 30  # int
gpa = 3.8  # float
is_student = True  # bool

print(type(name))

gpa = int(gpa)
print(gpa)

age = float(age)
print(age)

# If we want to add numbers to it, it will be an error, because its a string now
age = str(age)
print(age)  # It will keep showing a number but the description has changed
print(type(age))

name = bool(name)
print(name)  # This we can also use to discover if someone type the name before, if doesnt have that name, it will appears FALSE

# input(): a function that prompt the user to enter data
#          returns the entered data as a string

# We need to tell the user what we want them to type in.
name = input("What is your name?: ")
# The input function is going to return some data as a string
# When we accept user input, we store that input as a string.
age = input("How old are you?")
print(type(age))

age = int(input("How old are you?"))
print(type(age))

# or, other example:
age = int(age)
age = age + 1


print(f"Hello {name}!")
print("Happy Birthday!")
print(f"You are {age} years old now")

# Exercise 1: Retangle Area Calc. (A = w * l)
lenght = float(input("Enter the lenght: "))
width = float(input("Enter the width: "))

area = lenght * width
print(f" The area is: {area}m\u00B2")

# Exercise 2: cShopping Cart Program

item = input("What item would you like to buy?: ")
price = float(input("What is the price?: "))
quantity = int(input("How many would you like?: "))

total = price * quantity
print(f"You have bought {quantity} x {item}/s")
print(f"Your total is: ${total}")

# Madlibs game:
adjective1 = input("Enter an adjective (description): ")
adjective2 = input("Enter an adjective (description): ")
adjective3 = input("Enter an adjective (description): ")
noun1 = input("Enter a noun (person, place, thing): ")
verb1 = input("Enter a verb ending with 'ing': ")

print(f"Today I went to a {adjective1} zoo.")
print(f"In an exhibit, I saw a {noun1}.")
print(f"{noun1} was {adjective2} and {verb1}")
print(f"I was {adjective3}!")


friends = 0
# friends = friends + 1  (an option)
# This is known as an augmented assignment. (shortcut operators) (second option)
friends += 1
# [+=] [-=] [*=] [/=] [**=]
# remainder = friends % 3 {print(remainder)} -> (Its popular to use this operator to find if a number is even or odd)
print(friends)


x = 3.14
w = 3
y = -4
z = 5

# round function
result = round(x)
print(result)

# absolute value
result1 = abs(y)
print(result1)

# Built-in power function
result2 = pow(5, 4)  # we need a base, and an exponent
print(result2)

# Max function: We can find the maximum value of a various values.
result3 = max(x, w, y, z)
print(result3)
# otherwise, there's MIN
result4 = min(x, w, y, z)
print(result4)


# MATH FUNCTIONS -> EXERCISE

radius = float(input('Enter the radius of a circle: '))
circumference = 2 * math.pi * radius

print(f"The circumference is: {round(circumference, 2)}")


a = float(input("Enter side A: "))
b = float(input("Enter side B: "))

c = math.sqrt(((pow(a, 2) + (pow(b, 2)))))
print(f"The hypotenuse is: {round(c, 2)}")


# IF STATEMENT:
age = int(input("Enter your age: "))

if age >= 18 and age <= 99:
    print("You are now signed up!")
elif age <= 0:
    print("You need enter a valid age.")
elif age >= 100:
    print("You are too old to sign up.")
else:
    print("You can not sign for it.")

# Other option is to put 100 as the first condition
# if age >= 100:
    # print("You are too old to sign up.")
# elif age >= 18:
    # print("You are now signed up!")


responde = input("Would you like food? (N/Y): ")

if responde.upper() == "Y":
    print("Have some food.")
elif responde.upper() == "N":
    print("That's ok, Have a good day")
else:
    print("Try a valid key (Y or N).")


# Get age as an integer
age = int(input("Enter your age: "))

# Get parental guidance as a boolean (True/False)
with_parent = input() == "true"

# Declare a variable named message with "None"
message = "None"

# Write your nested if-else code here
if age < 18:
    if with_parent == "true":
        message = "You can watch PG-13 movies"
    elif with_parent == "false":
        message = "You can only watch G-rated movies"
elif age >= 18:
    message = "You can watch any movie"

# Don't change below this line
print(message)


first_input = int(input())
second_input = int(input())
sum = 0

for i in range(first_input):
    for j in range(second_input):
        sum += j
        print(sum)


# Registration:
print("====== User Registration ======")
register_username = input("Create an username: ")
register_password = getpass.getpass("Create a password: ")

print("You are Registered!")


# Login
attempts = 3

while attempts > 0:

    print("====== User Login ======")
    username = input("Enter your username: ")
    password = getpass.getpass("Enter your password: ")

    if username == register_username and password == register_password:
        print("Now, you are login.")
    else:
        attempts -= 1
        print(
            f"Login Failed! Username or/and password are incorrect. You still have {attempts} times")

if attempts == 0:
    print("Try it later")


# Factorial of n

n = int(input("Enter a number:"))
f = 1

while n > 1:
    f = (f * n)
    n = n - 1

    print(f)


# create a list
questions = [['Does it eat bananas?', 'monkey']]

# while true to create an infinite looping
while True:
    print("Think about an animal... ")

    # right to looping the questions
    right = False
    for question in questions:
        answer = input(f'{question[0]} yes/no: ').lower()
        if answer == 'yes':
            print(f'You thought of an animal - a {question[1]}')
            right = True
            break

    # to create a new list inside of questions' list
    if not right:
        animal = input('I give up! What is the animal you though on?: ')
        new_question = input(
            'What question make you think about in that animal?: ')
        questions.append([new_question, animal])

        answer = input('Do you want to play again? (yes/no): ').lower()
        if answer != 'yes':
            print("Ok! It was good to play with you.")
            break

# Create the boardgame for tic tac toe
boardgame = [[' ' for _ in range(3)]for _ in range(3)]


# Create your player as a global variable:
player = "X"

# Create a function that always when needed, it will to show the boardgame:


def showBoardgame():
    for row in boardgame:
        print("|".join(row))
        print("-" * 5)

# Create a function to get the play and also test to see if its a valid play turn:


def playtime(row, column):
    if (
        not 0 <= row <= 2 or
        not 0 <= column <= 2 or
        boardgame[row][column] != ' '
    ):
        print("Invalid playtime! Try again other position.")
        return player

    boardgame[row][column] = player
    return "O" if player == "X" else "X"

# Create a function to know who will win the game or if its tied game:


def gameresult():
    # Verify rows:
    for row in range(3):
        if (
            boardgame[row][0] != ' ' and
            boardgame[row][0] == boardgame[row][1] and
            boardgame[row][0] == boardgame[row][2]
        ):

            print(f"{boardgame[row][0]} GANHOU !!")
            return True

    # Verify columns:
    for column in range(3):
        if (
            boardgame[0][column] != ' ' and
            boardgame[0][column] == boardgame[1][column] and
            boardgame[0][column] == boardgame[2][column]
        ):

            print(f"{boardgame[0][column]} GANHOU !!")
            return True

    # Verify diagonals:
        if (
            boardgame[1][1] != ' ' and
            (
                (
                    boardgame[0][0] == boardgame[1][1] and
                    boardgame[0][0] == boardgame[2][2]
                ) or
                (
                boardgame[2][0] == boardgame[1][1] and
                boardgame[2][0] == boardgame[0][2]
                )
            )
        ):

            print(f"{boardgame[1][1]} GANHOU !!")
            return True


# if didn't have a win:
    return False

# Create a function to finish when the game is tied:


def tiedgame():
    for row in range(3):
        for column in range(3):
            if boardgame[row][column] == ' ':
                return False
    print("It's tied game.")
    return True


# Create a looping to keep asking the inputs from users:
while True:
    print(f"It's {player} turn to play")
    try:
        row = int(input("Type the row: "))
        column = int(input("Type the column: "))
        player = playtime(row, column)
    except (ValueError, IndexError):
        print("Type number between 0 to 2: ")

    showBoardgame()
    if gameresult() or tiedgame():
        break


# example:
def calcular_media(notas):
    return sum(notas) / len(notas)


def verificar_aprovacao(media):
    if media >= 6:
        return "Aprovado"
    else:
        return "Reprovado"


notas = [7, 5, 2]
media = calcular_media(notas)
print(calcular_media(notas))
print(verificar_aprovacao(media))


# disco de hanoi
def mover_discos(num_discos, origem, destino, auxiliar):
    if num_discos == 1:
        print(f"Mover disco 1 da {origem} para {destino}")
    else:
        mover_discos(num_discos - 1, origem, auxiliar, destino)
        print(f"Mover disco {num_discos} da {origem} para {destino}")
        mover_discos(num_discos - 1, auxiliar, destino, origem)


mover_discos(3, "Torre 1", "Torre 3", "Torre 2")


# EXEMPLO DE FILA:

def criarFila():
    return []


def insereNaFila(fila, elemento):
    fila.append(elemento)


def removeDaFila(fila):
    return fila.pop(0)


pilha = criarFila()

print(pilha)
insereNaFila(pilha, 8)
insereNaFila(pilha, 9)
insereNaFila(pilha, 10)
insereNaFila(pilha, 11)
insereNaFila(pilha, 12)
print(f"remover: {removeDaFila(pilha)}")
print(f"remover: {removeDaFila(pilha)}")
print(pilha)


# EXEMPLO DE PILHA:

def criarPilha():
    return []


def insereNaPilha(pilha, elemento):
    pilha.append(elemento)


def removeDaPilha(pilha):
    return pilha.pop()


pilha = criarPilha()

print(pilha)
insereNaPilha(pilha, 8)
insereNaPilha(pilha, 9)
insereNaPilha(pilha, 10)
insereNaPilha(pilha, 11)
insereNaPilha(pilha, 12)
print(f"remover: {removeDaPilha(pilha)}")
print(f"remover: {removeDaPilha(pilha)}")
print(pilha)


# EXEMPLO DE DEC:


def criarDeque():
    return deque()


def insereNaPilha(pilha, elemento):
    pilha.append(elemento)


def removeDaPilha(pilha):
    return pilha.popleft()


pilha = criarDeque()

print(pilha)
insereNaPilha(pilha, 8)
insereNaPilha(pilha, 9)
insereNaPilha(pilha, 10)
insereNaPilha(pilha, 11)
insereNaPilha(pilha, 12)
print(f"remover: {removeDaPilha(pilha)}")
print(f"remover: {removeDaPilha(pilha)}")
print(pilha)


estudantes = {
    1: {'nome': 'Joana', 'idade': 45, 'curso': 'Computacao'},
    2: {'nome': 'Ivan', 'idade': 70, 'curso': 'Matematica'},
    3: {'nome': 'Jaqueline', 'idade': 12, 'curso': 'Computacao'}
}

cursos = {'Computacao', 'Matematica', 'Fisica'}

estudantes_cursos = {
    'Computacao': {1, 3},
    'Matematica': {2}
}


def adicionarEstudante(matricula, nome, idade, curso):
    pessoa = {'nome': nome, 'idade': idade, 'curso': curso}
    estudantes[matricula] = pessoa
    if curso not in estudantes_cursos:
        estudantes_cursos[curso] = set()
    estudantes_cursos[curso].add(matricula)


print(estudantes_cursos)
adicionarEstudante(5, 'Jao', 89, 'Computacao')
print(estudantes_cursos)
adicionarEstudante(6, 'Maria', 55, 'Fisica')
print(estudantes_cursos)


# print(f'Todas as pessoas matriculadas em algum curso: {estudantes_cursos['Matematica'] | estudantes_cursos['Computacao']} ')

# O metado GET() E MUITO FUNCIONAL PARA DICIONARIOS:
# pegar o estudante de matricula 1:
# estudante.get(1)
# output: {'nome': 'Joana', 'idade': 45, 'curso': 'Computacao' }
# opcao para nao dar erro em caso ele nao encontre o estudante:
# estudante.get(4, 'Estudante nao encontrado')
# p1 = estudantes.get(1)
# output: {'nome': 'Joana', 'idade': 45, 'curso': 'Computacao' }
# p1.keys() mostra quais sao as chaves do dicionario
# dict_keys(['nome', 'idade', 'curso'])
# p1.values()
# dict_values(['Joana', 45, 'Coomputacao'])
# p1.items()  - volta como uma tupla




print("For utilizando lista")
lista = [10, 15, 20, 25, 30]
for elemento in lista:
    print(elemento)

print()
print("For utilizando range")
for indice in range(len(lista)):
    print(f"indice {indice}: {lista[indice]}")

print()
print("For utilizando tupla")
tupla = (9, 8, 7, 6, 5)
for elemento in tupla:
    print(elemento)


print()
print("For utilizando dicionario - chave")
pessoa = {"nome": "Barbara", "idade": 30, "cidade": "Ashland"}
for chave in pessoa.keys():
    print(chave)

print()
print("For utilizando dicionario - valor")
for valor in pessoa.values():
    print(valor)

print()
print("For utilizando dicionario - chave: valor")
for chave, valor in pessoa.items():
    print(f"{chave}: {valor}")



#Gerenciador de tarefas:
def adicionar_tarefas(lista_tarefa, nome_tarefa):
    tarefa = {"Tarefa": nome_tarefa,  "Completada": False}  #Criamos um dicionario para pegar as chaves e valores
    lista_tarefa.append(tarefa)
    print(f"A tarefa '{nome_tarefa}' foi adicionada.")
    return


def visualizar_lista(lista_tarefa):
    print("Lista de tarefas")
    if not lista_tarefa:
        print("Nenhuma tarefa adicionada ainda.")
    else:
        for indice, tarefa in enumerate(lista_tarefa, start=1):
            status = "x" if tarefa["Completada"] else " "
            nome_tarefa = tarefa["Tarefa"]
            print(f"{indice}. [{status}] {nome_tarefa}")
    return


def atualizar_tarefa(indice_tarefa, lista_tarefa, novo_nome_tarefa):
    indice_ajustado = int(indice_tarefa) - 1
    if indice_ajustado >= 0 and indice_ajustado < len(lista_tarefa):
        lista_tarefa[indice_ajustado]["Tarefa"] = novo_nome_tarefa
        print(f"A tarefa de indice {indice_tarefa} foi atualizado para '{novo_nome_tarefa}'")
    else:
        print("Indice invalido!")
    return

def completar_tarefa(indice_tafera, lista_tarefa):
    indice_ajustado = int(indice_tarefa) - 1
    if indice_ajustado >= 0 and indice_ajustado < len(lista_tarefa):
        lista_tarefa[indice_ajustado]["Completada"] = True
        print(f"Tarefa {indice_tafera} marcada como completada")
    else:
        print("Indice invalido!")
    return

def deletar_tarefas_completadas(lista_tarefa):
    for tarefa in lista_tarefa:
        if tarefa ["Completada"] == True:
            lista_tarefa.remove(tarefa)
    print("Tarefas completadas foram deletadas")
    return

lista_tarefa = []  # If its inside of the looping, always will be erased

while True:
    print("\n Bem-vindo ao nosso Gerenciador de Tarefas")

    print("""
    1. Adicionar tarefas à lista
    2. Visualizar a lista de tarefas
    3. Atualizar o nome das tarefas
    4. Marcar tarefas como completas
    5. Deletar tarefas completadas
    6. Sair
    """)

    opcao = int(input("Digite o número da sua opção: "))

    
    if opcao == 1:
        nome_tarefa = input("Qual tarefa você deseja adicionar? ")
        adicionar_tarefas(lista_tarefa, nome_tarefa)

    elif opcao == 2:
        visualizar_lista(lista_tarefa)

    elif opcao == 3:
        visualizar_lista(lista_tarefa)

        indice_tarefa = input("Digite o indice da tarefa que deseja atualizar: ")
        novo_nome_tarefa = input("Digite o novo nome da tarefa: ")
        atualizar_tarefa(indice_tarefa, lista_tarefa, novo_nome_tarefa)

    elif opcao == 4:
        visualizar_lista(lista_tarefa)
        indice_tarefa = input("Digite o indice da tarefa que seja marcar como completada: ")
        completar_tarefa(indice_tarefa, lista_tarefa)

    elif opcao == 5:
        deletar_tarefas_completadas(lista_tarefa)
        visualizar_lista(lista_tarefa)

    elif opcao == 6:
        print("Até breve!")
        break  # This stops the loop

    else:
        print("Opção inválida! Digite um número de 1 a 6.")