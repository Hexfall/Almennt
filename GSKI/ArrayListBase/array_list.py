class IndexOutOfBounds(Exception):
    pass

class NotFound(Exception):
    pass

class Empty(Exception):
    pass

class ArrayList:
    def __init__(self):
        self.__size = 16
        self.__arr = [0] * self.__size
        self.__current = 0
        self.__ordered = True

    #Time complexity: O(n) - linear time in size of list
    def print(self):
        print(str(self))

    #Time complexity: O(n) - linear time in size of list
    def prepend(self, value):
        self.insert(value, 0)

    #Time complexity: O(n) - linear time in size of list
    def insert(self, value, index):
        if 0 <= index <= self.length():
            self.resize_eval()
            self.__current += 1
            for i in range(self.length() - 1, index, -1):
                self.set_at(self.get_at(i - 1), i)
            self.set_at(value, index)
            self.__ordered = False

    def valid_index(self, index):
        if 0 <= index < self.length():
            return True
        return False

    #Time complexity: O(1) - constant time
    def append(self, value):
        self.resize_eval()
        self.__current += 1
        self.set_at(value, self.length() - 1)
        self.__ordered = False

    #Time complexity: O(1) - constant time
    def set_at(self, value, index):
        if self.valid_index(index):
            self.__arr[index] = value

    #Time complexity: O(1) - constant time
    def get_first(self):
        if self.length == 0:
            raise Empty()
        return self.__arr[0]

    #Time complexity: O(1) - constant time
    def get_at(self, index):
        if self.valid_index(index):
            return self.__arr[index]
        raise IndexOutOfBounds()

    #Time complexity: O(1) - constant time
    def get_last(self):
        if self.length == 0:
            raise Empty()
        return self.__arr[self.length() - 1]

    #Time complexity: O(n) - linear time in size of list
    def resize(self):
        self.__size += 16
        new_arr = [0] * self.__size
        for i in range(self.length()):
            new_arr[i] = self.__arr[i]
        self.__arr = new_arr

    def resize_eval(self):
        if self.length() == self.__size:
            self.resize()

    def length(self):
        return self.__current

    #Time complexity: O(n) - linear time in size of list
    def remove_at(self, index):
        if self.valid_index(index):
            for i in range(index, self.length() - 1):
                self.set_at(self.get_at(i + 1), i)
            self.set_at(0, self.length() - 1)
            self.__current -= 1

    #Time complexity: O(1) - constant time
    def clear(self):
        self.__init__()

    def __str__(self):
        s = ""
        for i in range(self.length()):
            s += str(self.get_at(i)) + ", "
        return s.strip(", ")
    
    def __repr__(self):
        return self.__str__()

    #Time complexity: O(n) - linear time in size of list
    #Time complexity: O(log n) - logarythmic time in size of list
    def insert_ordered(self, value):
        def find_index(value, lis):
            if lis.length() == 0:
                return 0
            if lis.length() == 1:
                if lis.get_first() > value:
                    return 0
                return 1
            half = lis.length() // 2
            if value < lis.get_at(half - 1):
                new_arr = ArrayList()
                for i in range(0, half - 1):
                    new_arr.append(lis.get_at(i))
                return find_index(value, new_arr)
            if value > lis.get_at(half):
                new_arr = ArrayList()
                for i in range(half + 1, lis.length()):
                    new_arr.append(lis.get_at(i))
                return half + 1 + find_index(value, new_arr)
            return half
        if not self.__ordered:
            self.sort()
        self.insert(value, find_index(value, self))
        self.__ordered = True
        

    #Time complexity: O(n^2) - quadratic time in size of list
    #Time complexity: O(n log n) - linear times logarythmic time in size of list
    def sort(self):
        def quicksort(lis):
            if lis.length() == 0 or lis.length() == 1:
                return lis
            pivot = lis.get_first()
            lesser, equal, greater = ArrayList(), ArrayList(), ArrayList()
            for i in range(lis.length()):
                if lis.get_at(i) == pivot:
                    equal.append(lis.get_at(i))
                elif lis.get_at(i) < pivot:
                    lesser.append(lis.get_at(i))
                else:
                    greater.append(lis.get_at(i))
            lesser = quicksort(lesser)
            greater = quicksort(greater)
            new_arr = ArrayList()
            for i in range(lesser.length()):
                new_arr.append(lesser.get_at(i))
            for i in range(equal.length()):
                new_arr.append(equal.get_at(i))
            for i in range(greater.length()):
                new_arr.append(greater.get_at(i))
            return new_arr
        new_arr = quicksort(self)
        for i in range(new_arr.length()):
            self.set_at(new_arr.get_at(i), i)
        self.__ordered = True

    #Time complexity: O(n) - linear time in size of list
    #Time complexity: O(log n) - logarythmic time in size of list
    def find(self, value):
        if self.__ordered:
            def quickfind(lis, find):
                if lis.length() == 0:
                    raise NotFound()
                elif lis.length() == 1:
                    if lis.get_first() == find:
                        return 0
                    raise NotFound()
                half = lis.length() // 2
                if lis.get_at(half) == find:
                    return half
                elif lis.get_at(half) > find:
                    new_arr = ArrayList()
                    for i in range(0, half):
                        new_arr.append(lis.get_at(i))
                    return quickfind(new_arr, find)
                else:
                    new_arr = ArrayList()
                    for i in range(half + 1, lis.length()):
                        new_arr.append(lis.get_at(i))
                    return half + 1 + quickfind(new_arr, find)
            return quickfind(self, value)
        else:
            for i in range(self.length()):
                if self.get_at(i) == value:
                    return i
                raise NotFound()

    #Time complexity: O(n) - linear time in size of list
    #Time complexity: O(log n) - logarythmic time in size of list
    def remove_value(self, value):
        try:
            index = self.find(value)
            self.remove_at(index)
        except NotFound:
            pass