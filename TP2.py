"""
Nom = Caesar
Gr = 407

Ce code est un jeu de chance ou le joueur devrait deviner le nombre que l'ordinateur a choisi par hasard de 0-1000.
"""


import random


game_begin = True
essaies = 0
#result = random.randint(0, 100)

#input("Choissisez la difficulté du jeu: Facile, Moyenne, Difficile ( Ecrivez le premier lettre en MAJUSCULE")


#if input() == "Facile":
   # random.randint(0, 100)
#elif input() == "Moyenne":
    #random.randint(0, 1000)
#elif input() == "Difficile":
   # random.randint(0, 10000)

def gener(x,y):
    answer = random.randint(x, y)
    return answer


first = int(input("first number"))
last = int(input("last number"))


result = gener(first, last)


while game_begin:

    essaies += 1

    x = int(input("Choisissez un nombre de 0 a 1000:"))

    if x > result:
        print(f"{x} est trop grande. essayez une autre fois:")

    elif x < result:
        print(f"{x} est trop petite. Essayez une autre fois:")

    else:
        print(f"Bravo! Vous avez eu la bonne réponse en {essaies} essaies.")
        quitter = input("Voulez-vous continuer? (o/n)")

        if quitter == "o":
            print("ok")
            #result = random.randint(0, 100)
            first = int(input("first number"))
            last = int(input("last number"))

            result = random.randint(first, last)
            essaies = 0

        else:
            game_begin = False


print("ok bye")
