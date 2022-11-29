from Utils.tools import *
import re


def get_horizontal_lines(list_of_lines: list):
    lines = []
    for line in list_of_lines:
        if line[1] == line[3]:
            lines.append(line)
    return lines

def get_vertical_lines(list_of_lines: list):
    lines = []
    for line in list_of_lines:
        if line[0] == line[2]:
            lines.append(line)
    return lines

def mark_horizontal_line(grid, row, start, end):
    in_between = abs(start - end)
    step = start
    grid[row][start] += 1
    grid[row][end] += 1

    # if there is a vent between the first and last of a line then mark them
    if in_between - 1 != 0:

        if start < end:
            for _ in range(in_between - 1):
                step += 1
                grid[row][step] +=1
        
        elif start > end:
            for _ in range(in_between - 1):
                step -= 1
                grid[row][step] +=1
    return grid

def mark_vertical_line(grid, col, start, end):
    in_between = abs(start - end)
    step = start
    grid[start][col] += 1
    grid[end][col] += 1

    # if there is a vent between the first and last of a line then mark them
    if in_between - 1 != 0:

        if start < end:
            for _ in range(in_between - 1):
                step += 1
                grid[step][col] +=1
            
        elif start > end:
            for _ in range(in_between - 1):
                step -= 1
                grid[step][col] +=1
    return grid



def main():

    data = get_input("202105", False)

    all_lines = [[int(el) for el in re.findall("\d+", d)]for d in data]

    # make an empty grid
    # find the max x and y to get the dimensions of the grid
    all_x_data = []
    all_y_data = []
    for line in all_lines:
        all_x_data.append(line[0])
        all_x_data.append(line[2])
        all_y_data.append(line[1])
        all_y_data.append(line[3])
    max_x = max(all_x_data)
    max_y = max(all_y_data)

    grid = [[0 for _ in range(max_x + 1)]for _ in range(max_y +1)]

    horizontal_lines = get_horizontal_lines(all_lines)
    vertical_lines = get_vertical_lines(all_lines)

    for line in horizontal_lines:
        row = line[1]
        start = line[0]
        end = line[2]
        grid = mark_horizontal_line(grid, row, start, end)


    for line in vertical_lines:
        col = line[0]
        start = line[1]
        end = line[3]
        grid = mark_vertical_line(grid, col, start, end)
        

    result = 0
    for row in grid:
        for el in row:
            if el >= 2:
                result += 1

    print(result) 
        





if __name__ == "__main__":
    main()