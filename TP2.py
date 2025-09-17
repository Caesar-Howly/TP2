import random


game_begin = True
essaies = 1
result = random.randint(0, 10)

while game_begin:

    x = int(input("Choisissez un nombre de 0 a 10:"))

    if x > result:
        print("Le nombre est trop grande. essayez une autre fois:")
        essaies += 1
    elif x < result:
        print("Le nombre est trop petite. Essayez une autre fois:")
        essaies += 1
    else:
        print(f"Bravo! Vous avez eu la bonne réponse en {essaies} essaies.")
        quitter = input("Voulez-vous continuer? (o/n)")

        if quitter == "o":
            print("ok")

        else:
            game_begin = False


print("ok bye")

