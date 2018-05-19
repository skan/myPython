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