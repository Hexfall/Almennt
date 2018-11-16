import random

TEAM_SIZE = 5
GAME_LENGTH = 48

class Team:
    def __init__(self, name):
        self.__name = name
        self.__team = []
        self.__points = 0
        for i in range(TEAM_SIZE):
            player = BasketballPlayer(i+1) # i+1 is the number for the player
            self.__team.append(player)

    def play_offence(self):
        random_index = random.randint(0, TEAM_SIZE-1)
        self.__points += self.__team[random_index].shoot_ball()

    def get_player_with_highest_score(self):
        highest_player = self.__team[0]
        for player in self.__team:
            if player > highest_player:
                highest_player = player
        return highest_player

    def get_name(self):
        return self.__name

    def get_points(self):
        return self.__points

    def __str__(self):
        the_str = ''
        for player in self.__team:
            the_str += str(player)
        return the_str


class BasketballPlayer:
    # You need to implment this class
    def __init__(self, nr):
        self.nr = nr
        self.points = 0
    def shoot_ball(self):
        shot = random.randint(0,1) * 2
        self.points += shot
        return shot
    def __gt__(self, other):
        return self.points > other.points
    def __str__(self):
        return "Number: {} Points: {}\n".format(self.nr, self.points)
    

def print_winner(team_a, team_b):
    ''' You need to implement this function. Print out:
        which team won (if tie, print "Tie!")
    '''
    if team_a.get_points() < team_b.get_points():
        print("{} won!".format(team_b.get_name()))
    elif team_b.get_points() < team_a.get_points():
        print("{} won!".format(team_a.get_name()))
    else:
        print("Tie!")
    print()

def print_scores(team_a, team_b):
    ''' You need to implent this function.  Print out:
        how many points each team scored
        the scoring of each player in each team
        the highest scoring player in each team  
    '''
    for i in [team_a, team_b]:
        print("{} scored {} points!".format(i.get_name(), i.get_points()))
    print()
    for i in [team_a, team_b]:
        print("{} scoring:".format(i.get_name()))
        print(i)
    for i in [team_a, team_b]:
        print("{} highest scoring player:".format(i.get_name()))
        print(i.get_player_with_highest_score())

def play(team_a, team_b):
    for _ in range(GAME_LENGTH):
        team_a.play_offence()    
        team_b.play_offence()
        
def random_seed():
    seed = int(input("Random seed: "))
    random.seed(seed)

def main():
    # You are not allowed to change this main function
    random_seed()
    chicago_bulls = Team("Chicago Bulls")
    la_lakers = Team("LA Lakers")

    play(chicago_bulls, la_lakers)
    print_winner(chicago_bulls, la_lakers)
    print_scores(chicago_bulls, la_lakers)

main()