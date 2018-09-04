#Design an algorithm that finds the maximum positive integer input by a user.  The user repeatedly inputs numbers until a negative value is entered.
intList = [int(input("Input a number: "))]
while(not min(intList) < 0):
    intList.append(int(input("Input a number: ")))
print("The maximum is", max(intList))