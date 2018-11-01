import random
class Island():
    def __init__(self, size, number_of_predators = 0, number_of_prey = 0):
        self.grid = [[0]*size for i in range(size)]
        self.grid_size = size
        self.populate_island(number_of_predators, number_of_prey)
        
    def __str__(self):
        s = ""
        for i in range(self.grid_size -1, -1, -1):
            for j in range(self.grid_size):
                if self.grid[j][i] == 0:
                    s += "{:<2s}".format(".")
                else:
                    s += "{:<2s}".format(str(self.grid[j][i]))
            s += '\n'
        return s

    def update(self):
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                if self.grid[i][j] != 0:
                    self.grid[i][j].move()

    def reset_movement(self):
        for row in self.grid:
            for value in row:
                if isinstance(value, Animal):
                    value.hasMoved = False

    def empty_cell(self, x, y):
        return self.grid[x][y] == 0

    def set_animal_on_island(self, animal):
        self.grid[animal.x][animal.y] = animal

    def populate_island(self, pred, prey):
        def pop(num, typ):
            while num > 0:
                x = random.randint(0, self.grid_size - 1)
                y = random.randint(0, self.grid_size - 1)
                if self.empty_cell(x, y):
                    if typ == "Predator":
                        new_animal = Predator(self, x, y)
                    else:
                        new_animal = Prey(self, x, y)
                    self.set_animal_on_island(new_animal)
                    num -= 1
        pop(pred, "Predator")
        pop(prey, "Prey")

    def remove(self, animal):
        self.grid[animal.x][animal.y] = 0
    
    def within_grid(self, x, y):
        return 0 <= x < self.grid_size and 0 <= y < self.grid_size

class Animal():
    def __init__(self, island, x = 0, y = 0, name = 'A'):
        self.island = island
        self.x = x
        self.y = y
        self.name = name
        self.hasMoved = False
    
    def __str__(self):
        return self.name

    def get_new_position(self, target = int):
        offset_list = [(-1, 1), (0, 1), (1, 1), (-1, 0), (1, 0), (-1, -1), (0, -1), (1, -1)]
        for cord in offset_list:
            new_x, new_y = self.x + cord[0], self.y + cord[1]
            if self.island.within_grid(new_x, new_y) and isinstance(self.island.grid[new_x][new_y], target):
                return new_x, new_y
        return None

    def move(self):
        if not self.hasMoved:
            new_pos = self.get_new_position()
            if new_pos != None:
                self.island.remove(self)
                self.x, self.y = new_pos
                self.island.set_animal_on_island(self)
                self.hasMoved = True

class Predator(Animal):
    def __init__(self, island, x = 0, y = 0, name = 'R'):
        Animal.__init__(self, island, x, y, name)

    def eat(self):
        if not self.hasMoved:
            new_pos = self.get_new_position(Prey)
            if new_pos != None:
                self.island.remove(self)
                self.x, self.y = new_pos
                self.island.set_animal_on_island(self)
                self.hasMoved = True


class Prey(Animal):
    def __init__(self, island, x = 0, y = 0, name = 'B'):
        Animal.__init__(self, island, x, y, name)

def main():
    random.seed(10)
    tenerife = Island(10, 15, 20)
    turns = 3
    while turns > 0:
        print(tenerife)
        for x in range(tenerife.grid_size):
            for y in range(tenerife.grid_size):
                if isinstance(tenerife.grid[x][y], Animal):
                    animal = tenerife.grid[x][y]
                    if isinstance(animal, Predator):
                        animal.eat()
                    animal.move()
        tenerife.reset_movement()
        turns -= 1

main()