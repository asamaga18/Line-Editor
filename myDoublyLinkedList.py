class Node:
    def __init__(self, data = None):
        self.prev = None
        self.data = data
        self.next = None

    def getData(self):
        return self.data
    
    def isEdge(self):
        if ((self.prev == None) or (self.next == None) ):
            return True
        return False


class DoublyLinkedList:

    def __init__(self):
        # CHANGED: Create dummy nodes instead of None
        self.dummy_head = Node()  # Dummy head node
        self.dummy_tail = Node()  # Dummy tail node
        
        self.dummy_head.data = "BEGINNING"
        self.dummy_tail.data = "ENDING"
        
        # Connect dummy nodes
        self.dummy_head.next = self.dummy_tail
        self.dummy_tail.prev = self.dummy_head
        
        # Keep track of length
        self.length = 0

    
    def insertFirst(self, data):
        newNode = Node(data)
        self.length += 1

        newNode.next = self.dummy_head.next
        newNode.prev = self.dummy_head
        self.dummy_head.next.prev = newNode
        self.dummy_head.next = newNode




    def insertLast(self, data):
        newNode = Node(data)
        self.length += 1  # CHANGED: Used += operator

        newNode.prev = self.dummy_tail.prev
        newNode.next = self.dummy_tail
        self.dummy_tail.prev.next = newNode
        self.dummy_tail.prev = newNode
        
    def getLength(self):
        return self.length
    
    def getHead(self):
        if self.length > 0:
            return self.dummy_head.next
        return None
    
    def getTail(self):
        if self.length > 0:
            return self.dummy_tail.prev
        return None
        
    def getNext(self, node):
        if ((node != None) and (node != self.dummy_tail)):
            return node.next
        else:
            return node
        
    def getPrev(self, node):
        if ((node != None) and (node != self.dummy_head)):
            return node.prev
        else:
            return node

    def printList(self):
        currNode = self.dummy_head.next
        while(currNode != self.dummy_tail):
            print(str(currNode.data).strip())
            currNode = currNode.next
    
    
    def deleteNode(self, node):
    # Validation with specific error messages
        if not node:
            print("Error: Cannot delete None node")
            return False
        if node == self.dummy_head or node == self.dummy_tail:
            print("Error: Cannot delete dummy nodes")
            return False
            
        # Delete the node
        node.prev.next = node.next
        node.next.prev = node.prev
        self.length -= 1
        
        # Optional: clear the node's connections
        node.prev = None
        node.next = None
        
        return True

