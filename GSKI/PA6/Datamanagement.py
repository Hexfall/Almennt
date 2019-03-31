from datetime import datetime

class Datamanagement():
    def __init__(self):
        pass
    
    def save_sports(self, sports):
        with open("data/Sports.txt", "w+", encoding = "UTF-8") as write:
            write.write(";".join(sports))
    
    def load_sports(self):
        with open("data/Sports.txt", "r", encoding = "UTF-8") as read:
            sports = read.read().split(';')
            return sports
    
    def save_members(self, members):
        with open("data/Members.txt", "w+", encoding = "UTF-8") as write:
            s = []
            for key in members.keys():
                s.append(str(key) + ";" + ";".join([str(i) for i in members[key]]))
            write.write("\n".join(s))
    
    def load_members(self):
        with open("data/Members.txt", "r", encoding = "UTF-8") as read:
            members = {}
            data = read.read().split("\n")
            for i in data:
                sep = i.split(";")
                members[int(sep[0])] = [sep[1], sep[2], datetime.strptime(sep[3], '%Y-%m-%d %H:%M:%S')]
            return members
    
    def save_membership(self, sport, members):
        with open("data/membership/{}.txt".format(sport), "w+", encoding = "UTF-8") as write:
            write.write(";".join([str(i) for i in members]))

    def load_membership(self, sport):
        with open("data/membership/{}.txt".format(sport), "r", encoding = "UTF-8") as read:
            return [int(i) for i in read.read().split(';')]