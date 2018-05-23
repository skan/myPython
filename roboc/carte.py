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
        self.isDoor = 0
        self.gameOver = 0

    def __repr__(self):
        return "<Carte {}>".format(self.nom)

    def display(self):
        i = 0
        labyrinthe_l = self.labyrinthe[:]
        while i < len (labyrinthe_l):
            labyrinthe_l[i]="".join(labyrinthe_l[i])
            labyrinthe_l[i] +="\n"
            i+=1
        labyrinthe_c = "".join(labyrinthe_l)
        print(labyrinthe_c)
    
    def get_robot_position(self):
        y=0
        while y < len (self.labyrinthe):
            if 'X' in self.labyrinthe[y]:
                x = self.labyrinthe[y].index('X')
                return x,y
            y +=1
        return 0
    
    def get_map_situation(self,x,y):
        return self.labyrinthe[y][x]
    
    def move_x(self,old_position,new_position):
        old_x = old_position[0]
        old_y = old_position[1]
        new_x = new_position[0]
        new_y = new_position[1]

        if self.labyrinthe[new_y][new_x] != "O": 
            if self.labyrinthe[new_y][new_x] == "U":
                print ("You win ! congrats")
                self.gameOver = 1 
            if self.isDoor == 1:
                self.labyrinthe[old_y][old_x] = "."
                self.isDoor = 0 
            else:
                self.labyrinthe[old_y][old_x] = " "
            if self.labyrinthe[new_y][new_x] == ".":
                self.isDoor = 1
            self.labyrinthe[new_y][new_x] = 'X'
            
    def update_map(self, movement):
        x,y = self.get_robot_position()
        if movement == "S":
            new =(x,y+1)
        elif movement == "N":
            new =(x,y-1)
        elif movement == "E":
            new =(x+1,y)
        elif movement == "O":
            new =(x-1,y)
        self.move_x((x,y),new)
