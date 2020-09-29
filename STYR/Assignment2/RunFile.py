from VM import VM
PATH = "Files/"

vm = VM()

with open(PATH + "Init.txt", "r") as f:
    init = f.read().split("\n")
init[0] = [int(i) for i in init[0].split(" ")]
init[1] = [int(i) for i in init[1].split(" ")]

for i in range(2):
    for j in range(len(init[i])//3):
        getattr(vm, ["InsertSegment", "InsertPage"][i])(init[i][j*3], init[i][j*3 + 1], init[i][j*3 + 2])
    
with open(PATH + "Input.txt", "r") as f:
    inp = [int(i) for i in f.read().split(" ")]

out = [vm.GetPA(i) for i in inp]

with open(PATH + "Output.txt", "w") as f:
    f.write(" ".join([str(i) for i in out]))