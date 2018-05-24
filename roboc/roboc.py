# -*-coding:Utf-8 -*
import pickle
import os.path
import os
from carte import *

# check if there is a saved game
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
                    break
                if (choice.upper() =='N'):
                    break

# Propose map selection if no game loaded
try:
    current_map
except NameError:
    # Load all cartes folder content
    cartes = []
    for nom_fichier in os.listdir("cartes"):
        if nom_fichier.endswith(".txt"):
            chemin = os.path.join("cartes", nom_fichier)
            nom_carte = nom_fichier[:-3].lower()
            with open(chemin, "r") as fichier:
                contenu = fichier.read()
                cartes.append (Carte(nom_carte,contenu))

    # Display existing cards
    print("Existing labyrinths :")
    for i, carte in enumerate(cartes):
        print("  {} - {}".format(i + 1, carte.nom))
    while 1:
        try :
            choice = int (raw_input  ("please type the map you want to play: "))
            if choice < (len(cartes) + 1):
                current_map = cartes[choice - 1]
                break
        except ValueError:
            print ("this is not an int")
        # Star of the game 
current_map.display()
while current_map.gameOver == 0:
    move = raw_input("robot mouvement : ")
    current_map.move_robot(move)
    """ save the game """
    current_map.display()
    with open(file_path,'w') as f:
        my_pickler = pickle.Pickler(f)
        my_pickler.dump(current_map)

