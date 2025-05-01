class HashTable:
    def __init__(self, capacity = 10):
        self.capacity = capacity
        self.table = [None for i in range(self.capacity)]
        
    def insert(self, key, value):