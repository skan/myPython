class OrganizedDico():
    def __init__(self,*copyDico, **dicoInputs):
        self.dicoKeys=[]
        self.dicoVal=[]
        for key,value in dicoInputs.items():
            self.dicoKeys.append(key)
            self.dicoVal.append(value)
        
        for dico in copyDico:
            if isinstance(dico, OrganizedDico):
                self += dico
            else:
                raise TypeError ("not a dico object")

    def __repr__(self):
        dicoSize=len(self.dicoKeys)
        i=0
        output=""
        while i < dicoSize :
            message = ("{0} = {1} \n".format(self.dicoKeys[i],self.dicoVal[i]))
            output += message
            i+=1
        return output
    
    def __str__(self):
        return repr(self)
    
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
            raise ValueError ("the key {0} doesn't exist in our dictionnary".format(key))
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
        resultatAddition = OrganizedDico()
        resultatAddition.dicoKeys=self.dicoKeys[:]
        resultatAddition.dicoVal=self.dicoVal[:]

        otherDico_size=len(otherDico.dicoKeys)
        i = 0
        while (i < otherDico_size):
            if (otherDico.dicoKeys[i] in self.dicoKeys):
                key = otherDico.dicoKeys[i]
                resultatAddition[key]+=otherDico.dicoVal[i]
            else:
                resultatAddition.dicoKeys.append(otherDico.dicoKeys[i])
                resultatAddition.dicoVal.append(otherDico.dicoVal[i])
            i+=1
        return resultatAddition
    
    def __iadd__(self,otherDico):
        otherDico_size=len(otherDico.dicoKeys)
        i = 0
        while (i < otherDico_size):
            if (otherDico.dicoKeys[i] in self.dicoKeys):
                key = otherDico.dicoKeys[i]
                self[key]+=otherDico.dicoVal[i]
            else:
                self.dicoKeys.append(otherDico.dicoKeys[i])
                self.dicoVal.append(otherDico.dicoVal[i])
            i+=1
        return self
    
    def __iter__ (self):
        self.dicoSize=len(self.dicoKeys)
        self.i = 0
        return self

    def next(self):
        if (self.i < self.dicoSize):
            result = (self.dicoKeys[self.i] ,self.dicoVal[self.i])
            self.i +=1
            return result
        else:
            raise StopIteration
    
    def keys(self):
        i = 0
        dicoSize=len(self.dicoKeys)
        while (i < dicoSize):
            yield self.dicoKeys[i] 
            i +=1
    
    def values(self):
        i = 0
        dicoSize=len(self.dicoKeys)
        while (i < dicoSize):
            yield self.dicoVal[i] 
            i +=1

    def items(self):
        i = 0
        dicoSize=len(self.dicoKeys)
        while (i < dicoSize):
            yield self.dicoKeys[i] , self.dicoVal[i]
            i +=1