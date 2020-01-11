from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if self.storage.length < self.capacity:
            self.storage.add_to_tail(item)
            self.current = self.storage.head
        else:
            # if an item needs to be deleted, it is the head.
            delete = self.storage.head
            self.storage.remove_from_head()
            self.storage.add_to_tail(item)

            if delete == self.current:
                self.current = self.storage.tail

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        first = self.current  # keep track of first node so no duplicates
        list_buffer_contents.append(first.value)

        node = first  # Changing node
        if node.next is not None:
            node = node.next
        else:
            node = self.storage.head

        while node is not first:
            list_buffer_contents.append(node.value)
            if node.next is not None:
                node = node.next
            else:
                node = self.storage.head

        return list_buffer_contents


# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
