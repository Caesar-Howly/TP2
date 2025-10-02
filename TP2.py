"""
Nom = Caesar
Gr = 407

Ce code est un jeu de chance ou le joueur devrait deviner le nombre que l'ordinateur a choisi par hasard entre les
nombres que le joueur a choisis.
"""


import random


game_begin = True
essaies = 0

lower_bound = 0
upper_bound = 100


def generate(min_value, max_value):
    global lower_bound
    global upper_bound
    choix_difficulty = input("Voulez-vous garder la difficulté défaute? o/n")

    if choix_difficulty == "o":
        lower_bound = min_value
        upper_bound = max_value
        print(f"J'ai choisi un numéro entre les nombres de votre choix.")
        print(f"Choisissez un nombre de {lower_bound} à {upper_bound}:")
    else:
        lower_bound = int(input("Choisissez votre premier nombre:"))
        upper_bound = int(input("Choisissez votre dernier nombre: "))
        print(f"J'ai choisi un numéro entre les nombres de votre choix.")
        print(f"Choisissez un nombre de {lower_bound} à {upper_bound}:")

generate(0, 100)


result = random.randint(lower_bound, upper_bound)


while game_begin:

    essaies += 1

    response = int(input())

    if response > result:
        print(f"{response} est trop grande. Essayez une autre fois:")

    elif response < result:
        print(f"{response} est trop petite. Essayez une autre fois:")

    else:
        print(f"Bravo! Vous avez eu la bonne réponse en {essaies} essaies.")
        continuer = input("Voulez-vous continuer? (o/n)")

        if continuer == "o":
            print("D'accord.")
            generate(0, 100)
            result = random.randint(lower_bound, upper_bound)
            essaies = 0

        else:
            game_begin = False


print("Au revoir!")
