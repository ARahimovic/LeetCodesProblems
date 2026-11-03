class Node :
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList :
    def __init__(self):
        self.head = None

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def append(self, data):
        new_node = Node(data)

        if not self.head :
            self.head = new_node
            return 

        #else traverse the linked list to get last element    
        current = head
        while current.next != None :
            current = current.next
        
        current.next = new_node

    def delete(self, key) :
        if not head :
            return 
        
        current = head




