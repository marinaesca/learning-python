# marinaescalante-unfinished

# using bradyz template, mostly learning not my code

class LinkedListNode:
    def __init__(self, value, pointer=None):
        self.value = value
        self.pointer = pointer

    def __str__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, value):
        if self.head is None:
        	self.head = LinkedListNode(value)
        else:
        	current = self.head
        	while current.pointer is not None:
        		current = current.pointer
        	current.pointer = LinkedListNode(value)

    def remove(self, value):
        # do something to show error when trying to remove when head none?
        if self.head.value == value:
            current = self.head.pointer
            self.head = current
        else:
            current = self.head
            while current.pointer is not None:
                if current.pointer.value == value:
                    pointerNext = current.pointer.pointer
                    current.pointer.value = None
                    current.pointer.pointer = None
                    current.pointer = pointerNext

                current = current.pointer

    def removeAll(self, value):
        while (self.contains(value) == True):
            self.remove(value)

    def contains(self, value):
        current = self.head
        while current is not None:
            if current.value == value:
                return True;
            current = current.pointer

        return False

    def __str__(self):
        # No need to mess with this function -
        # Really important to understand.
        node_strings = list()

        # Go through all the nodes and gather the string representations.
        current = self.head
        while current is not None:
            node_strings.append(str(current))
            current = current.pointer

        return "->".join(node_strings)


if __name__ == "__main__":
    ll = LinkedList()
    ll.head = LinkedListNode(1)
    ll.head.pointer = LinkedListNode(2)
    ll.head.pointer.pointer = LinkedListNode(3)

    print(ll)

