class Social:
    def __init__(self):
        self.upper = None
        self.middle = None
        self.lower = None
        self.people = []
    
    def Add(self, classes, name):
        if classes == []:
            self.people.append(name)
            self.people.sort()
            return
        if classes[0] == "lower":
            self.AddLower(classes[1:], name)
        elif classes[0] == "middle":
            self.AddMiddle(classes[1:], name)
        elif classes[0] == "upper":
            self.AddUpper(classes[1:], name)
    
    def AddLower(self, classes, name):
        if self.lower == None:
            self.lower = Social()
        self.lower.Add(classes, name)
        
    def AddMiddle(self, classes, name):
        if self.middle == None:
            self.middle = Social()
        self.middle.Add(classes, name)
        
    def AddUpper(self, classes, name):
        if self.upper == None:
            self.upper = Social()
        self.upper.Add(classes, name)

    def Sanitize(self, classes):
        while classes != [] and classes[-1] == "middle":
            classes.pop()
        return classes
    
    def GetList(self):
        l = []
        if self.upper != None:
            l += self.upper.GetList()
        if self.middle != None:
            l += self.middle.GetUpperList() + self.people + self.middle.GetLowerList()
        else:
            l += self.people
        if self.lower != None:
            l += self.lower.GetList()
        
        return l
    
    def GetLowerList(self):
        if self.lower != None:
            return self.lower.GetList()
        return []

    def GetUpperList(self):
        if self.upper != None:
            return self.upper.GetList()
        return []

    def __str__(self):
        return "\n".join(self.GetList())

    def __repr__(self):
        return str(self)

for case in range(int(input())):
    s = Social()
    for n in range(int(input())):
        name, cs, trash = input().split()
        name = name[:-1]
        cs = cs.split('-')[::-1]
        cs = s.Sanitize(cs)
        s.Add(cs, name)
    print(s)
    print("==============================")
