class Ponto:
    def __init__(self,novo,previous = None,next = None):
        self.Data = novo
        self.previous = previous
        self.next = next
    def getData(self):
        return self.Data
    def setData(self,info):
        self.Data = info
    def getPrevious(self):
        return self.previous
    def setPrevious(self,info):
        self.previous = info
    def getNext(self):
        return self.next
    def setNext(self,info):
        self.next = info
class ArrayList:
    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None
    def isEmpty(self):
        return self.head == None
    def add(self,info):
        info = Ponto(info,previous=self.tail)
        if(self.isEmpty()):
            self.head = info
            self.tail = info            
        else:
            self.tail.setNext(info)
            self.tail = info
        self.size+=1
    def getSize(self):
        return self.size
    def remove(self,item):
        #item = Ponto(item)
        current = self.head
        found = False
        while current!=None:
            if(current.getData == item):
                auxprev = current.getPrevious()
                auxnext = current.getNext()
                auxprev.setNext(auxnext)
                del current
                found = True;
                break
            current = current.getNext()
        return found
    
    

            
    
