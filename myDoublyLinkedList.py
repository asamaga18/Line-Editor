class myDoublyLinkedList:

    class Node:
        prev = None
        next = None
        data = None

        def __init__(self, data, prev, next):
            self.prev = prev
            self.data = data
            self.next = next

        def __str__(self):
            if (data == None):
                print("Data is None")

            else:
                print(data)

    
    head = None

    def __init__(self, data):
        pass

