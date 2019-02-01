def sum_of_even(x, y):
    if x % 2 == 1:
        x += 1
    if x > y:
        return 0
    return x + sum_of_even(x + 2, y)

def raise_by_one(lis):
    if len(lis) == 1:
        return [lis[0] + 1]
    return [lis[0] + 1] + raise_by_one(lis[1:])

class ArrayList():
    def __init__(self):
        self.capacity = 4
        self.arr = [0] * self.capacity
        self.size = 0
    def resize(self):
        if self.capacity == self.get_size():
            self.capacity += 4
            new_arr = [0] * self.capacity
            for i in range(self.get_size()):
                new_arr[i] = self.arr[i]
            self.arr = new_arr
    def append(self, value):
        self.resize()
        self.arr[self.get_size()] = value
        self.size += 1
    def get_size(self):
        return self.size
    def print_list(self):
        for i in range(self.get_size()):
            print(self.arr[i], end = " ")
        print()
    def remove_first(self):
        if self.get_size() > 0:
            for i in range(0, self.get_size() - 1):
                self.arr[i] = self.arr[i + 1]
            self.size -= 1
            self.arr[self.get_size()] = 0

class Animal():
    def __init__(self, id, species, weight):
        self.__id = id
        self.species = species
        self.weight = weight
    def get_id(self):
        return self.__id
    def get_species(self):
        return self.species
    def get_weight(self):
        return self.weight
    def set_id(self, id):
        self.id = id
    def set_species(self, species):
        self.species = species
    def set_weight(self, weight):
        self.weight = weight
    def __str__(self):
        return "{}: {}, {} kilograms".format(self.get_id(), self.get_species(), self.get_weight())

class Zoo():
    def __init__(self):
        self.animals = {}
    def get_animal(self, id):
        try:
            return self.animals[id]
        except:
            return None
    def add_animal(self, id, species, weight):
        self.animals[id] = Animal(id, species, weight)
    def change_species(self, id, new_species):
        try:
            self.animals[id].set_species(new_species)
        except:
            pass
    def change_weight(self, id, weight):
        try:
            self.animals[id].set_weight(weight)
        except:
            pass
    def remove_animal(self, id):
        try:
            self.animals.pop(id)
        except:
            pass
    def __str__(self):
        return "\n".join([str(animal) for animal in self.animals.values()])