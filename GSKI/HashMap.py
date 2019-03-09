class ItemExistsException(Exception):
    pass

class NotFoundException(Exception):
    pass

class Node():
    def __init__(self, key, data, next = None):
        self.key = key
        self.data = data
        self.next = next

class Bucket():
    def __init__(self):
        self.__items = None
    
    def insert(self, key, data):
        if self.contains(key):
            raise ItemExistsException
        if self.__items == None:
            self.__items = Node(key, data)
        else:
            self.__items = Node(key, data, self.__items)
    
    def update(self, key, data):
        node = self.get_at(key)
        node.data = data
    
    def find(self, key):
        node = self.get_at(key)
        return node.data

    def remove(self, key):
        node = self.__items
        if node.key == key:
            self.__items = self.__items.next
        else:
            next = node.next
            while next != None:
                if next.key == key:
                    node.next = next.next
                    break
                node = next
                next = node.next
            else:
                raise NotFoundException()
    
    def get_at(self, key):
        node = self.__items
        while node != None:
            if node.key == key:
                return node
        raise NotFoundException
    
    def contains(self, key):
        try:
            self.get_at(key)
            return True
        except NotFoundException:
            return False

    def __len__(self):
        def count(head):
            if head == None:
                return 0
            return 1 + count(head.next)
        return count(self.__items)

    def __setitem__(self, key, data):
        if not self.contains(key):
            self.insert(key, data)
        else:
            self.update(key, data)
        
    def __getitem__(self, key):
        return self.find(key)

    def __str__(self):
        def get(head):
            if head == None:
                return ""
            return str(head.data) + " " + get(head.next)
        return get(self.__items)

class MashMap():
    def __init__(self):
        self.__size = 8
        self.__lis = [Bucket() for _ in range(self.__size)]

class MyHashableKey():
    def __init__(self, int_value, string_value):
        self.int = int_value
        self.str = string_value
    
    def __eq__(self, other):
        return self.int == other.int and self.str == other.str
    
    def __hash__(self):
        primes = [2]
        num = 3
        while len(primes) < len(self.str) + 1:
            for i in primes:
                if num % i == 0:
                    break
            else:
                primes.append(num)
            num += 2
        numbers = [self.int] + [ord(i) for i in self.str]
        summa = 0
        for i in range(len(numbers)):
            summa += numbers[i]**primes[i]
        return summa

a = Bucket()
a.insert(1, 1)
a.insert(2, 2)
a.insert(3, 3)
print(a)
print(a[2])
a.remove(2)
print(a)