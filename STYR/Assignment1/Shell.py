from Manager import Manager

Functions = {
    "cr": "Create",
    "de": "Destroy",
    "rq": "Request",
    "rl": "Release",
    "to": "Timeout",
}

def ParseInput(inp):
    inp = inp.split(" ")
    args = []
    if len(inp) > 1:
        args = [int(inp[1])]
    return Functions[inp[0]], args
    

mng = None
while True:
    inp = input()
    if inp == "in":
        mng = Manager()
    else:
        if not mng.ErrorMode:
            inp, args = ParseInput(inp)
            getattr(mng, inp)(*args)
    print(mng.Scheduler())
