from LinkedList import LinkedList

class PCB:
    def __init__(self, parent, index, priority):
        self.ready = True
        self.parent = parent
        self.chilren = LinkedList()
        self.resources = LinkedList()
        self.index = index
        self.prio = priority
        if not parent == None:
            parent.AddChild(self)
    
    def Block(self):
        self.ready = False
    
    def Unblock(self):
        self.ready = True
    
    def AddChild(self, child):
        self.chilren.Add(child)

    def AddResource(self, resource):
        self.resources.Add(resource)
    
    def ReleaseResources(self):
        pcbs = []
        for resource in self.resources.GetList():
            pcb = resource.ConditionalRelease(self)
            resource.TakeOffWaitlist(self)
            if not pcb == None:
                pcbs.append(pcb)
        return pcbs

    def RemoveResource(self, index):
        self.resources.RemoveIndex(index)
    
    def Remove(self):
        self.parent.RemoveChild(self.index)

    def RemoveChild(self, index):
        self.chilren.RemoveIndex(index)

    def __str__(self):
        return str(self.index)
    
    def __repr__(self):
        return str(self)