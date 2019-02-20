
class ArrayDeque():
    def __init__(self):
        self.__size = 16
        self.__arr = [0] * self.__size
        self.__current = 0
        self.__ordered = True
    def push_back(self, value):
        self.resize_eval()
        self.__current += 1
        self.set_at(value, self.get_size() - 1)
        self.__ordered = False
    def push_front(self, value):
        self.insert(value, 0)
    def insert(self, value, index):
        if 0 <= index <= self.get_size():
            self.resize_eval()
            self.__current += 1
            for i in range(self.get_size() - 1, index, -1):
                self.set_at(self.get_at(i - 1), i)
            self.set_at(value, index)
            self.__ordered = False
    def get_at(self, index):
        if self.valid_index(index):
            return self.__arr[index]
    def set_at(self, value, index):
        if self.valid_index(index):
            self.__arr[index] = value
    def pop_back(self):
        if self.get_size() == 0:
            return None
        returnVal = self.get_at(self.get_size() - 1)
        self.__current -= 1
        return returnVal
    def pop_front(self):
        if self.get_size() == 0:
            return None
        returnVal = self.__arr[0]
        self.remove_at(0)
        return returnVal
    def remove_at(self, index):
        if self.valid_index(index):
            for i in range(index, self.get_size() - 1):
                self.set_at(self.get_at(i + 1), i)
            self.set_at(0, self.get_size() - 1)
            self.__current -= 1
    def get_size(self):
        return self.__current
    def resize(self):
        self.__size += 16
        new_arr = [0] * self.__size
        for i in range(self.get_size()):
            new_arr[i] = self.__arr[i]
        self.__arr = new_arr
    def resize_eval(self):
        if self.get_size() == self.__size:
            self.resize()
    def valid_index(self, index):
        if 0 <= index < self.get_size():
            return True
        return False
    def __str__(self):
        s = ""
        for i in range(self.get_size()):
            s += str(self.get_at(i)) + " "
        return s