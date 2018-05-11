# coding=utf-8
import os
from random import randrange
from math import ceil

# Déclaration des variables de départ
argent = 1000 # On a 1000 $ au début du jeu
continuer_partie = True # Booléen qui est vrai tant qu'on doit
                        # continuer la partie

print("Hello, welcome ! you'll start playing with this amount:", argent, "$.")

while continuer_partie: # Tant qu'on doit continuer la partie
    # on demande à l'utilisateur de saisir le nombre sur
    # lequel il va miser
    nombre_mise = -1
    while nombre_mise < 0 or nombre_mise > 49:
        nombre_mise = input("Give us the number on which you wanna bet (from 0 to 49) : ")
        # On convertit le nombre misé
        try:
            nombre_mise = int(nombre_mise)
        except ValueError:
            print("Wrong value")
            nombre_mise = -1
            continue
        if nombre_mise < 0:
            print("Negative number")
        if nombre_mise > 49:
            print("Number greater than 49")

    # À présent, on sélectionne la somme à miser sur le nombre
    mise = 0
    while mise <= 0 or mise > argent:
        mise = input("What is your bet amount: ")
        # On convertit la mise
        try:
            mise = int(mise)
        except ValueError:
            print("You didn't gave us a number")
            mise = -1
            continue
        if mise <= 0:
            print("negative value.")
        if mise > argent:
            print("You don't have enough money baby. your walled contains: ", argent, "$")

    # Le nombre misé et la mise ont été sélectionnés par
    # l'utilisateur, on fait tourner la roulette
    numero_gagnant = randrange(50)
    print("Spinning spinning spinning .... ant the ball is on: ", numero_gagnant)

    # On établit le gain du joueur
    if numero_gagnant == nombre_mise:
        print("GOOOOOOOOOOOOOD !! the right nomber !! this is your gain: ", mise * 3, "$ !")
        argent += mise * 3
    elif numero_gagnant % 2 == nombre_mise % 2: # ils sont de la même couleur
        mise = ceil(mise * 0.5)
        print("GOOD: you bet on the righ color. You win: ", mise, "$")
        argent += mise
    else:
        print("Sorry friend. Not for this time. You lose your bet.")
        argent -= mise

    # On interrompt la partie si le joueur est ruiné
    if argent <= 0:
        print("Sorry, you have no more money. Game over.")
        continuer_partie = False
    else:
        # On affiche l'argent du joueur
        print("In your wallet now: ", argent, "$")
        quitter = input("Do you wanna leave (o/n) ? ")
        if quitter == "o" or quitter == "O":
            print("Thank you for playing with us.")
            continuer_partie = False

# On met en pause le système (Windows)
os.system("pause")