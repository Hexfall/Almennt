colors = {
    "Black": {"black": ["B", "-"], "dilution": ["D", "-"], "red": ["o", "o"]},
    "Blue": {"black": ["B", "-"], "dilution": ["d", "d"], "red": ["o", "o"]},
    "Chocolate": {"black": ["b", "b"], "dilution": ["D", "-"], "red": ["o", "o"]},
    "Lilac": {"black": ["b", "b"], "dilution": ["d", "d"], "red": ["o", "o"]},
    "Red": {"black": ["-", "-"], "dilution": ["D", "-"], "red": ["O", "-"]},
    "Cream": {"black": ["-", "-"], "dilution": ["d", "d"], "red": ["O", "-"]},
    "Black-Red Tortie": {"black": ["B", "-"], "dilution": ["D", "-"], "red": ["O", "o"]},
    "Chocolate-Red Tortie": {"black": ["b", "b"], "dilution": ["D", "-"], "red": ["O", "o"]},
    "Blue-Cream Tortie": {"black": ["B", "-"], "dilution": ["d", "d"], "red": ["O", "o"]},
    "Lilac-Cream Tortie": {"black": ["b", "b"], "dilution": ["d", "d"], "red": ["O", "o"]},
}

class Cat:
    def __init__(self, black = [], dilution = [], red = []):
        self.black = black
        self.dilution = dilution
        self.red = red

    def __repr__(self):
        return self.GetColor()
    
    def __str__(self):
        return self.GetColor()
    
    def IsTortie(self):
        return "o" in self.red and "O" in self.red
    
    def IsBlack(self):
        return "B" in self.black
    
    def IsDiluted(self):
        return "D" in self.dilution
    
    def IsRed(self):
        return "O" in self.red
    
    def __GetBlackColor(self):
        if self.IsBlack():
            if self.IsDiluted():
                return "Black"
            return "Blue"
        else:
            if self.IsDiluted():
                return "Chocolate"
            return "Lilac"

    def __GetRedColor(self):
        if self.IsDiluted():
            return "Red"
        return "Cream"
    
    def GetColor(self):
        if self.IsTortie():
            return self.__GetBlackColor() + "-" + self.__GetRedColor() + "Tortie"
        if self.IsRed():
            return self.__GetRedColor()
        return self.__GetBlackColor()
    
    def SetColor(self, color, male):
        newCat = Cat(**colors[color])
        if male:
            newCat.red = [newCat.red[0]]
        self.black = newCat.black
        self.dilution = newCat.dilution
        self.red = newCat.red
    
    def MultLists(self, l1, l2):
        retlist = []
        for i in l1:
            for j in l2:
                retlist.append([i, j])
        return retlist

    def GetBlackMutations(self):
        retlist = self.black
        for i in range(len(retlist)):
            if retlist[i] == '-':
                retlist[i] = ['B', 'b']
            else:
                retlist[i] = [retlist[i]]
        return self.MultLists(*retlist)
    
    def GetDilutionMutations(self):
        retlist = self.dilution
        for i in range(len(retlist)):
            if retlist[i] == '-':
                retlist[i] = ['D', 'd']
            else:
                retlist[i] = [retlist[i]]
        return self.MultLists(*retlist)
    
    def GetRedMutations(self):
        retlist = self.red
        for i in range(len(retlist)):
            if retlist[i] == '-':
                retlist[i] = ['O', 'o']
            else:
                retlist[i] = [retlist[i]]
        if len(retlist) == 1:
            return retlist
        return self.MultLists(*retlist)
    
    def GetMutations(self):
        retlist = [
            self.GetBlackMutations(),
            self.GetDilutionMutations(),
            self.GetRedMutations(),
        ]
        return retlist

c = Cat()
c.SetColor("Red", False)
print(c.GetMutations())