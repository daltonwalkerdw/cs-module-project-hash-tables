from Linkedlist import LinkedList

class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.table = [None] * capacity
        self.count = 0

    def get_num_slots(self):
        return self.capacity


    def get_load_factor(self):
        return self.count / self.capacity # current occupied buckets / capacity


    # not doing this one
    def fnv1(self, key):
        pass


    def djb2(self, key):
        hash_value = 5381
        for x in key:
            hash_value = ((hash_value << 5) + hash_value) + ord(x)
        return hash_value


    def hash_index(self, key):
        return self.djb2(key) % self.capacity


    def put(self, key, value):
        # resize if needed
        if self.get_load_factor() >= 0.7:
            self.resize(self.capacity * 2)

        # bucket being added to
        current = self.table[self.hash_index(key)]

        # for adding new list to empty bucket
        if current is None:
            new_list = LinkedList()
            self.table[self.hash_index(key)] = new_list
            new_list.add_new(HashTableEntry(key, value))
            self.count += 1
        # if there is already a list
        else:
            # if the new key/item doesn't exist, add it as a new head
            if current.find(key) == None:
                current.add_new(HashTableEntry(key, value))
                self.count += 1
            else:
                # change the current node to the new node
                current.change_value(key, HashTableEntry(key, value))


    def delete(self, key):
        current = self.table[self.hash_index(key)]

        # prints a message if it doesn't exist
        current.delete(key)


    def get(self, key):
        current = self.table[self.hash_index(key)]
        item = current.find(key)

        if item is not None:
            # should return the node value
            return item.value
        else:
            # should return none
            return item


    def resize(self, new_capacity):
        old = self.table
        self.capacity = new_capacity
        self.table = [None] * self.capacity

        for i in old:
            if i is None:
                continue
            else:
                self.put(i.head.key, i.head.value)



if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"), "SHOULD RETURN POEM")

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")

 