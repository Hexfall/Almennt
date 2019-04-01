import os
from Framework import Framework
from datetime import datetime

clear = lambda: os.system('cls')
MAIN_MENU = "\t1 - Manage Sports\n\t2 - Manage Members\n\ts - Save\n\tq - Exit program"
MANAGE_SPORTS = "\t1 - Add Sport\n\t2 - Remove Sport\n\t3 - List of Sports\n\t4 - Manage Sport\n\tq - Exit to Main Menu"
MANAGE_SPORT = "\t1 - Add Member\n\t2 - Remove Member\n\t3 - List of Members\n\tq - Exit to Manage Sports"
MANAGE_MEMBERS = "\t1 - Add or Change Member\n\t2 - Remove Member\n\t3 - Member list\n\t4 - View Member\n\tq - Exit to Main Menu"
ORDER = "\t1 - Order by Name\n\t2 - Order by Phone\n\t3 - Order by Email\n\t4 - Order by DoB\n\tq - Exit to Manage Members"

class UI():
    def __init__(self):
        self.Fr = Framework()
    
    def Menu(self, path, options):
        clear()
        print(path)
        print(options)
        return input()

    def UILoop(self):
        command = ""
        while command.lower() != "q":
            command = self.Menu("Main Menu", MAIN_MENU)
            if command == "1":
                self.Manage_Sports()
            elif command == "2":
                self.Manage_Members()
            elif command.lower() == "s":
                self.Fr.save()
        self.Fr.save()

    def Manage_Sports(self):
        command = ""
        while command.lower() != "q":
            command = self.Menu("Main Menu > Manage Sports", MANAGE_SPORTS)
            if command == "1":
                self.Add_sport()
            elif command == "2":
                self.Remove_sport()
            elif command == "3":
                self.Sports_list()
            elif command == "4":
                self.Manage_sport()
    
    def Add_sport(self):
        clear()
        self.Fr.add_sport(input("Name of Sport: "))
    
    def Remove_sport(self):
        clear()
        self.Fr.remove_sport(input("Name of Sport: "))
    
    def Sports_list(self):
        clear()
        self.Menu("Main Menu > Manage Sports > List of Sports", self.Fr.get_sports())
    
    def Manage_sport(self):
        clear()
        sport = input("Sport to Manage: ")
        if sport not in self.Fr.sports:
            print("Unknown Sport")
            input()
            return
        command = ""
        while command.lower() != "q":
            command = self.Menu("Main Menu > Manage Sports > {}".format(sport), MANAGE_SPORT)
            if command == "1":
                self.Add_membership(sport)
            elif command == "2":
                self.Remove_membership(sport)
            elif command == "3":
                self.View_sport(sport)
            
    def Add_membership(self, sport):
        phone = int(self.Menu("Main Menu > Manage Sports > {} > Add Membership".format(sport), "Phone to add: "))
        if phone not in self.Fr.members.keys():
            print("Unknown Member")
            input()
            return
        self.Fr.add_membership(sport, phone)
    
    def Remove_membership(self, sport):
        phone = int(self.Menu("Main Menu > Manage Sports > {} > Remove Membership".format(sport), "Phone to Remove: "))
        if phone not in self.Fr.members.keys():
            print("Unknown Member")
            input()
            return
        self.Fr.remove_membership(sport, phone)
    
    def View_sport(self, sport):
        self.Menu("Main Menu > Manage Sports > {} > Membership".format(sport), self.Fr.get_membership(sport))
    
    def Manage_Members(self):
        command = ""
        while command.lower() != "q":
            command = self.Menu("Main Menu > Manage Members", MANAGE_MEMBERS)
            if command == "1":
                self.Add_member()
            elif command == "2":
                self.Remove_member()
            elif command == "3":
                self.Member_list()
            elif command == "4":
                self.View_member()
    
    def Add_member(self):
        while True:
            try:
                phone = int(input("Phone Nr.: "))
                break
            except:
                print("Incorrect Phone Nr.")
        name = input("Name: ")
        while True:
            email = input("Email: ")
            if "@" in email and "." in email:
                break
            else:
                print("Incorrect Email")
        while True:
            try:
                DoB = input("Date of Birth (YYYY-MM-DD): ")
                DoB = [int(i) for i in DoB.split('-')]
                DoB = datetime(DoB[0], DoB[1], DoB[2])
                break
            except:
                print("Incorrect DoB")
        self.Fr.add_member(phone, name, email, DoB)
    
    def Remove_member(self):
        phone = int(self.Menu("", "Phone to Remove: "))
        self.Fr.remove_member(phone)
    
    def Member_list(self):
        command = ""
        while command.lower() != "q":
            command = self.Menu("Main Menu > Manage Members > Member List", ORDER)
            if command == "1":
                self.Menu("Main Menu > Manage Members > Member List > By Name", self.Fr.members_by_name())
            elif command == "2":
                self.Menu("Main Menu > Manage Members > Member List > By Phone", self.Fr.members_by_phone())
            elif command == "3":
                self.Menu("Main Menu > Manage Members > Member List > By Email", self.Fr.members_by_email())
            elif command == "4":
                self.Menu("Main Menu > Manage Members > Member List > By Date of Birth", self.Fr.members_by_DoB())
            
    def View_member(self):
        phone = int(self.Menu("Main Menu > Manage Members > View Member", "Phone to view: "))
        if phone not in self.Fr.members.keys():
            print("Unknown Member")
            input()
            return
        self.Menu("Main Menu > Manage Members > View Member > {}".format(phone), self.Fr.get_member(phone))
