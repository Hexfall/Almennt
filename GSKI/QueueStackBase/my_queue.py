from my_array_deque import ArrayDeque
from my_linked_list import LinkedList

class Queue:
    def __init__(self, type = "array"):
        if type == "array":
            self.__array = ArrayDeque()
        else:
            self.__array = LinkedList()
    def add(self, value):
        self.__array.push_back(value)
    def remove(self):
        return self.__array.pop_front()
    def get_size(self):
        return self.__array.get_size()