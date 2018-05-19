class OrganizedDico():
    dicoKeys=[]
    dicoVal=[]
    def __init__(self,**dicoInputs):
        print("init dico")
        for key,value in dicoInputs.items():
            self.dicoKeys.append(key)
            self.dicoVal.append(value)