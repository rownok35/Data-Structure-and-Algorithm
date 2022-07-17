class Queue:

    def __init__(self):
        self.item = []
    def enqueue(self, item):
        self.item.append(item)

    def dequeue(self):
        return self.item.pop(0)
    
    def is_empty(self):
        return len(self.item) == 0

class CircularQueue():

    def __init__(self, size):
        self.items = [0] * size
        self.max_size = size
        self.head, self.tail, self.size = 0, 0, 0

    def enqueue(self, item):
        if self.is_full():
            print("Queue is full")
            return
        
        print("Inserting item", item)
        self.items[self.tail] = item
        self.tail = (self.tail + 1) % self.max_size
        self.size += 1

    def dequeue(self):
        item = self.items[self.head]
        self.head = (self.head + 1) % self.max_size
        self.size -= 1
        
        return item
    
    def is_empty(self):
        return self.size == 0
    
    def is_full(self):
        return self.size == self.max_size

        




if __name__ == '__main__':

    q = Queue()
    q.enqueue("Ron")
    q.enqueue("Sam")
    q.enqueue("Mim")

    while not q.is_empty():
        print(q.dequeue())

    a = CircularQueue(3)
    a.enqueue("Ron")
    a.enqueue("Sam")
    a.enqueue("Mim")
    a.enqueue("Liza")

    while not a.is_empty():
        print(a.dequeue())
    
    a.enqueue("Shaily")
    print(a.items)
    print(a.head)
    print(a.tail)


