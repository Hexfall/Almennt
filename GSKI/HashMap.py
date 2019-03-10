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
        self.items = None
    
    def insert(self, key, data):
        if self.contains(key):
            raise ItemExistsException
        if self.items == None:
            self.items = Node(key, data)
        else:
            self.items = Node(key, data, self.items)
    
    def update(self, key, data):
        node = self.get_at(key)
        node.data = data
    
    def find(self, key):
        node = self.get_at(key)
        return node.data

    def remove(self, key):
        node = self.items
        if node.key == key:
            self.items = self.items.next
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
        node = self.items
        while node != None:
            if node.key == key:
                return node
            node = node.next
        raise NotFoundException()
    
    def contains(self, key):
        try:
            self.get_at(key)
            return True
        except:
            return False

    def __len__(self):
        def count(head):
            if head == None:
                return 0
            return 1 + count(head.next)
        return count(self.items)

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
            return str(head.data) + "; " + get(head.next)
        return get(self.items)[:-2]
    
    def __repr__(self):
        if self.items == None:
            return "Empty Bucket"
        else:
            return self.__str__()

class HashMap():
    def __init__(self):
        self.__size = 8
        self.__lis = [Bucket() for _ in range(self.__size)]
        self.__len = 0

    def __len__(self):
        return self.__len

    def __compress(self, key):
        return hash(key) % self.__size

    def __setitem__(self, key, data):
        if not self.contains(key):
            self.insert(key, data)
        else:
            self.update(key, data)
    
    def __getitem__(self, key):
        pass

    def insert(self, key, data):
        self.__lis[self.__compress(key)].insert(key, data)
        self.__len += 1
        self.rebuild_eval()
    
    def update(self, key, data):
        node = self.get_node(key)
        node.data = data
    
    def rebuild(self):
        keys, datas = [], []
        for i in self.__lis:
            node = i.items
            while node != None:
                keys.append(node.key)
                datas.append(node.data)
                node = node.next
        self.__size *= 2
        self.__lis = [Bucket() for _ in range(self.__size)]
        self.__len = 0
        for i in range(len(keys)):
            self.insert(keys[i], datas[i])

    def rebuild_eval(self):
        if len(self) >= self.__size * 1.2:
            self.rebuild()
    
    def get_node(self, key):
        return self.__lis[self.__compress(key)].get_at(key)
    
    def contains(self, key):
        try:
            self.get_node(key)
            return True
        except:
            return False

    def find(self, key):
        node = self.get_node(key)
        return node.data

    def remove(self, key):
        self.__lis[self.__compress(key)].remove(key)
        self.__len -= 1
    
    def __str__(self):
        s = ""
        for i in range(len(self)):
            s += "Bucket {}: ".format(i) + str(self.__lis[i])
            s += "\n"
        return s[:-1]

    def __repr__(self):
        return self.__str__()

class MyHashableKey():
    def __init__(self, int_value, string_value):
        self.int = int_value
        self.str = string_value
    
    def __eq__(self, other):
        return self.int == other.int and self.str == other.str
    
    def __hash__(self):
        primes = [3]
        num = 5
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

a = HashMap()
b = [i for i in range(520)]
[a.insert(b[i], i) for i in range(520)]
print(a)