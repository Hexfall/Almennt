from Datamanagement import Datamanagement
from datetime import datetime

class Framework():
    def __init__(self):
        self.data = Datamanagement()
        try:
            self.sports = self.data.load_sports()
        except:
            self.sports = []
        try:
            #    members[phone] = [name, email, DoB]
            self.members = self.data.load_members()
        except:
            self.members = {}
        #    membership[sport] = [phone, phone, phone...]
        self.membership = {}
        for sport in self.sports:
            try:
                self.membership[sport] = self.data.load_membership(sport)
            except:
                self.membership[sport] = []

    def save(self):
        self.data.save_sports(self.sports)
        self.data.save_members(self.members)
        for sport in self.sports:
            self.data.save_membership(sport, self.membership[sport])
    
    def add_sport(self, name):
        if not name in self.sports:
            self.sports.append(name)
            self.membership[name] = []
        self.sports.sort()
    
    def remove_sport(self, name):
        try:
            self.sports.pop(self.sports.index(name))
            self.membership.pop(name)
        except:
            pass
    
    def get_sports(self):
        return "\n".join(self.sports)
    
    def get_membership(self, sport):
        return "\n".join(["{}, {}".format(key, self.members[key][0]) for key in self.membership[sport]])
    
    def add_member(self, phone, name, email, DoB):
        self.members[phone] = [name, email, DoB]
    
    def remove_member(self, phone):
        self.members.pop(phone)
        for sport in self.sports:
            self.remove_membership(sport, phone)
    
    def change_member(self, phone, new_phone):
        self.members[new_phone] = self.members[phone]
        self.members.pop(phone)
    
    def add_membership(self, sport, phone):
        self.membership[sport].append(phone)
    
    def remove_membership(self, sport, phone):
        try:
            self.membership[sport].pop(self.membership[sport].index(phone))
        except:
            pass
    
    def members_by_name(self):
        keys = self.members.keys()
        member_list = [[key] + self.members[key] for key in keys]
        member_list.sort(key=lambda x: x[1])
        return "\n".join(["\t".join([str(i) for i in member]) for member in member_list])

    def members_by_phone(self):
        keys = self.members.keys()
        member_list = [[key] + self.members[key] for key in keys]
        member_list.sort(key=lambda x: x[0])
        return "\n".join(["\t".join([str(i) for i in member]) for member in member_list])

    def members_by_email(self):
        keys = self.members.keys()
        member_list = [[key] + self.members[key] for key in keys]
        member_list.sort(key=lambda x: x[2])
        return "\n".join(["\t".join([str(i) for i in member]) for member in member_list])

    def members_by_DoB(self):
        keys = self.members.keys()
        member_list = [[key] + self.members[key] for key in keys]
        member_list.sort(key=lambda x: x[3])
        return "\n".join(["\t".join([str(i) for i in member]) for member in member_list])
        
    def get_member(self, phone):
        s = "\t".join([str(i) for i in [phone] + self.members[phone]])
        s += "\nMembership:\n\t"
        s += "\n\t".join([key for key in self.membership.keys() if phone in self.membership[key]])
        return s