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
