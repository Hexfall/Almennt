TARGET = 47

class SumList:
    def __init__(self, array):
        self.array = []
        self.lastSum = 0
        for i in array:
            self.Add(i)
    
    def __len__(self):
        return len(self.array)
    
    def RangeSum(self, left, right):
        if left == 0:
            return self.array[right]
        return self.array[right] - self.array[left - 1]
    
    def Add(self, num):
        self.lastSum += num
        self.array.append(self.lastSum)

for _ in range(int(input())):
    input()
    size = int(input())
    s = SumList([int(i) for i in input().split()])
    count = 0
    for i in range(size):
        for j in range(i, size):
            if s.RangeSum(i, j) == TARGET:
                count += 1
    print(count)