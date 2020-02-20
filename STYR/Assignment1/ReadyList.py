from LinkedList import LinkedList

class ReadyList:
    def __init__(self):
        self.priority = [LinkedList() for i in range(3)]
    
    def InsertPCB(self, PCB, priority_level):
        if priority_level == 0 and len(self.priority[0]) > 0:
            raise ValueError("Level 0 is reserved for the OS.")
        self.priority[priority_level].Add(PCB)
    
    def GetProcess(self):
        for level in self.priority[::-1]:
            if len(level) > 0:
                return level.head.data
    
    def Timeout(self):
        for level in self.priority[::-1]:
            if len(level) > 0:
                level.HeadToTail()
                return
    
    def RemoveProcess(self, index):
        for level in self.priority:
            level.RemoveIndex(index)