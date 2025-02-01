class Node:
    def __init__(self, data = None):
        self.prev = None
        self.data = data
        self.next = None

    def getData(self):
        return self.data


    def deleteNode(self):
        # Case 1: If this is the head node (no previous node)
        if self.prev is None:
            print("attempting to delete head\n")
            if self.next:
                self.next.prev = None
                return self.next
            return None  # If it's the only node
        
        # Case 2: If this is the last node
        if self.next is None:
            self.prev.next = None
            temp = self.prev
            self.prev = None  # ADDED: Clear connection
            return temp
        
        # Case 3: If node is in the middle
        self.prev.next = self.next
        self.next.prev = self.prev
        temp = self.prev
        
        # ADDED: Clear connections
        self.prev = None
        self.next = None
        
        if temp.prev is None:
            return temp.next
        return temp
    
    def isEdge(self):
        if ((self.prev == None) or (self.next == None) ):
            return True
        return False


class DoublyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    
    def insertFirst(self, data):
        newNode = Node(data)
        self.length += 1

        if self.head is None:
            self.head = newNode
            self.tail = newNode
            return

        newNode.next = self.head
        self.head.prev = newNode
        self.head = newNode



    def insertLast(self, data):
        newNode = Node(data)
        self.length += 1  # CHANGED: Used += operator

        if self.head is None:  # ADDED: Empty list case
            self.head = newNode
            self.tail = newNode
            return

        # CHANGED: Use tail pointer instead of traversing
        self.tail.next = newNode
        newNode.prev = self.tail
        self.tail = newNode
        
    def getLength(self):
        return self.length
    
    def getHead(self):
        return self.head
    
    def getTail(self):
        return self.tail

    def printList(self):
        currNode = self.head
        while(currNode != None):
            print(str(currNode.data).strip())
            currNode = currNode.next
    
    def deleteNode(self, node):
        if node == self.head:
            self.head = node.next

        if node == self.tail:
            self.tail = node.prev

        self.length -= 1

