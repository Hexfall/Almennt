y = int(input("Years: "))
s = y * 365 * 24 * 60 * 60
pop = 307357870
pop += s // 7
pop -= s // 13
pop += s // 35
print("New population after", y, " years is ", pop)
