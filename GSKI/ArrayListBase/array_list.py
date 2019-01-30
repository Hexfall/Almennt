class IndexOutOfBounds(Exception):
    pass

class NotFound(Exception):
    pass

class ArrayList:
    def __init__(self):
        self.__size = 16
        self.__arr = [0] * self.__size
        self.__current = 0
        self.__ordered = True

    #Time complexity: O(n) - linear time in size of list
    def print(self):
        for i in range(self.__current):
            print(self.__arr[i], end=" ")
        print()

    #Time complexity: O(n) - linear time in size of list
    def prepend(self, value):
        self.insert(value, 0)

    #Time complexity: O(n) - linear time in size of list
    def insert(self, value, index):
        if self.valid_index(index) or index == 0:
            self.resize_eval()
            for i in range(self.__current, index, -1):
                self.__arr[i] = self.__arr[i - 1]
            self.__current += 1
            self.__arr[index] = value
            self.__ordered = False

    def valid_index(self, index):
        if 0 <= index < self.__current:
            return True
        return False

    #Time complexity: O(1) - constant time
    def append(self, value):
        self.resize_eval()
        self.__arr[self.__current] = value
        self.__current += 1
        self.__ordered = False

    #Time complexity: O(1) - constant time
    def set_at(self, value, index):
        if self.valid_index(index):
            self.__arr[index] = value

    #Time complexity: O(1) - constant time
    def get_first(self):
        return self.__arr[0]

    #Time complexity: O(1) - constant time
    def get_at(self, index):
        if self.valid_index(index):
            return self.__arr[index]
        else:
            raise IndexOutOfBounds()

    #Time complexity: O(1) - constant time
    def get_last(self):
        if self.__current == 0:
            return 0
        return self.__arr[self.__current - 1]

    #Time complexity: O(n) - linear time in size of list
    def resize(self):
        self.__size += 16
        new_arr = [0] * self.__size
        for i in range(self.__current):
            new_arr[i] = self.__arr[i]
        self.__arr = new_arr

    def resize_eval(self):
        if self.__current == self.__size:
            self.resize()

    #Time complexity: O(n) - linear time in size of list
    def remove_at(self, index):
        if self.valid_index(index):
            for i in range(index, self.__current - 1):
                self.__arr[i] = self.__arr[i + 1]
            self.__current -= 1
            self.__arr[self.__current] = 0

    #Time complexity: O(1) - constant time
    def clear(self):
        self.__init__()

    #Time complexity: O(n) - linear time in size of list
    #Time complexity: O(log n) - logarythmic time in size of list
    def insert_ordered(self, value):
        # TODO: remove 'pass' and implement functionality
        pass

    #Time complexity: O(n^2) - quadratic time in size of list
    #Time complexity: O(n log n) - linear times logarythmic time in size of list
    def sort(self):
        def quicksort(l):
            if l

    #Time complexity: O(n) - linear time in size of list
    #Time complexity: O(log n) - logarythmic time in size of list
    def find(self, value):
        if self.__ordered:
            pass
        else:
            for i in range(self.__current):
                if self.__arr[i] == value:
                    return i
                raise NotFound()

    #Time complexity: O(n) - linear time in size of list
    #Time complexity: O(log n) - logarythmic time in size of list
    def remove_value(self, value):
        index = self.find(value)
        self.remove_at(index)