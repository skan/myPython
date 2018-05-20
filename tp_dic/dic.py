class OrganizedDico():
    dicoKeys=[]
    dicoVal=[]

    def __init__(self,**dicoInputs):
        for key,value in dicoInputs.items():
            self.dicoKeys.append(key)
            self.dicoVal.append(value)

    def __repr__(self):
        dicoSize=len(self.dicoKeys)
        i=0
        output=""
        while i < dicoSize :
            message = ("{0} = {1} \n".format(self.dicoKeys[i],self.dicoVal[i]))
            output += message
            i+=1
        return output
    
    def sort(self):
        default_ValList = self.dicoVal[:]
        default_KeyList = self.dicoKeys[:]
        self.dicoVal.sort()
        i = 0
        for item in self.dicoVal:
            index = default_ValList.index(item)
            self.dicoKeys[i]=default_KeyList[index]
            i+=1

    def reverse(self):
        default_ValList = self.dicoVal[:]
        default_KeyList = self.dicoKeys[:]
        self.dicoVal.reverse()
        i = 0
        for item in self.dicoVal:
            index = default_ValList.index(item)
            self.dicoKeys[i]=default_KeyList[index]
            i+=1

    def len (self):
        return len(self.dicoKeys)

    def __getitem__(self,key):
        try:
            index = self.dicoKeys.index(key)
        except ValueError:
            return 0
        else:
            return self.dicoVal[index]
    
    def __setitem__(self,key,value):
        try:
            index = self.dicoKeys.index(key)
        except ValueError:
            self.dicoKeys.append(key)
            self.dicoVal.append(value)
        else:
            self.dicoVal[index] = value

    def __delitem__(self,key):
        try:
            index = self.dicoKeys.index(key)
        except ValueError:
            print ("the key {0} doesn't exist in our dictionnary".format(key))
            return 0
        else:
            del self.dicoKeys[index]
            del self.dicoVal[index]
    def __contains__ (self,key):
        try:
            index = self.dicoKeys.index(key)
        except ValueError:
            return False
        else:
            return True
    
    def __add__(self,otherDico):
        otherDico_size=len(otherDico.dicoKeys)
        i = 0
        while (i < otherDico_size):
            self.dicoKeys.append(otherDico.dicoKeys[i])
            self.dicoVal.append(otherDico.dicoVal[i])
            i+=1
    
    def __iadd__(self,otherDico):
        otherDico_size=len(otherDico.dicoKeys)
        i = 0
        while (i < otherDico_size):
            self.dicoKeys.append(otherDico.dicoKeys[i])
            self.dicoVal.append(otherDico.dicoVal[i])

            i+=1