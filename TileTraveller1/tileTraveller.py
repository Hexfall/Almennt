import random

class Tile():
    def __init__(self, directions, max_coins = 0, depleted_coins = 0):
        self.__directions = directions
        self.__max_coins = max_coins
        self.__depleted_coins = depleted_coins
    def is_lever(self):
        if self.__max_coins == self.__depleted_coins:
            return True
        return False
    def pull_lever(self):
        coins_got = random.randint(1, self.__max_coins + 1 - self.__depleted_coins)
        coins_string = "You pulled the lever and recieved {} coins.".format(coins_got)
        self.__depleted_coins += coins_got
        if not self.is_lever():
            coins_string += " The lever is now empty."
        print(coins_string)
        return coins_got
    def get_directions(self):
        return self.__directions
    def rem_coins(self, amount):
        self.__depleted_coins += amount

class Game():
    def __init__(self, x_location = 0, y_location = 0, coins = 0, load_path = "Default"):
        self.x_location = x_location
        self.y_location = y_location
        self.coins = coins
        self.load_path = load_path
        self.grid = []
        self.load()
    def load(self):
        