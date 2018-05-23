# -*-coding:Utf-8 -*

"""Ce fichier contient le code principal du jeu.

Exécutez-le avec Python pour lancer le jeu.

"""

import os

from carte import *

# On charge les cartes existantes
cartes = []
for nom_fichier in os.listdir("cartes"):
    if nom_fichier.endswith(".txt"):
        chemin = os.path.join("cartes", nom_fichier)
        nom_carte = nom_fichier[:-3].lower()
        with open(chemin, "r") as fichier:
            contenu = fichier.read()
            cartes.append (Carte(nom_carte,contenu))
            # Création d'une carte, à compléter

# On affiche les cartes existantes
print("Labyrinthes existants :")
for i, carte in enumerate(cartes):
    print("  {} - {}".format(i + 1, carte.nom))

choice = input  ("please type the map you want to play: ")
current_map = cartes[choice-1]
current_map.display()
while current_map.gameOver == 0:
    move = raw_input("robot mouvement : ")
    current_map.move_robot(move)
    current_map.display()

# Si il y a une partie sauvegardée, on l'affiche, à compléter

# ... Complétez le programme ...
