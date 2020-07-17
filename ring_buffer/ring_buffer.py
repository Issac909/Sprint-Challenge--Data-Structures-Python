class RingBuffer:
    def __init__(self, capacity):
        self.last_index = 0
        self.capacity = capacity
        self.container = []

    def append(self, item):
        if len(self.container) < self.capacity:
            self.container.append(item)
        
        else:
            self.container[self.last_index] = item
         
        self.last_index += 1 
        self.last_index = self.last_index % self.capacity

    def get(self):
        return self.container