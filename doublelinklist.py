# Hello World program in Python
    
class Node:
    def __init__(self,data=None):
        self.data = data
        self.nextptr = None
        self.prevptr = None

class DoubleLinkList:
    def __init__(self):
        self.head = None
    
    def AddNodeAtBeg(self,data):
        if self.head == None:
            n = Node(data)
            self.head = n
        else:
            currentnode = self.head
            n = Node(data)
            n.prevptr = None
            n.nextptr = self.head
            self.head = n
            currentnode.prevptr = self.head
            
    def AddNodeAtEnd(self,data):
        if self.head == None:
            self.AddNodeAtBeg(data)
        else:
            nodeitr = self.head
            
            while nodeitr.nextptr:
                nodeitr = nodeitr.nextptr
            
            node = Node(data)
            nodeitr.nextptr = node
            node.prevptr = nodeitr

    def deletelastnode(self):
        if self.head == None:
            print("No node to delete")  
        else:
            nodeitr = self.head
            count = 0
            while nodeitr.nextptr:
                if count == self.getlengthlist() - 2:
                    break
                count += 1
                nodeitr = nodeitr.nextptr     


            nodeitr.nextptr = None

    def AddNodeAtSpecifiedIndex(self,index,data):
        if index == 0:
            self.AddNodeAtBeg(data)

        elif index == self.getlengthlist() - 1:
            self.AddNodeAtEnd(data)

        else:
            nodeitr = self.head
            count = 0
            while nodeitr.nextptr:
                if count == index - 1:
                    break
                count += 1
                nodeitr = nodeitr.nextptr
            
            node = Node(data)
            node.nextptr = nodeitr.nextptr
            node.prevptr = nodeitr
            nodeitr.nextptr =node
            nodeitr.nextptr.nextptr.prevptr = node
            


    def removeNodeAtSpecificIndex(self,index):
        if self.head == None:
            print("List is empty")

        if index == 0:
            self.head = self.head.nextptr
            self.head.prevptr = None

        
        elif index == self.getlengthlist() - 1:
            self.deletelastnode()
            
            
        else:
            nodeitr = self.head
            count = 0
            while nodeitr.nextptr:
                if count == index - 1:
                    break
                count += 1
                nodeitr = nodeitr.nextptr
            nodeitr.nextptr = nodeitr.nextptr.nextptr
            nodeitr.nextptr.nextptr.prevptr = nodeitr
            
            
            
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
            print(nodeitr.data)
            Nodelist = ''
            
            while nodeitr:
                Nodelist += nodeitr.data + '-->'
                nodeitr = nodeitr.nextptr
                
            print(Nodelist)
            
if __name__ == '__main__':
    ll = DoubleLinkList()
    ll.AddNodeAtBeg('6')
    ll.AddNodeAtBeg('3')
    ll.AddNodeAtBeg('2')
    ll.AddNodeAtEnd('5')
    ll.AddNodeAtEnd('7')
    ll.AddNodeAtEnd('10')
    ll.AddNodeAtEnd('8')
    ll.printlist()
    ll.AddNodeAtSpecifiedIndex(0,'1')
    ll.AddNodeAtSpecifiedIndex(2,'9')
    ll.printlist()
    ll.removeNodeAtSpecificIndex(0)
    ll.printlist()
    ll.removeNodeAtSpecificIndex(2)
    ll.printlist()
    ll.deletelastnode()
    ll.printlist()
    ll.removeNodeAtSpecificIndex(3)
    ll.printlist()
    ll.AddNodeAtEnd('7')
    ll.AddNodeAtBeg('6')
    ll.printlist()
    