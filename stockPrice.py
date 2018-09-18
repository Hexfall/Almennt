def lesa ():
    while True:
        try:
            br = int(input("Enter number of shares: "))
            break
        except:
            print("Invalid price!")
    while True:
        try:
            a, b, c = [int(i) for i in input("Enter price (dollars, numerator, denominator): ").split()]
            break
        except:
            print("Invalid number!")
    return br, a, b, c

def prentVerd (br, ver, tel, nef):
    brefVerd = br * (ver + tel / nef)
    print(br ,"shares with market price", ver, str(tel) + "/" + str(nef), "have value $" + "{:.2f}".format(brefVerd))

def afram ():
    inntak = input("Continue: ")
    if inntak == "y":
        return True
    else:
        return False

while True:
    bref, verd, teljari, nefnari = lesa()
    prentVerd(bref, verd, teljari, nefnari)
    if not afram():
        break