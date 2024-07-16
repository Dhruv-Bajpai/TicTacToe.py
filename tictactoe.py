
print('its a tic tac toe')

print('its a tic tac toe i created it with my hardwork but it have some issue so dont take any funcking step')



grid = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

def create_grid(grid):
    # Create a formatted string for the grid
    formatted_rows = [' | '.join(row) for row in grid]
    separator = '\n' + '-' * (len(formatted_rows[0])) + '\n'
    return separator.join(formatted_rows)

grid = [
    ['1', '2', '3'],
    ['4', '5', '6'],
    ['7', '8', '9']
]

result = create_grid(grid)
print(result)


for i in range(5):
    for i in range(1):
        user = 'X'
        row = int(input('please enter row '))
        column = int(input('please enter column'))
        grid[row][column] = user 
        print(grid)
        break
    for i in range(1):
        user = '0'
        row = int(input('please enter row '))
        column = int(input('please enter column'))
        grid[row][column] = user 
        print(grid)
        break

    
  
    if grid[0][0] == 'X' and grid[0][1] == 'X' and grid[0][2] == 'X':
        print('x won')
        break
    elif grid[1][0] == 'X' and grid[1][1] == 'X' and grid[1][2] == 'X':
        print('x won ')
        break
    elif grid[2][0] == 'X' and grid[2][1] == 'X' and grid[2][2] == 'X':
        print('x won ')
        break
    elif grid[0][0] == 'X' and grid[1][1] == 'X' and grid[2][2] == 'X':
        print('x won ')
        break

    elif grid[0][0] == '0' and grid[0][1] == '0' and grid[0][2] == '0':
        print('0 won')
        break
    elif grid[1][0] == '0' and grid[1][1] == '0' and grid[1][2] == '0':
        print('0 won ')
        break
    elif grid[2][0] == '0' and grid[2][1] == '0' and grid[2][2] == '0':
        print('0 won ')
        break
    elif grid[0][0] == '0' and grid[1][1] == '0' and grid[2][2] == '0':
        print('0 won ')
        break