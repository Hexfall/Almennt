from VM import VM

vm = VM()
init = input().split(" ")
init = [int(i) for i in init]
for i in range(0, len(init)//3):
    vm.InsertSegment(init[i*3], init[i*3 + 1], init[i*3 + 2])

init = input().split(" ")
init = [int(i) for i in init]
for i in range(0, len(init)//3):
    vm.InsertPage(init[i*3], init[i*3 + 1], init[i*3 + 2])

while True:
    inp = int(input())
    print(vm.GetPA(inp))