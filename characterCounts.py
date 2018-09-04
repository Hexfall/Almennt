inntak = input("Enter a sentence: ")
Upp, Low, Dig, Pun = 0, 0, 0, 0
for i in inntak:
    if i == 'A' or i == 'B' or i == 'C' or i == 'D' or i == 'E' or i == 'F' or i == 'G' or i == 'H' or i == 'I' or i == 'J' or i == 'K' or i == 'L' or i == 'M' or i == 'N' or i == 'O' or i == 'P' or i == 'Q' or i == 'R' or i == 'S' or i == 'T' or i == 'U' or i == 'V' or i == 'W' or i == 'X' or i == 'Y' or i == 'Z':
        Upp += 1
    elif i == 'a' or i == 'b' or i == 'c' or i == 'd' or i == 'e' or i == 'f' or i == 'g' or i == 'h' or i == 'i' or i == 'j' or i == 'k' or i == 'l' or i == 'm' or i == 'n' or i == 'o' or i == 'p' or i == 'q' or i == 'r' or i == 's' or i == 't' or i == 'u' or i == 'v' or i == 'w' or i == 'x' or i == 'y' or i == 'z':
        Low += 1
    elif i == ' ':
        Pun = Pun
    else:
        try:
            int(i)
            Dig += 1
        except:
            Pun += 1
print("     Upper case", end = "")
for i in range(0, 6 - len(str(Upp))):
    print(" ", end = "")
print(Upp)
print("     Lower case", end = "")
for i in range(0, 6 - len(str(Low))):
    print(" ", end = "")
print(Low)
print("         Digits", end = "")
for i in range(0, 6 - len(str(Dig))):
    print(" ", end = "")
print(Dig)
print("    Punctuation", end = "")
for i in range(0, 6 - len(str(Pun))):
    print(" ", end = "")
print(Pun)