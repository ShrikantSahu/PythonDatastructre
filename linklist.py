# Hello World program in Python
    
class Node:
    def __init__(self,data=None,nextptr=None):
        self.data = data
        self.nextptr = nextptr
        

class LinkList:
    def __init__(self):
        self.head = None
    
    def AddNodeAtBeg(self,data):
        if self.head == None:
            n = Node(data,self.head)
            self.head = n
        else:
            n = Node(data,self.head)
            self.head = n
    
    def AddNodeAtSpecifiedIndex(self,index,data):
        if index < 0 or index >= self.getlengthlist():
            print("List index out of bound")
        
        if index == 0:
            self.AddNodeAtBeg(data)

        else:
            nodeitr = self.head
            indexcount = 0
            while nodeitr.nextptr:
                if indexcount == index - 1:
                    break
                indexcount += 1
                nodeitr = nodeitr.nextptr
            nodeitr.nextptr = Node(data,nodeitr.nextptr)

    def AddNodeAtEnd(self,data):
        if self.head == None:
            self.AddNodeAtBeg(data)
        
        else:
            nodeitr = self.head
            while nodeitr.nextptr:
                nodeitr = nodeitr.nextptr
                
            nodeitr.nextptr = Node(data,nodeitr.nextptr)
    
    def removeNodeAtSpecificIndex(self,index):
        if index < 0 or index >= self.getlengthlist():
            print("List index out of bound")

        if index == 0:
            nodeitr = self.head
            self.head = nodeitr.nextptr

        else:
            nodeitr = self.head
            counterindex = 0
            while nodeitr.nextptr:
                if counterindex == index - 1:
                    break
                counterindex += 1
                nodeitr = nodeitr.nextptr
            nodeitr.nextptr = nodeitr.nextptr.nextptr
            
    def deletelastnode(self):
        if self.head == None:
            print("Link list is empty") 
        else:
            nodeitr = self.head
            linklistlength = self.getlengthlist()
            countindex = 0 
            while nodeitr.nextptr:
                if countindex == linklistlength - 2:
                    break
                countindex += 1
                nodeitr = nodeitr.nextptr
            nodeitr.nextptr = None
             
            
    
            
    def getlengthlist(self):
        nodeitr = self.head
        count = 0
        while nodeitr:
            count += 1
            nodeitr = nodeitr.nextptr
            
        return count
            
    def printlist(self):
        if self.head == None:
            print("Link List is empty")
            
        else:
            nodeitr = self.head
            Nodelist = ''
            
            while nodeitr:
                Nodelist += nodeitr.data + '-->'
                nodeitr = nodeitr.nextptr
                
            print(Nodelist)
            
if __name__ == '__main__':
    ll = LinkList()
    ll.AddNodeAtBeg('6')
    ll.AddNodeAtBeg('3')
    ll.AddNodeAtBeg('2')
    ll.AddNodeAtEnd('5')
    ll.AddNodeAtEnd('7')
    ll.AddNodeAtEnd('10')
    ll.AddNodeAtEnd('8')
    ll.AddNodeAtSpecifiedIndex(0,'1')
    ll.AddNodeAtSpecifiedIndex(2,'9')
    ll.printlist()
    ll.removeNodeAtSpecificIndex(0)
    ll.printlist()
    ll.removeNodeAtSpecificIndex(2)
    ll.printlist()
    ll.deletelastnode()
    ll.printlist()
    