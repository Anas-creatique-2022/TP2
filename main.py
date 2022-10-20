#tp2 Anas Siah
#13

#importerr la variable random dans le  code
import random

# variable pour savoir le nombre d'essai effectuer

nb_essai = 0

#variable qui permet de choisir  la borne maximal et minimum
nombre_minimum = int(input("Choisissez la borne minimale du jeu: "))
nombre_maximum = int(input("Choisissez la borne maximale du jeu: "))
chiffre_aleatoire = random.randint(nombre_minimum, nombre_maximum)
print("J'ai choisi un nombre entre",nombre_minimum,"et", nombre_maximum)


#la boucle dans la boucle pour savoir si le joueur veut recomencer et pour qu'il devine le nombre



jouer = True
while jouer:
    while (essai := int(input("trouvez ce nombre"))) != chiffre_aleatoire:
        nb_essai += 1
        if essai < chiffre_aleatoire:
            print("Mauvaise réponse, le nombre superieure ")

        elif essai > chiffre_aleatoire:
            print("Mauvaise réponse, le nombre est infereieure ")

    print("Bonne réponse! tu as réussi en ", nb_essai, " essais")
    rejouer = input("veut tu rejouer")
    if rejouer == "oui":
        jouer = True
    elif rejouer == "non":
        jouer = False


#fin du code









