# Main program starts here
l = [i for i in input("Enter a list separated with commas: ").split(',')]
sub_lists = [[]]
for i in range(len(l)):
    for j in range(i + 1, len(l) + 1):
        sub_lists.append(l[i:j])
# This should be the last statement in your main program/function 
print(sorted(sub_lists))
