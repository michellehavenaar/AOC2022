from Utils.tools import *


def move_right(pos):
    x,y = pos
    x +=1
    new_pos = (x,y)
    return new_pos

def move_left(pos):
    x,y = pos
    x -=1
    new_pos = (x,y)
    return new_pos

def move_up(pos):
    x,y = pos
    y +=1
    new_pos = (x,y)
    return new_pos

def move_down(pos):
    x,y = pos
    y -=1
    new_pos = (x,y)
    return new_pos

def is_adjacent(coord_H, coord_T):
    adjacent = False
    x_H, y_H = coord_H
    x_T, y_T = coord_T
    if coord_H == coord_T:
        adjacent = True
    else:
        if abs(x_H-x_T) == 1 and y_H == y_T:
            adjacent = True
        elif abs(y_H-y_T) == 1 and x_H == x_T:
            adjacent = True
        elif abs(x_H-x_T) == 1 and abs(y_H-y_T) == 1:
            adjacent = True
    return adjacent

def move_head( new_pos_H,list_of_pos_H): 
    # T retains current position
    # update list of H coordinates
    list_of_pos_H.append(new_pos_H)

def move_tail(old_pos_H, current_pos_T, list_of_pos_T):
    # T follows H
    current_pos_T = old_pos_H
    # update list of T coordinates
    list_of_pos_T.append(current_pos_T)

def is_adjacent_2(new_pos_H, current_pos_T):
    hx, hy = new_pos_H
    tx, ty = current_pos_T
    if abs(hx - tx) == 2 or abs(hy - ty) == 2:
        return False
    else:
        return True


def move_tail_2(new_pos_H, current_pos_T, list_of_pos_T):
    # lol i thought i was being smart in part 1..
    hx, hy = new_pos_H
    tx, ty = current_pos_T
    difference = ((hx - tx), (hy - ty))
    if difference[0] == -2:
        mod_x = -1
        if difference[1] == 2:
            mod_y = 1
        elif difference[1] == -2:
            mod_y = -1
        else:
            mod_y = difference[1]
        new_pos_T = ((tx + mod_x), (ty + mod_y))
    elif difference[0] == 2:
        mod_x = 1
        if difference[1] == 2:
            mod_y = 1
        elif difference[1] == -2:
            mod_y = -1
        else:
            mod_y = difference[1]
        new_pos_T = ((tx + mod_x), (ty + mod_y))
    else:
        if difference[1] == -2:
            mod_y = -1
            mod_x = difference[0]
            new_pos_T = ((tx + mod_x), (ty + mod_y))
        elif difference[1] == 2:
            mod_y = 1
            mod_x = difference[0]
            new_pos_T = ((tx + mod_x), (ty + mod_y))
    list_of_pos_T.append(new_pos_T)



def main():
    input = get_input("09", False)
    data = clean_list_strings(input)

    motions = [d.split() for d in data]

    start_position = (0,0)

    def puzzle_1(list_of_motions):
        coordinates_of_h = [start_position]
        coordinates_of_t = [start_position]

        for motion in list_of_motions:
            if motion[0] == "R":
                # move Head one right
                for _ in range(int(motion[1])):
                    # for the amount of times as directed
                    current_pos_H = coordinates_of_h[-1]
                    current_pos_T = coordinates_of_t[-1]
                    # get the current position
                    new_pos_H = move_right(current_pos_H)
                    # determine new position of Head
                    temp_pos_H = current_pos_H
                    # store current position for when T needs to follow H
                    move_head(new_pos_H, coordinates_of_h)
                    # update list of Head coordinates
                    # check if T is adjacent to H
                    adjacent = is_adjacent(new_pos_H, current_pos_T)
                    # check if T is adjacent to H
                    if not adjacent: 
                        # if T is not adjacent to H
                        move_tail(temp_pos_H, current_pos_T, coordinates_of_t)
                    else:
                        pass
                        # T does not need to move
            elif motion[0] == "L":
                for _ in range(int(motion[1])):
                    current_pos_H = coordinates_of_h[-1]
                    current_pos_T = coordinates_of_t[-1]
                    new_pos_H = move_left(current_pos_H)
                    temp_pos_H = current_pos_H
                    move_head(new_pos_H, coordinates_of_h)
                    adjacent = is_adjacent(new_pos_H, current_pos_T)
                    if not adjacent: 
                        move_tail(current_pos_H, current_pos_T, coordinates_of_t)
            elif motion[0] == "U":
                for _ in range(int(motion[1])):
                    current_pos_H = coordinates_of_h[-1]
                    current_pos_T = coordinates_of_t[-1]
                    new_pos_H = move_up(current_pos_H)
                    temp_pos_H = current_pos_H
                    move_head(new_pos_H, coordinates_of_h)
                    adjacent = is_adjacent(new_pos_H, current_pos_T)
                    if not adjacent: 
                        move_tail(current_pos_H, current_pos_T, coordinates_of_t)
            elif motion[0] == "D":
                for _ in range(int(motion[1])):
                    current_pos_H = coordinates_of_h[-1]
                    current_pos_T = coordinates_of_t[-1]
                    new_pos_H = move_down(current_pos_H)
                    temp_pos_H = current_pos_H
                    move_head(new_pos_H, coordinates_of_h)
                    adjacent = is_adjacent(new_pos_H, current_pos_T)
                    if not adjacent: 
                        move_tail(current_pos_H, current_pos_T, coordinates_of_t)

        set_of_T = set(coordinates_of_t)
        return(len(set_of_T))

    def puzzle_2(list_of_motions):
        coordinates = {
            0: [start_position],
            1: [start_position],
            2: [start_position],
            3: [start_position],
            4: [start_position],
            5: [start_position],
            6: [start_position],
            7: [start_position],
            8: [start_position],
            9: [start_position],
        }
        # we are calling the Head 0 from now

        for motion in list_of_motions:
            if motion[0] == "R":
                # move Head one right
                for _ in range(int(motion[1])):
                    # for the amount of times as directed
                    current_pos_H = coordinates[0][-1]
                    # get the current position
                    new_pos_H = move_right(current_pos_H)
                    # determine new position of Head
                    move_head(new_pos_H, coordinates[0])
                    # update list of Head coordinates
                    for i in range(1, 10):
                    # for every knot starting at 1
                    # check if knot is adjacent to its previous knot
                    # so we call the previous knot Head
                        current_pos_head = coordinates[i-1][-1]
                        current_pos_knot = coordinates[i][-1]
                        adjacent = is_adjacent_2(current_pos_head, current_pos_knot)
                    # check if T is adjacent to H
                        if not adjacent: 
                        # if T is not adjacent to H
                            move_tail_2(current_pos_head, current_pos_knot, coordinates[i])
                        else:
                            pass
                            # T does not need to move
            elif motion[0] == "L":
                for _ in range(int(motion[1])):
                    current_pos_H = coordinates[0][-1]
                    new_pos_H = move_left(current_pos_H)
                    move_head(new_pos_H, coordinates[0])
                    for i in range(1, 10):
                        current_pos_head = coordinates[i-1][-1]
                        current_pos_knot = coordinates[i][-1]
                        adjacent = is_adjacent_2(current_pos_head, current_pos_knot)
                        if not adjacent: 
                            move_tail_2(current_pos_head, current_pos_knot, coordinates[i])
            elif motion[0] == "U":
                for _ in range(int(motion[1])):
                    current_pos_H = coordinates[0][-1]
                    new_pos_H = move_up(current_pos_H)
                    move_head(new_pos_H, coordinates[0])
                    for i in range(1, 10):
                        current_pos_head = coordinates[i-1][-1]
                        current_pos_knot = coordinates[i][-1]
                        adjacent = is_adjacent_2(current_pos_head, current_pos_knot)
                        if not adjacent: 
                            move_tail_2(current_pos_head, current_pos_knot, coordinates[i])
            elif motion[0] == "D":
                for _ in range(int(motion[1])):
                    current_pos_H = coordinates[0][-1]
                    new_pos_H = move_down(current_pos_H)
                    move_head(new_pos_H, coordinates[0])
                    for i in range(1, 10):
                        current_pos_head = coordinates[i-1][-1]
                        current_pos_knot = coordinates[i][-1]
                        adjacent = is_adjacent_2(current_pos_head, current_pos_knot)
                        if not adjacent: 
                            move_tail_2(current_pos_head, current_pos_knot, coordinates[i])

        set_of_T = set(coordinates[9])
        return(len(set_of_T))
                

    result_puzzle_1 = puzzle_1(motions)
    result_puzzle_2 = puzzle_2(motions)
    
    print(f"Puzzle 1 answer: {result_puzzle_1}")
    print(f"Puzzle 2 answer: {result_puzzle_2}")  

if __name__ == "__main__":
    main()