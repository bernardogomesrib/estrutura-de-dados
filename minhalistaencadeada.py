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
    
    def search(self,item):
        current = self.head
        while current.getData != item:
            current = current.getNext()
        if( current.getData == item):
            return current
        else:
            return None

    def remove(self,item):
        current = self.head
        found = False
        while current!=None:
            if(current.getData == item):
                auxprev = current.getPrevious()
                auxnext = current.getNext()
                auxprev.setNext(auxnext)
                del current
                found = True;
                self.size-=1
                break
            current = current.getNext()
        return found
    def pop(self,interator = -1):
        if(interator== -1):
            current = self.tail
            self.tail = self.tail.getPrevious()
            self.tail.setNext(None)
            self.size-=1
            data = current.getData()
            del current
            return data
        else:
            current = self.head
            for i in range(interator):
                current = current.getNext()
            try:
                deta = current.getData()
                current = current.getPrevious()
                self.size -=1
                return deta
            except:
               
                return "deuerroneh"


    def append(self,item,indice=0):
        side = None
        count = 0
        if indice == 0:
            self.head.setPrevious(Ponto(item,next=self.head,previous=None))
            self.size+=1
            self.head = self.head.getPrevious()
            return True
        elif indice == self.size-1:
            temp = Ponto(item,previous=self.tail)
            self.tail.setNext(temp)
            self.tail = temp
            self.size+=1
            return True
        elif 0< indice<self.size -1:
            if indice<= self.size/2:
                current = self.head
                side = +1
            elif indice> self.size/2:
                current = self.tail
                side = -1
            if(side<0):
                count = self.getSize()
            while count !=indice:
                
                if(side>0):
                    current = current.getNext()
                else:
                    current = current.getPrevious()
                count+=side
            aux = current.getPrevious()
            pt = Ponto(item,aux,current)
            aux.setNext(pt)
            current.setPrevious(pt)
            self.size +=1
            return True
        return False
    def get(self,local):
        current = self.head
        if(local == 0):
            return current.getData()
        for i in range(local):
            current = current.getNext()
            if current is None:
                return "Exception"
                break
        return current.getData()
    def remove(self,item):
        current = self.search(item)
        aux = current.getNext()
        aux2 = current.getPrevious()
        aux.setNext(aux2)
        aux2.setPrevious(aux)
        
    def printAll(self):
        current = self.head
        while True:
            try:
                print(current.getData(),end=" -> ")
                current = current.getNext()
            except:
                break
    
arr = ArrayList()
arr.add(1)
arr.add(2)
arr.add(3)
arr.add(4)
print(arr.append(69,2))
arr.printAll()
print()
print("agora era pra aparecer os caras")
print(arr.get(0))
print(arr.get(1))
print(arr.get(2))
print(arr.get(3))
print(arr.get(4))
print(arr.getSize())
print(arr.get(5))
arrrrrrr = arr.pop()
print(arrrrrrr)
print(arr.pop(2))