# -*-coding:Utf-8 -*

"""Ce module contient la classe Carte."""

def creer_labyrinthe_depuis_chaine(chaine):
    labyrinthe_l = chaine.splitlines()
    i = 0
    while i < len (labyrinthe_l):
        labyrinthe_l[i]=list(labyrinthe_l[i])
        i+=1
    return labyrinthe_l

def afficher_labyrinthe(labyrinthe_l):
    i = 0
    while i < len (labyrinthe_l):
        labyrinthe_l[i]="".join(labyrinthe_l[i])
        labyrinthe_l[i] +="\n"
        i+=1
    labyrinthe_c = "".join(labyrinthe_l)
    print(labyrinthe_c)

def get_robot_position(labyrinthe_l):
    i=0
    while i < len (labyrinthe_l):
        if 'X' in labyrinthe_l[i]:
            j = labyrinthe_l[i].index('X')
            return i,j
        i +=1
    return 0

class Carte:

    """Objet de transition entre un fichier et un labyrinthe."""

    def __init__(self, nom, chaine):
        self.nom = nom
        self.labyrinthe = creer_labyrinthe_depuis_chaine(chaine)
        #afficher_labyrinthe(self.labyrinthe)

    def __repr__(self):
        return "<Carte {}>".format(self.nom)

