class HashTable:
    # Chaining Hash Table comprised of a "list of lists"
    def __init__(self, capacity = 10):

        # Capacity of table set to 'capacity' parameter - default is 10
        self.capacity = capacity

        # Initialize hash table as empty list
        self.table = []

        # For every item in capacity, initialize an empty list to act as a bucket for hashing
        for i in range(self.capacity):
            self.table.append([])

    # Hashing function intended to sort each item into correct bucket
    def hash(self, key):
        # Returns correct bucket for item based on size of hash table, will update with size of table
        return key % self.capacity

    # Insert an item based on key into lookup table
    def insert(self, key, item):

        # Use hash function defined previously to identify index of correct bucket
        index = self.hash(key)

        # For each key-item pair, if key exists, update current item
        for kv in self.table[index]:
            if kv[0] == key:
                kv[1] = item
                return

        # If key does not exist, append key-item pair to bucket-list
        self.table[index].append(key, item)


    # Implement search function with key as parameter
    def search(self, key):

        # Identify index of correct bucket
        index = self.hash(key)

        # Iterate through bucket-list to find item
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        # Return None if key does not exist in index
        return None

    def delete(self, key):
        # Use search function to identify correct index of bucket
        index = self.hash(key)

        # Find and delete item - return if found
        for i in range(self.table[index]):
            if self.table[index][i][0] == key:
                del(self.table[index][i])
                return
        # Indicate to user that item was not found with given key
        print("Key not found")
