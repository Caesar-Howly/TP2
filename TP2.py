"""
Nom = Caesar
Gr = 407

Ce code est un jeu de chance ou le joueur devrait deviner le nombre que l'ordinateur a choisi par hasard entre les
nombres que le joueur a choisis.
"""


import random


game_begin = True
essaies = 0

first = 0
last = 100


def generate():
    global first
    global last
    difficulty = str(input("Voulez-vous garder la difficulté défaute? o/n"))

    if difficulty == "o":
        print(f"J'ai choisi un numéro entre les nombres de votre choix. Choisissez un nombre de {first} à {last}:")
    else:
        first = int(input("Choisissez votre premier nombre:"))
        last = int(input("Choisissez votre dernier nombre: "))
        print(f"J'ai choisi un numéro entre les nombres de votre choix. Choisissez un nombre de {first} à {last}:")


generate()


result = random.randint(first, last)


while game_begin:

    essaies += 1

    x = int(input())

    if x > result:
        print(f"{x} est trop grande. Essayez une autre fois:")

    elif x < result:
        print(f"{x} est trop petite. Essayez une autre fois:")

    else:
        print(f"Bravo! Vous avez eu la bonne réponse en {essaies} essaies.")
        continuer = input("Voulez-vous continuer? (o/n)")

        if continuer == "o":
            print("D'accord.")
            generate()
            result = random.randint(first, last)
            essaies = 0

        else:
            game_begin = False


print("Au revoir!")
