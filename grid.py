# Constants to be used in the implementation
DIM = 5
POSITION = 'o'
EMPTY = 'x'
LEFT = 'l'
RIGHT = 'r'
UP = 'u'
DOWN = 'd'
QUIT = 'q'

def get_move():
    ''' Returns a move corresponding to the user input direction '''
    move = input('Move: ')
    
    if move not in [LEFT, RIGHT, UP, DOWN]:
        return QUIT
    else:
        return move

def initialize_grid():
    ''' Returns an initialized grid for the given dimension '''
    grid = []

    for i in range(DIM):
        sublist = []
        for j in range(DIM):
            sublist.append(EMPTY)
        grid.append(sublist)

    grid[0][0] = POSITION  # Current position
    return grid

def print_grid(inGrid):
    for i in range(DIM):
        for j in range(DIM):
            print(inGrid[i][j], end = " ")
        print()
    print()

def get_pos(curX, curY, toDo):
    if toDo == LEFT:
        curX -= 1
    elif toDo == RIGHT:
        curX += 1
    elif toDo == UP:
        curY -= 1
    else:
        curY += 1
    if curX < 0:
        curX += 5
    elif curX > 4:
        curX -= 5
    if curY < 0:
        curY += 5
    elif curY > 4:
        curY -= 5
    return curX, curY

# Main program starts here
# In your implementation, you have to use the functions and the constants given above
grid = initialize_grid()
print_grid(grid)
command = get_move()
x, y = [0, 0]
while command != QUIT:
    grid[y][x] = EMPTY
    x, y = get_pos(x, y, command)
    grid[y][x] = POSITION
    print_grid(grid)
    command = get_move()