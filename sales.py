def load_from_file(filename):
    try:
        with open(filename) as read:
            data = read.readlines()
            return data
    except FileNotFoundError:
        print('File not found!')
        
def make_int(to_change):
    for index in range(len(to_change)):
        to_change[index] = [int(j) for j in to_change[index].strip().split()]

sales = load_from_file(input('Enter file name: '))
make_int(sales)
print('Average sales:')
for index in range(len(sales)):
    print('Department no. {}: {:.1f}'.format(index + 1, sum(sales[index]) / len(sales[index])))