class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
    
class LinkedList:

    def __init__(self):
        self.head = None
    
    def find(self, key):
        next_node = self.head

        # value not found
        if next_node is None:
            return None
        else:
            while next_node.next is not None:
                if next_node.key == key:
                    # return the found item
                    return next_node
                else:
                    next_node = next_node.next

        return next_node

    def insert_at_head(self, node):
        node.next = self.head
        self.head = node
        #Also updates

    def delete(self, key):
        if key == self.head.key:
            self.head = self.head.next
            return self.head
        prev = None
        curr = self.head
        while curr is not None:
            if curr.key == key:
                prev.next = curr.next
                return curr

            prev = curr
            curr = curr.next
        return None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        self.capacity = capacity
        self.buckets = [None] * capacity 
        self.number_of_items = 0


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        return self.capacity


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        return self.number_of_items / self.capacity


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        hash = 5381
        for c in key:
            hash = (hash * 33) + ord(c)
        return hash


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        hash_value = self.djb2(key)
        
        index = hash_value % self.capacity
        return index

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        if self.get_load_factor() >= 0.7:
            self.resize(self.capacity * 2)

        current = self.buckets[self.hash_index(key)]
            # search the linked list for a node with the same key as the one we are inserting
        
        if current is not None:
                # if it exist\
            new_list = LinkedList()           
            self.buckets[self.hash_index(key)] = new_list
            new_list.insert_at_head(HashTableEntry(key, value))
            self.number_of_items + 1
                    # return
        else:
            # if the new key/item doesn't exist, add it as a new head
            if current == None:
                current = (HashTableEntry(key, value))
                self.number_of_items += 1
            else:
                # change the current node to the new node
                current.insert_at_head(HashTableEntry(key, value))
            
                # if it doesn't exist do the following steps
                # the first item in the hasharray is the head of the linked list
        

                # create a new hashtableentry and add it to the head of the linked list
                # make the new entry the new head
        


    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # check to see if their is a key
        #if no key found print warning
        # else remove the value
        hash_index = self.hash_index(key)
        # search through the linked list until we find the node to delete
        # delete the node if found
        if self.buckets[hash_index] == None:
            print("Nothing in that slot")
        else:
            self.buckets[hash_index].value = None

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        current = self.buckets[self.hash_index(key)]
        

        if current is not None:
            # should return the node value
            return current.value
        else:
            # should return none
            return current


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Create a blank new array with double size of the old array
        old = self.buckets
        self.capacity = new_capacity
        self.buckets = [None] * self.capacity

        for i in old:
            if i is None:
                continue
            else:
                self.put(i.key, i.value)
        # rehase every single item because the hash function has changed
            # go through each slot in the array
                # rehase the key in each item and store in new array
            
            # make new array the new storage



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
    ht.get("")

    

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

 