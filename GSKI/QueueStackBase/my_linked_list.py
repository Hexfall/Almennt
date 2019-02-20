class Node():
    def __init__(self, data = None, nxt = None):
        self.data = data
        self.next = nxt

class LinkedList():
    def __init__(self):
        self.__nodes = None
        self.back_node = None
        self.__size = 0
    def push_back(self, value):
        if self.get_size() == 0:
            self.push_front(value)
        else:
            self.back_node.next = Node(value)
            self.back_node = self.back_node.next
            self.__size += 1
    def push_front(self, value):
        self.__nodes = Node(value, self.__nodes)
        if self.get_size() == 0:
            self.back_node = self.__nodes
        self.__size += 1
    def pop_back(self):
        if self.get_size() == 0:
            return None
    def pop_front(self):
        if self.get_size() == 0:
            return None
    def get_size(self):
        return self.__size
    def get_back_node(self):
        def get_back(node):
            if node.next == None:
                return node
            return get_back(node.next)
        if self.get_size() == 0:
            return None
        return get_back(self.__nodes)