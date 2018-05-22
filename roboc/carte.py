# -*-coding:Utf-8 -*

"""Ce module contient la classe Carte."""

def creer_labyrinthe_depuis_chaine(chaine):
    labyrinthe_l = chaine.splitlines()
    i = 0
    while i < len (labyrinthe_l):
        labyrinthe_l[i]=list(labyrinthe_l[i])
        i+=1
    return labyrinthe_l


class Carte:

    """Objet de transition entre un fichier et un labyrinthe."""

    def __init__(self, nom, chaine):
        self.nom = nom
        self.labyrinthe = creer_labyrinthe_depuis_chaine(chaine)

    def __repr__(self):
        return "<Carte {}>".format(self.nom)

