from LinkedList import LinkedList

class RCB:
    def __init__(self, index):
        self.curPCB = None
        self.waitlist = LinkedList()
        self.index = index

    def Request(self, PCB):
        PCB.AddResource(self)
        if self.Free():
            self.curPCB = PCB
        else:
            self.waitlist.Add(PCB)
            PCB.Block()

    def Release(self):
        self.curPCB.RemoveResource(self.index)
        self.curPCB = self.waitlist.Pop()
        if not self.Free():
            self.curPCB.Unblock()
        return self.curPCB
    
    def ConditionalRelease(self, PCB):
        if self.curPCB == PCB:
            return self.Release()
        return None

    def TakeOffWaitlist(self, PCB):
        PCB.RemoveResource(self.index)
        self.waitlist.RemoveIndex(PCB.index)
        

    def Free(self):
        return self.curPCB == None