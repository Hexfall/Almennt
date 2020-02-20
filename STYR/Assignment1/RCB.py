from LinkedList import LinkedList

class RCB:
    def __init__(self):
        self.curPCB = None
        self.waitlist = LinkedList()

    def Request(self, PCB):
        if self.Free():
            self.curPCB = PCB
        else:
            self.waitlist.Add(PCB)
            PCB.Block()

    def Release(self):
        self.curPCB = self.waitlist.Pop()
        self.curPCB.Unblock()

    def Free(self):
        return self.curPCB == None