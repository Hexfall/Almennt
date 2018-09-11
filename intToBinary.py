n = int(input('Give me an int >= 0: '))
myBin = ""
m = n
while (m > 0):
    myBin = str(m % 2) + myBin
    m = m // 2
if n == 0:
    m = "0"
print("The binary of", n, "is", myBin)