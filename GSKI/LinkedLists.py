class Node():
    def __init__(self, data = None, nxt = None):
        self.data = data
        self.next = nxt

class Stack():
    def __init__(self):
        self.__nodes = None
        self.__size = 0
    def push(self, value):
        if self.get_size() == 0:
            self.__nodes = Node(value)
        else:
            self.__nodes = Node(value, self.__nodes)
        self.__size += 1
    def pop(self):
        if self.get_size() == 0:
            raise IndexError("Index out of range.")
        popped = self.__nodes.data
        self.__nodes = self.__nodes.next
        self.__size -= 1
        return popped
    def get_size(self):
        return self.__size

class Queue():
    def __init__(self):
        self.__nodes = None
        self.__back_node = None
        self.__size = 0
    def get_size(self):
        return self.__size
    def push(self, value):
        if self.get_size() == 0:
            self.__nodes = Node(value)
            self.__back_node = self.__nodes
        else:
            self.__back_node.next = Node(value)
            self.__back_node = self.__back_node.next
        self.__size += 1
    def pop(self):
        if self.get_size() == 0:
            raise IndexError("Index out of range.")
        popped = self.__nodes.data
        self.__nodes = self.__nodes.next
        self.__size -= 1
        return popped