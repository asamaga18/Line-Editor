class Node:
    def __init__(self, data = None):
        self.prev = None
        self.data = data
        self.next = None

class DoublyLinkedList:

    def __init__(self):
        self.head = None
        self.length = 0

    
    def insertFirst(self, data):
        
        newNode = Node(data)
        newNode.next = self.head
        self.length = self.length + 1

        if self.head:
            self.head.prev = newNode
        
        self.head = newNode


    def insertLast(self, data):
        
        newNode = Node(data)
        self.length = self.length + 1

        if self.head is None:
            self.head =  newNode
            return

        currNode = self.head
        while (currNode.next != None):
            currNode = currNode.next
            
        currNode.next = newNode
        newNode.prev = currNode
        
    def getLength(self):
        return self.length
    
    def getHead(self):
        return self.head
    

    def printList(self):
        currNode = self.head
        while(currNode != None):
            print(currNode.data)
            currNode = currNode.next

