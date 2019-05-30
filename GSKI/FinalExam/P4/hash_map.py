class NotFoundException(Exception):
    pass

class Bucket:
    def __init__(self, key, value, next = None):
        self.key = key
        self.value = value
        self.next = next
    
    def __getitem__(self, key):
        if self.key == key:
            return self.value
        if self.next == None:
            raise NotFoundException()
        return self.next[key]
    
    def __setitem__(self, key, value):
        if self.key == key:
            self.value = value
        elif self.next == None:
            self.next = Bucket(key, value)
        else:
            self.next[key] = value
    
    def __str__(self):
        if self.next == None:
            return "({}: {})".format(self.key, self.value)
        return "({}: {})".format(self.key, self.value) + " " + str(self.next)
    
    def __repr__(self):
        return str(self)
    
    def __len__(self):
        if self.next == None:
            return 1
        return 1 + len(self.next)
        

class HashMap:
    def __init__(self):
        self.array = [None] * 16

    def __setitem__(self, key, data):
        if self.array[key%16] == None:
            self.array[key%16] = Bucket(key, data)
        else:
            self.array[key%16][key] = data
    
    def __getitem__(self, key):
        if self.array[key%16] == None:
            raise NotFoundException()
        return self.array[key%16][key]

    def __len__(self):
        total = 0
        for i in self.array:
            if i != None:
                total += len(i)
        return total

if __name__ == "__main__":

    print("\nTESTING HASHMAP - MAKE BETTER TESTS!!")

    m = HashMap()
    m[3] = "Value for key: 3"
    m[6] = "Value for key: 6"
    m[2] = "Value for key: 2"

    print("")
    try:
        print(str(m[2]))
    except(NotFoundException):
        print("Item not found")
    try:
        print(str(m[3]))
    except(NotFoundException):
        print("Item not found")
    try:
        print(str(m[4]))
    except(NotFoundException):
        print("Item not found")
    try:
        print(str(m[5]))
    except(NotFoundException):
        print("Item not found")
    try:
        print(str(m[6]))
    except(NotFoundException):
        print("Item not found")
    print("Size of collection: " + str(len(m)))
    