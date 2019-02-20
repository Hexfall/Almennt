class Node():
    def __init__(self, data = None, nxt = None):
        self.data = data
        self.next = nxt

class LinkedList():
    def __init__(self):
        self.__nodes = None
        self.__back_node = None
        self.__size = 0
    def push_back(self, value):
        if self.get_size() == 0:
            self.push_front(value)
        else:
            self.__back_node.next = Node(value)
            self.__back_node = self.__back_node.next
            self.__size += 1
    def push_front(self, value):
        self.__nodes = Node(value, self.__nodes)
        if self.get_size() == 0:
            self.__back_node = self.__nodes
        self.__size += 1
    def pop_back(self):
        if self.get_size() == 0:
            return None
        returnVal = self.__back_node.data
        self.__back_node = self.get_back_node()
        self.__back_node.next = None
        self.__size -= 1
        return returnVal
    def pop_front(self):
        if self.get_size() == 0:
            return None
        returnVal = self.__nodes.data
        self.__nodes = self.__nodes.next
        self.__size -= 1
        return returnVal
    def get_size(self):
        return self.__size
    def get_back_node(self):
        def get_back(node):
            next_node = node.next
            if next_node.next == None:
                return node
            return get_back(node.next)
        if self.get_size() == 0:
            return None
        return get_back(self.__nodes)
    def __str__(self):
        def get_str(node):
            if node == None:
                return ""
            return str(node.data) + " " + get_str(node.next)
        return get_str(self.__nodes)