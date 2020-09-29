from ReadyList import ReadyList
from PCB import PCB
from RCB import RCB

PCB_SIZE, RCB_SIZE = 16, 4

class Manager:
    def __init__(self):
        self.PCBArray = [PCB(None, 0, 0)] + [None] * (PCB_SIZE - 1)
        self.RCBArray = [RCB(i) for i in range(RCB_SIZE)]
        self.RL = ReadyList()
        self.RL.InsertPCB(self.PCBArray[0], 0)
        self.ErrorMode = False

    def Create(self, level):
        try:
            index = self.__GetNextAvailable()
            self.PCBArray[index] = PCB(self.RL.GetProcess(), index, level)
            self.InsertPCB(self.PCBArray[index])
        except:
            self.ErrorMode = True

    def Timeout(self):
        self.RL.Timeout()
    
    def InsertPCB(self, PCB):
        self.RL.InsertPCB(PCB, PCB.prio)

    def __GetNextAvailable(self):
        return self.PCBArray.index(None)

    def CurPCB(self):
        return self.RL.GetProcess()

    def Destroy(self, index):
        if not 0 < index < PCB_SIZE or self.PCBArray[index] == None:
            self.ErrorMode = True
            return
        PCB = self.PCBArray[index]
        PCB.Remove()
        for child in PCB.chilren.GetList():
            self.Destroy(child.index)
        self.RL.RemoveProcess(PCB.index)
        pcbs = PCB.ReleaseResources()
        for pcb in pcbs:
            self.InsertPCB(pcb)
        self.PCBArray[PCB.index] = None
        
    def Scheduler(self):
        if self.ErrorMode:
            return -1
        return self.CurPCB().index
    
    def Request(self, index):
        PCB = self.CurPCB()
        if not 0 <= index < RCB_SIZE or PCB.resources.ContainsIndex(index):
            self.ErrorMode = True
            return
        self.RCBArray[index].Request(PCB)
        if not PCB.ready:
            self.RL.RemoveProcess(PCB.index)
    
    def Release(self, index):
        if not 0 <= index < RCB_SIZE or not self.CurPCB().resources.ContainsIndex(index):
            self.ErrorMode = True
            return
        PCB = self.RCBArray[index].Release()
        if not PCB == None:
            self.InsertPCB(PCB)
