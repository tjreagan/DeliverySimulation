# Thomas Reagan
# ID: 001265074

# Class structure for a basic hash table

class HashTable:
    # Constructor initializes an empty table with a size of the input list
    # O(n)
    def __init__(self, list):
        self.table = []
        self.capacity = len(list)
        for i in range(self.capacity):
            self.table.append([])

    # Function to determine a hash key
    # O(1)
    def get_hash(self, key):
        hash_key = hash(key) % self.capacity
        return hash_key

    # Function to insert an item, assigning a bucket using a hash key
    # O(1)
    def insert(self, key, value):
        bucket = self.get_hash(key)
        self.table[bucket].append([key, value])

    # Function to search for an item using its key
    # Worst case complexity would be O(n) depending on
    # the number of items in a bucket.
    def search(self, key):
        bucket = self.get_hash(key)
        if self.table[bucket]:
            bucket_list = self.table[bucket]
            for index, value in bucket_list:
                if index == key:
                    return value
                else:
                    return None

    # Function to remove an item using its key
    # O(1)
    def remove(self, key, value):
        bucket = self.get_hash(key)
        self.table[bucket].remove([key, value])