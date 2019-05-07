
class Node:
    def __init__(self, data = None, prev = None, next = None):
        self.data = data
        self.prev = prev
        self.next = next

class DLL:
    def __init__(self):
        self.sentinel = Node()
        self.sentinel.next = self.sentinel
        self.sentinel.prev = self.sentinel
        self.curr = self.sentinel
        self.size = 0

    def insert(self, data):
        node = Node(data, self.curr.prev, self.curr)
        node.prev.next = node
        node.next.prev = node
        self.curr = node
        self.size += 1

    def remove(self):
        if self.size == 0 or self.size == 1:
            self.__init__()
        else:
            prev = self.curr.prev
            next = self.curr.next
            if not next is self.sentinel:
                next.prev = prev
                self.curr = next
                if not prev is self.sentinel:
                    prev.next = next
            else:
                prev.next = next
                self.curr = prev
            self.size -= 1

    def move_to_next(self):
        if not self.curr.next is self.sentinel:
            self.curr = self.curr.next

    def move_to_prev(self):
        if not self.curr.prev is self.sentinel:
            self.curr = self.curr.prev

    def __len__(self):
        return self.size

    def __str__(self):
        ret_str = ""
        node = self.sentinel.next
        while node != self.sentinel:
            ret_str += str(node.data) + " "
            node = node.next
        return ret_str

if __name__ == "__main__":

    print("\nTESTING DLL - MAKE BETTER TESTS!!\n")

    dll = DLL()
    dll.insert(5)
    dll.insert(4)
    dll.insert(3)
    dll.insert(2)
    print(dll)

    dll.move_to_next()
    dll.move_to_next()
    dll.insert(77)
    print(dll)

    dll.move_to_next()
    dll.move_to_next()
    dll.insert(88)
    print(dll)

    dll.move_to_prev()
    dll.remove()
    print(dll)