class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
       # if the node is none then the list is empty
        if node is None:
            return
        # finds the last element in the list which points to None
        elif node.next_node is None:
            # if the node points to None set it to the head
            self.head = node
            # set the next node to the previous node
            node.next_node = prev
            return
        else:
            nxt = node.next_node
            node.next_node = prev
            self.reverse_list(nxt, node)

    def print_list(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next_node

# Tests 

# llist = LinkedList()
# llist.add_to_head(1)
# llist.add_to_head(2)
# llist.add_to_head(3)
# llist.add_to_head(4)
# llist.add_to_head(5)

# print(llist.print_list())
# llist.reverse_list(llist.head, None)
# print(llist.print_list())
