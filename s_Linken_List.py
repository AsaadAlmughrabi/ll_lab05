from Node import Node

class LinkedList:
    def __init__(self):
        """Initialize an empty LinkedList."""
        self.head = None

    def append(self, value):
        """Add a node with the given value at the end of the LinkedList."""
        node = Node(value)
        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = node

    def delete_node(self, key):
        """
        Delete the node with the given value from the LinkedList.

        Returns:
        - True if the node is found and deleted, False otherwise.
        """
        temp = self.head

        if temp is None:
            return False

        if temp is not None and temp.value == key:
            self.head = temp.next
            temp = None
            return True

        while temp is not None:
            if temp.value == key:
                break
            prev = temp
            temp = temp.next

        if temp is None:
            return False

        prev.next = temp.next
        temp = None
        return True

    def __len__(self):
        """Return the number of nodes in the LinkedList."""
        length = 0
        temp = self.head
        while temp:
            length += 1
            temp = temp.next
        return length

    def __str__(self):
        """Return a string representation of the LinkedList."""
        temp = self.head
        string = ""
        while temp:
            string += str(temp.value) + "-->"
            temp = temp.next
        return string

    def __getitem__(self, index):
        """
        Return the value of the node at the given index.
    
        Raises:
        - IndexError if the index is out of range.
        """
        temp = self.head
        current_index = 0
        while temp:
            if current_index == index:
                return temp.value
            current_index += 1
            temp = temp.next

        raise IndexError("Index out of range") 
