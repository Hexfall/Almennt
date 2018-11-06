class Player():
    def __init__(self, name, year, rating):
        self.name = name
        self.year = int(year)
        self.rating = int(rating)
    def __str__(self):
        return "Name: {}\nYear: {}\nRating: {}".format(self.name, self.year, self.rating)
    def __gt__(self, other):
        return self.rating > other.rating
    def __int__(self):
        return self.rating
        
def get_highest_rated_player(plays):
    top = plays[0]
    for i in range(1, len(plays)):
        if plays[i] > top:
            top = plays[i]
    return top
    
def get_average_rating(plays):
    summa = 0
    for i in plays:
        summa += int(i)
    return summa / len(plays)

def main():

    number_of_players = int(input("Number of players: "))
    players = []
    print()
    print("--- Reading players ---")
    #here you should get info from the user about 
    #number_of_players many chess player
    # code goes here....
    for i in range(number_of_players):
        newName = input("Enter Name: ")
        newYear = input("Enter Year: ")
        newRating = input("Enter Rating: ")
        players.append(Player(newName, newYear, newRating))
        print()
    
    print("--- Displaying players --- ")
    #here you should print each player
    #code goes here....
    for i in players:
        print(i)
        print()

    highest_rated_player = get_highest_rated_player(players)
    print("Highest rated player: ")
    print(highest_rated_player)

    average_rating = get_average_rating(players)
    print("Average rating:", average_rating)

main()