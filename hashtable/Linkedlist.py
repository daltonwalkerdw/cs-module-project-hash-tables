class LinkedList:
    def __init__(self):
        self.head = None


    def add_new(self, node):
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node


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


    def delete(self, key):
        if self.head is None:
            print("There is nothing to delete")
        elif self.head.next is None:
            old = self.head
            self.head = None

            # might not need to return value
            return old
        else:
            old = self.head
            self.head = old.next

            # might not need to return value
            return old


    def change_value(self, key, node):
        next_node = self.head
        prev = None
        while next_node.next is not None:
            if next_node.key == key:
                next_node
                break
            else:
                prev = next_node
                next_node = next_node.next

        if next_node is not None:
            if prev is not None:
                prev.next = node
            else:
                self.head = node
        else:
            print("There is nothing to change")