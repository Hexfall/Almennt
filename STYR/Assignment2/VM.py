class VM(object):
    def __init__(self):
        self.PM = [None]*524288
    
    def GetPA(self, VA):
        s, p, w = self.TranslateVA(VA)
        if not self.ValidVA(s, p, w):
            return -1
        return self.PM[self.PM[2*s + 1]*512 + p] * 512 + w
    
    def InsertSegment(self, s, z, f):
        self.PM[2*s] = z
        self.PM[2*s + 1] = f

    def InsertPage(self, s, p, f):
        try:
            self.PM[self.PM[2*s+1]*512 + p] = f
        except:
            pass

    def ValidVA(self, s, p, w):
        if self.PM[2*s] == None:
            return False
        pw = p*2**9 + w
        if pw < self.PM[2*s]:
            return True
        return False

    def TranslateVA(self, VA):
        s = VA >> 18
        w = VA & 0x1FF
        p = (VA >> 9) & 0x1FF
        return s, p, w
