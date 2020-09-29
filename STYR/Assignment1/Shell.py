from Manager import Manager

Functions = {
    "cr": "Create",
    "de": "Destroy",
    "rq": "Request",
    "rl": "Release",
    "to": "Timeout",
}

class Shell:
    def __init__(self):
        self.mng = None
        self.InputFile = "Files/Input.txt"
        self.OutputFile = "Files/Output.txt"
        self.firstWrite = True
        with open(self.OutputFile, "w+") as f:
            "Clear file."

    def ParseInput(self, inp):
        if inp == "":
            return
        if inp == "in":
            self.mng = Manager()
            if not self.firstWrite:
                self.WriteToFile("\n")
            self.firstWrite = False
        else:
            if self.mng.ErrorMode:
                return
            inp = inp.split(" ")
            args = []
            if len(inp) > 1:
                args = [int(inp[1])]
            self.Exec(Functions[inp[0]], args)
        self.WriteToFile(self.GetProc() + " ")
    
    def WriteToFile(self, text):
        with open(self.OutputFile, "a") as f:
            f.write(text)

    def ReadFromFile(self):
        with open(self.InputFile, "r") as f:
            for line in f.readlines():
                line = line.strip()
                self.ParseInput(line)

    def GetProc(self):
        return str(self.mng.Scheduler())
    
    def Exec(self, function, args):
        getattr(self.mng, function)(*args)
    
    def RunShell(self):
        while True:
            inp = input()
            self.ParseInput(inp)
            print(self.GetProc())

s = Shell()
s.ReadFromFile()
s.RunShell()
