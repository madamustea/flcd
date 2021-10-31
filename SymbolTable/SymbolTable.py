
class SymTable():
    def __init__(self,size):
        self.nrElems=0
        self.sizeTable=size
        self.elems=[[] for _ in range(self.sizeTable)]
    def asciiFunction(self,k):
        sum=0
        for c in str(k):
            sum+=ord(c)
        return sum
    def hashFunction(self,key):
        return self.asciiFunction(key)%self.sizeTable
    def get(self,key):
        value=self.hashFunction(key)
        ind=0
        for elem in self.elems[value]:
            if elem==key:
                return (value,ind)
            ind+=1
        return False
    def alreadyExists(self,key):
        if self.get(key)==False:
            return False
        else:
            return True
    def getSize(self):
       return self.nrElems
    def insert(self,k):
        if self.alreadyExists(k):
            return self.get(k)
        value=self.hashFunction(k)
        self.elems[value].append(k)
        self.nrElems+=1
        return self.get(k)