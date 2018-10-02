
def get_list():
    a_list = input("Enter elements of list separated by commas: ").strip().split(',')
    return a_list
    
def even_sum (l):
    summa = 0
    for i in l:
        if int(i) % 2 == 0:
            summa += int(i)
    return summa

# Main program starts here - DO NOT change it
a_list = get_list()
print(even_sum(a_list))
