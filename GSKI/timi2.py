import random
import math

def power(num, exponent):
    ''' Linear O(n). n is equal to the exponent'''
    ret = num
    for _ in range(1, exponent):
        ret *= num
    return ret

def mopi(num1, num2):
    '''Linear O(n). n is equal to the input closer to 0'''
    if max(abs(num1), abs(num2)) == abs(num2):
        temp = num1
        num1 = num2
        num2 = temp
    base = num1
    if num2 > 0:
        for _ in range(1, num2):
            base += num1
    else:
        for _ in range(num2, 1):
            base -= num1
    return base

def rni(list_size):
    '''Linear O(n) where n = list_size'''
    ret_list = [0] * list_size
    for i in range(len(ret_list)):
        ret_list[i] = random.randint(1, 6)
    return ret_list

def print_list(inp_list):
    '''Linear O(n). n = len(inp_list)'''
    inp_list = [str(i) for i in inp_list]
    print(", ".join(inp_list))

def random_inc(inp_list):
    '''Constant O(1)'''
    index = random.randint(0, len(inp_list) - 1)
    inp_list[index] += 1

def switch(inp_list):
    '''Constant O(1)'''
    index1 = random.randint(0, len(inp_list) - 1)
    index2 = index1
    while index1 == index2:
        index2 = random.randint(0, len(inp_list) - 1)
    temp = inp_list[index1]
    inp_list[index1] = inp_list[index2]
    inp_list[index2] = temp

def ordered_insertion(inp_list, num = None):
    '''Linear O(n). n <= len(inp_list)'''
    if num == None:
        num = random.randint(1,6)
    for i in range(len(inp_list)):
        if inp_list[i] >= num:
            inp_list.insert(i, num)
            break
    else:
        inp_list.append(num)

def comb_ins_ord(size):
    '''Quadratic O(n^2). n <= size'''
    l = rni(size)
    ret_list = []
    for i in l:
        ordered_insertion(ret_list, i)
    return ret_list

l = [0,1,2,3,4,5,6,7,8,9]
l = comb_ins_ord(10)
print_list(l)