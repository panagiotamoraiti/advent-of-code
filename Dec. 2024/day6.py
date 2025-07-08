print(f"Day 6!!!!!")
x=5
print("\n".join([f"{'+'*(2* n + 1):^{2*x+1}}" for n in (*range(x), 0, 0)]))
print(f"-----------------------------------------------------------------------")

import copy
import time

def find_guard_position(txt_file):
    # Open the text file and read text into a list, text_rows is a list of strs
    with open(txt_file,'r') as file:
        text = file.read().split('\n')

    grid = []

    # Make a grid of all characters in text
    for line in text:
        line = list(line)

        # Keep only not empty lines
        if line:
            grid.append(line)

    for line_index, line in enumerate(grid):
        if '^' in line:
            column_index = line.index('^')
            pos_line = line_index
            pos_col = column_index

    up = True
    right = False
    down = False
    left = False

    num_positions = 0
    grid[pos_line][pos_col] = '.'
    positions = copy.deepcopy(grid)

    positions[pos_line][pos_col] = 'X' 

    # Check if guard in in mapped area
    start = time.time()
    while pos_line > 0 and pos_line < len(grid)-1 and pos_col > 0 and pos_col < len(grid[0])-1:

        if up:
            # If you go up
            # print("Going up")
            # print(grid[pos_line-1][pos_col])
            if grid[pos_line-1][pos_col] == '.':
                # Continue going up
                up = True
                pos_line -= 1
                positions[pos_line][pos_col] = 'X' 
            elif grid[pos_line][pos_col+1] == '.':
                # Turn right
                right = True
                up = False
            elif grid[pos_line+1][pos_col] == '.':
                # Go down
                down = True
                up = False
            elif grid[pos_line][pos_col-1] == '.':
                # Go left
                left = True
                up = False
        elif right:
            # If you go right
            # print("Going right")
            # print(grid[pos_line][pos_col+1])
            if grid[pos_line][pos_col+1] == '.':
                # Continue going right
                right = True
                pos_col += 1
                positions[pos_line][pos_col] = 'X' 
            elif grid[pos_line+1][pos_col] == '.':
                # Turn right, which means go down
                down = True
                right = False
            elif grid[pos_line][pos_col-1] == '.':
                # Turn right, which means go left
                left = True
                right = False
            elif grid[pos_line-1][pos_col] == '.':
                # Turn right, which means go up
                up = True
                right = False
        elif down:
            # If you go down
            # print("Going down")
            # print(grid[pos_line+1][pos_col])
            if grid[pos_line+1][pos_col] == '.':
                # Continue going down
                down = True
                pos_line += 1
                positions[pos_line][pos_col] = 'X' 
            elif grid[pos_line][pos_col-1] == '.':
                # Turn right, which means go left
                left = True
                down = False
            elif grid[pos_line-1][pos_col] == '.':
                # Turn right, which means go up
                up = True
                down = False
            elif grid[pos_line][pos_col+1] == '.':
                # Turn right, which means go right
                right = True
                down = False
        elif left:
            # If you go left
            # print("Going left")
            # print(grid[pos_line][pos_col-1])
            if grid[pos_line][pos_col-1] == '.' :
                # Continue going left
                left = True
                pos_col -= 1
                positions[pos_line][pos_col] = 'X' 
            elif grid[pos_line-1][pos_col] == '.':
                # Turn right, which means go up
                up = True
                left = False
            elif grid[pos_line][pos_col+1] == '.':
                # Turn right, which means go right
                right = True
                left = False
            elif grid[pos_line+1][pos_col] == '.':
                # Turn right, which means go down
                down = True
                left = False

    for row in positions:
        num_positions += row.count('X')
    elapsed_time = time.time() - start
    print("Elapsed time for finding path is ", elapsed_time)

    # Write the grid to a text file
    file_path = "practice/map.txt"
    with open(file_path, "w") as file:
        for row in positions:
            file.write("".join(row) + "\n")

    return num_positions


def find_num_obstacles_pos(txt_file):
    # Open the text file and read text into a list, text_rows is a list of strs
    with open(txt_file,'r') as file:
        text = file.read().split('\n')

    grid = []

    # Make a grid of all characters in text
    for line in text:
        line = list(line)

        # Keep only not empty lines
        if line:
            grid.append(line)

    for line_index, line in enumerate(grid):
        if '^' in line:
            column_index = line.index('^')
            line_index_global = line_index
            pos_line = line_index_global
            pos_col = column_index

    num_positions = 0
    num_obstacles_pos = 0
    num_positions_prev = 0

    # Put an obstacle in each position in the grid and check if there is a loop
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            # print(i, j)
            # Add obstacle
            grid_with_obstacle = copy.deepcopy(grid)
            grid_with_obstacle[i][j] = '#'

            up = True
            right = False
            down = False
            left = False

            pos_line = line_index_global
            pos_col = column_index

            grid[pos_line][pos_col] = '.'
            positions = copy.deepcopy(grid)
            positions[pos_line][pos_col] = 'X' 

            # Check if guard in in mapped area
            start = time.time()
            while pos_line > 0 and pos_line < len(grid)-1 and pos_col > 0 and pos_col < len(grid[0])-1:
                
                if up:
                    # If you go up
                    if grid_with_obstacle[pos_line-1][pos_col] == '.':
                        # Continue going up
                        up = True
                        pos_line -= 1
                        positions[pos_line][pos_col] = 'X' 
                    elif grid_with_obstacle[pos_line][pos_col+1] == '.':
                        # Turn right
                        right = True
                        up = False
                    elif grid_with_obstacle[pos_line+1][pos_col] == '.':
                        # Go down
                        down = True
                        up = False
                    elif grid_with_obstacle[pos_line][pos_col-1] == '.':
                        # Go left
                        left = True
                        up = False
                elif right:
                    # If you go right
                    if grid_with_obstacle[pos_line][pos_col+1] == '.':
                        # Continue going right
                        right = True
                        pos_col += 1
                        positions[pos_line][pos_col] = 'X' 
                    elif grid_with_obstacle[pos_line+1][pos_col] == '.':
                        # Turn right, which means go down
                        down = True
                        right = False
                    elif grid_with_obstacle[pos_line][pos_col-1] == '.':
                        # Turn right, which means go left
                        left = True
                        right = False
                    elif grid_with_obstacle[pos_line-1][pos_col] == '.':
                        # Turn right, which means go up
                        up = True
                        right = False
                elif down:
                    # If you go down
                    if grid_with_obstacle[pos_line+1][pos_col] == '.':
                        # Continue going down
                        down = True
                        pos_line += 1
                        positions[pos_line][pos_col] = 'X' 
                    elif grid_with_obstacle[pos_line][pos_col-1] == '.':
                        # Turn right, which means go left
                        left = True
                        down = False
                    elif grid_with_obstacle[pos_line-1][pos_col] == '.':
                        # Turn right, which means go up
                        up = True
                        down = False
                    elif grid_with_obstacle[pos_line][pos_col+1] == '.':
                        # Turn right, which means go right
                        right = True
                        down = False
                elif left:
                    # If you go left
                    if grid_with_obstacle[pos_line][pos_col-1] == '.' :
                        # Continue going left
                        left = True
                        pos_col -= 1
                        positions[pos_line][pos_col] = 'X' 
                    elif grid_with_obstacle[pos_line-1][pos_col] == '.':
                        # Turn right, which means go up
                        up = True
                        left = False
                    elif grid_with_obstacle[pos_line][pos_col+1] == '.':
                        # Turn right, which means go right
                        right = True
                        left = False
                    elif grid_with_obstacle[pos_line+1][pos_col] == '.':
                        # Turn right, which means go down
                        down = True
                        left = False

                elapsed_time = time.time() - start

                # Check if there is loop
                if elapsed_time > 0.005:
                    num_obstacles_pos += 1
                    break

    return num_obstacles_pos
    

input = 'practice/input_day6.txt'
# input = 'practice/test.txt'
num_positions = find_guard_position(input)
num_obstacles_pos = find_num_obstacles_pos(input)

print(f"The number of distinct positions that the guard will visit before leaving the mapped area is {num_positions}.")
print(f"The number of distinct positions that the can be put to lead the guard into a loop is {num_obstacles_pos}.")
print(f"-----------------------------------------------------------------------")
