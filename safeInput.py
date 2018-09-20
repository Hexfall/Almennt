def safe_input (prompt, a_type):
    while True:
        try:
            x = input(prompt)
            if a_type == str:
                x = str(x)
            elif a_type == int:
                x = int(x)
            elif a_type == float:
                x = float(x)
            break
        except ValueError:
            print("Error: please enter a value of ", a_type)
    return x

# Do not change the lines below
print(safe_input('Please enter an integer: ', int))
print(safe_input('Please enter a float: ', float))
print(safe_input('Please enter a string: ', str))

