from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # Checks if DLL is empty --> true, then add to head and current becomes the head
        if self.storage.length == 0:
            self.storage.add_to_head(item)
            self.current = self.storage.head
            return

        # If the DLL is at the capacity, overwrite the oldest value (current.next)
        if self.storage.length == self.capacity:
            # If the current is the tail, overwrite the head
            if self.current == self.storage.tail:
                self.storage.head.value = item
                self.current = self.storage.head
            # Else if the current.next exists, overwrite current.next
            else:
                self.current.next.value = item
                self.current = self.current.next
            # Else if the storage is not at capacity, add the value to tail
        else:
            self.storage.add_to_tail(item)
            self.current = self.storage.tail


    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        selection = self.storage.head

        # TODO: Your code here
        if selection == None:
            return list_buffer_contents

        while selection:
            list_buffer_contents.append(selection.value)
            selection = selection.next

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
