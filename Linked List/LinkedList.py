class Node:

    def __init__(self, data= None, next= None):
        self.data = data
        self.next = next
    
    def __repr__(self):
        return repr(self.data)

class LinkedList():

    def __init__(self):
        self.head = Node()
    
    def __repr__(self):
        nodes = []

        current_node = self.head.next
        while current_node:
            nodes.append(repr(current_node.data))
            current_node = current_node.next
        
        return ",".join(nodes)
    
    def prepend(self, data):

        node = Node(data, self.head.next)
        self.head.next = node
    
    def append(self, data):

        node = Node(data)

        if self.head.next is None:
            self.head.next = node
            return
        
        current_node = self.head.next
        
        while current_node.next:
            current_node = current_node.next
        
        current_node.next = node
    
    def search(self, item):
        
        current_node = self.head.next

        while current_node:
            if current_node.data == item:
                return current_node
            
            current_node = current_node.next
        
        return None
    
    def remove(self, item):

        previous_node = self.head
        current_node = self.head.next

        while current_node:
            if current_node.data == item:
                break

            previous_node = current_node
            current_node = current_node.next

        if current_node is None:

            return None
        
        if self.head == previous_node:
            # First node is current_node whose data is equal to item
            self.head.next = current_node.next
        else:
            previous_node.next = current_node.next
        
    
    def insert(self, data, new_data):
        
        current_node = self.head.next

        while current_node:
            if current_node.data == data:
                new_node = Node(new_data, current_node.next)
                current_node.next = new_node
            
            current_node = current_node.next



if __name__ == '__main__':
    li = LinkedList()
    li.append(5)
    li.append(10)
    print(li)
    li.prepend(1)
    print(li)
    print(li.search(5))
    print(li.search(50))
    li.append(50)
    print(li.search(50))
    li.remove(50)
    print(li)
    li.insert(5,6)
    print(li)
    li.remove(1)
    print(li)

    
