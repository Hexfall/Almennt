x = str(oct(int(input())))[2:]
orglen = len(x)
for i in range(len(x)):
    if x[i] == '0':
        x = str(int(x) - 10**(len(x) - i - 1))
        if len(x) != orglen:
            i -= 1
            orglen = len(x)
print(x)