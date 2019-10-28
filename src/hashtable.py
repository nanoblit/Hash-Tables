# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass


    def _hash_mod_storage(self, key, storage):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % len(storage)


    def _insert_storage(self, key, value, storage):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''
        # if value in position already exists
        element = storage[self._hash_mod_storage(key, storage)]
        if element:
            # loop until the same key found
            while True:
                # set the value to the new value
                if element.key == key:
                    element.value = value
                    break
                # if not found
                elif not element.next:
                    # add key and value at the end of the list
                    element.next = LinkedPair(key, value)
                    break
                else:
                    element = element.next
        # else
        else:
            # set key and value as the first element of the list
            storage[self._hash_mod_storage(key, storage)] = LinkedPair(key, value)


    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''
        self._insert_storage(key, value, self.storage)



    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        element = self.storage[self._hash_mod_storage(key, self.storage)]
        # if key is first in the list
        if element and element.key == key:
            # set the child of the element as the head
            self.storage[self._hash_mod_storage(key, self.storage)] = element.next
            # return
            return
        # else
        else:
            # Loop through the list
            while True:
                # if next element is None
                if not element or not element.next:
                    # print warning and return
                    print("Value is not present in the hash table")
                    return
                # if the next element has the correct key
                if element.next.key == key:
                    # set the child of that element as the child of the current element
                    element.next = element.next.next
                    # return
                    return
                element = element.next


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        element = self.storage[self._hash_mod_storage(key, self.storage)]
        # loop through elements at that index until element isn't None
        while element:
            # if key found
            if element.key == key:
                # return value
                return element.value
            element = element.next
        # return None
        return None


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        # set new capacity
        self.capacity *= 2
        # create new, larger storage
        new_storage = [None] * self.capacity
        # loop through the original list
        for element in self.storage:
            # loop through each element
            while element:
                # insert it to a new storage
                self._insert_storage(element.key, element.value, new_storage)
                element = element.next
        # set the new storage as the storage
        self.storage = new_storage
        



if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
