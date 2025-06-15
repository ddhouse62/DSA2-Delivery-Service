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
        bucket = self.hash(key)


        # For each key-item pair, if key exists, update current item
        for kv in self.table[bucket]:
            if kv[0] == key:
                kv[1] = item
                return

        # If key does not exist, append key-item pair to bucket-list
        kv = [key, item]
        self.table[bucket].append(kv)



    # Implement search function with key as parameter
    def search(self, key):

        # identify index of correct bucket
        bucket = self.hash(key)
        # Return value if key exists in bucket
        for kv in self.table[bucket]:
            if kv[0] == key:
                return kv[1]
        # Return None if key does not exist in bucket
        return None

    def delete(self, key):
        # identify item to remove
        bucket = self.hash(key)

        # Find and delete item - return if found
        for kv in self.table[bucket]:
            if kv[0] == key:
                self.table[bucket].remove(kv)
                print(f"Item {key} removed from table")
                return
        # Indicate to user that item was not found with given key
        print("key not found")

    # Package Lookup function, takes key as input, passes time value previously identified to show stats for package
    # Utilizes existing search function to pass package
    def lookup(self, key, time = (17, 0)):
        package = self.search(key)
        return package.get_package_stats(time)
