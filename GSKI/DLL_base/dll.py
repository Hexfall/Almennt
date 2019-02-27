
class Node:
    def __init__(self, data = None, prev = None, next = None):
        self.data = data
        self.prev = prev
        self.next = next

class DLL:
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__curr = None
        self.__size = 0

    def __str__(self):
        def get(head):
            if head == None:
                return ""
            return str(head.data) + " " + get(head.next)
        return get(self.__head)[:-1]

    def __repr__(self):
        return self.__str__()

    def __len__(self):
        return self.__size

    def insert(self, value):
        if len(self) == 0:
            self.__head = Node(value)
            self.__tail = self.__head
            self.__curr = self.__head
        else:
            if not self.__curr is self.__head:
                prev = self.__curr.prev
                prev.next = Node(value, prev, self.__curr)
                self.__curr.prev = prev.next
            else:
                self.__curr.prev = Node(value, None, self.__curr)
                self.__head = self.__head.prev
            self.__curr = self.__curr.prev
        self.__size += 1

    def delete(self):
        if len(self) <= 1:
            self.__init__()
            return
        prev, next = self.__curr.prev, self.__curr.next
        is_head, is_tail = self.__curr is self.__head, self.__curr is self.__tail
        if next != None:
            next.prev = prev
            self.__curr = next
        if prev != None:
            prev.next = next
            self.__curr = prev
        if is_head:
            self.__head = self.__curr
        if is_tail:
            self.__tail = self.__curr
        
    def delete_at(pos):
        if pos == 0:
            self.__head = self.__head.next
            self.__head.prev = None
        elif pos == len(self) - 1:
            self.__tail = self.__tail.prev
            self.__tail.next = None
        elif 0 < pos < len(self) - 1:


    def get_value(self):
        return self.__curr.data

    def move_to_next(self):
        if self.__curr.next:
            self.__curr = self.__curr.next
            
    def move_to_prev(self):
        if self.__curr.prev:
            self.__curr = self.__curr.prev

    def get_pos(self, pos):
        def get(head, num):
            if num == 0:
                return head
            return get(head.next, num - 1)
        if 0 <= pos < len(self):
            return get(self.__head, pos)

    def move_to_pos(self, pos):
        self.__curr = self.get_pos(pos)