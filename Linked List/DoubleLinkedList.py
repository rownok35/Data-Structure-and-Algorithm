class Node:

    def __init__(self, data= None, prev = None, next= None):
        self.data = data
        self.prev = prev
        self.next = next
    
    def __repr__(self):
        return repr(self.data)

class DoubleLinkedList():

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

        first_node = self.head.next
        new_node = Node(data, None, first_node)
        self.head.next = new_node

        if first_node:
            first_node.prev = new_node

    
    def append(self, data):

        node = Node(data)

        if self.head.next is None:
            self.head.next = node
            return
        
        current_node = self.head.next
        
        while current_node.next:
            current_node = current_node.next
        
        current_node.next = node
        node.prev = current_node
    
    def search(self, item):
        
        current_node = self.head.next

        while current_node:
            if current_node.data == item:
                return current_node
            
            current_node = current_node.next
        
        return None
    
    def remove_node(self, node):

        if node.prev:
            node.prev.next = node.next
        else:
            self.head.next = node.next
        
        if node.next:
            node.next.prev = node.prev

    def remove(self, item):

        node = self.search(item)

        if node is None:
            return
        
        self.remove_node(node)
        
    




if __name__ == '__main__':
    li = DoubleLinkedList()
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
    li.remove(1)
    print(li)

    
