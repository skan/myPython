# -*-coding:Utf-8 -*
import pickle
import os.path
import os
from carte import *

"""Ce fichier contient le code principal du jeu.

    Exécutez-le avec Python pour lancer le jeu.

    """
file_path= "savedGames/saved_game"
if os.path.exists(file_path):
    with open(file_path,'r') as f:
        my_depickler = pickle.Unpickler(f)
        loaded_card = my_depickler.load()
        if loaded_card.gameOver == 0:
            while 1:
                choice = raw_input  ("you have a game ongoing, do you want to load it y/n ?: ")
                if (choice.upper() =='Y'):
                    current_map = loaded_card
                if (choice.upper() =='N'):
                    break

try:
    current_map
except NameError:
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
    choice = int (input  ("please type the map you want to play: "))
    current_map = cartes[choice - 1]

current_map.display()
while current_map.gameOver == 0:
    move = raw_input("robot mouvement : ")
    current_map.move_robot(move)
    current_map.display()
    """ save the game """
    with open(file_path,'w') as f:
        my_pickler = pickle.Pickler(f)
        my_pickler.dump(current_map)

# Si il y a une partie sauvegardée, on l'affiche, à compléter

# ... Complétez le programme ...
