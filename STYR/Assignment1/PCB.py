from LinkedList import LinkedList

class PCB:
    def __init__(self, parent):
        self.ready = True
        self.parent = parent
        self.chilren = LinkedList()
        self.resources = LinkedList()
    
    def Block(self):
        self.ready = False
    
    def Unblock(self):
        self.ready = True
    
    def AddChild(self, child):
        self.chilren.Add(child)

    def AddResource(self, resource):
        self.resources.Add(resource)
    
    def Destroy(self):
        pass

    def DestroyChild(self):
        pass