
class ArraySet:
    def __init__(self):
        self.size = 8
        self.array = [None] * self.size
        self.header = 0

    def add(self, value):
        self.resize_eval()
        for i in range(self.header):
            if self.array[i] == value:
                break
            elif value < self.array[i]:
                to_add = self.array[i]
                self.array[i] = value
                self.add(to_add)
                break
        else:
            self.array[self.header] = value
            self.header += 1

    def resize_eval(self):
        if self.header == self.size:
            self.resize()
    
    def resize(self):
        self.size *= 2
        new_array = [None] * self.size
        for i in range(self.header):
            new_array[i] = self.array[i]
        self.array = new_array

    def __str__(self):
        s = ""
        for i in range(self.header):
            s += str(self.array[i]) + " "
        return s
    
    def __repr__(self):
        return str(self)


if __name__ == "__main__":

    print("\nTESTING ARRAY SET - MAKE BETTER TESTS!!\n")

    lis = ArraySet()
    lis.add(4)
    print(lis)

    lis.add(2)
    print(lis)

    lis.add(7)
    print(lis)

    lis.add(1)
    print(lis)

    lis.add(11)
    print(lis)

    lis.add(2)
    print(lis)

    lis.add(9)
    print(lis)
