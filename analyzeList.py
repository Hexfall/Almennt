def is_prime(n):
    '''Returns True if the given positive number is prime and False otherwise'''
    if n == 1:
        return False
    if n == 2:
        return True
    for i in range(2,n):
        if n%i == 0:
            return False
    else:
        return True
        
# The main program starts here
l = [int(i) for i in input("Enter integers separated with commas: ").split(',')]
print("Input list:", l)
l.sort()
print("Sorted list: ", l)
p = list(set([i for i in l if is_prime(i)]))
p.sort()
print("Prime list: ", p)
print("Min: {:d}, Max: {:d}, Average: {:.2f}".format(min(l), max(l), sum(l)/len(l)))