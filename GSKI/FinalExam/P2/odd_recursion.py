def print_odd(num):
    def rec(low, high):
        if high < low:
            return ""
        return str(low) + " " + rec(low + 2, high)
    print(rec(1, num))

if __name__ == "__main__":

    print("TESTING PRINT_ODD - MAKE BETTER TESTS!!!\n")

    print_odd(16)
    print_odd(15)
    print_odd(17)