from Utils.tools import *


rocks = {
    1: [[0,0,1,1,1,1,0]],
    2: [[0,0,0,1,0,0,0],
        [0,0,1,1,1,0,0],
        [0,0,0,1,0,0,0]],
    3: [[0,0,0,0,1,0,0],
        [0,0,0,0,1,0,0],
        [0,0,1,1,1,0,0]],
    4: [[0,0,1,0,0,0,0],
        [0,0,1,0,0,0,0],
        [0,0,1,0,0,0,0],
        [0,0,1,0,0,0,0]],
    5: [[0,0,1,1,0,0,0],
        [0,0,1,1,0,0,0]]
}

class Chamber():

    def __init__(self, grid, jet_patttern):
        self.rock = 0
        self.height = 0
        self.row_pointer = 4
        self.grid = grid
        self.jet_pattern = jet_patttern
        self.jet_pointer = 0

    def update_jet_pointer(self):
        # if the current pointer is at the last index of the jet pattern restart it at 0
        if self.jet_pointer == len(self.jet_pattern)-1:
            self.jet_pointer = 0
        # else increase by one
        else:
            self.jet_pointer += 1

    def rock_appears(self):
        self.rock +=1
        self.row_pointer = self.height + 4

# def rock_falls(rock_number):
#     rock = rocks[rock_number]
#     rock_heigth = len(rock)

def transform(action, row):
    new_row = []
    if action == ">":
        for i in range(7):
            if i == 0:
                if row[i] == 1:
                    new_row.append(0)
                else:
                    pass
            new_row.append(row[i-1])
            
        return new_row


def move_by_jets( rock, chamber):
    rock_heigth = len(rock)
    action = chamber.jet_pattern[chamber.jet_pointer]
    possible = True
    if action == ">":
        # see if the action is possible for each row of the rock
        rock.reversed()
        for i in range(rock_heigth):
            r = rock[i]
            # get the surrounding state
            # first check if there is any row in the grid at this level
            if len(chamber.grid) <= chamber.row_pointer + i:
                # if there is not then there is nothing to block but the walls
                # get the right edge of the rock at this row
                # see if it can move
                r_idx = get_last_index(r, 1)
                if (r_idx + 1) < 7:
                    # move is possible
                    continue
                else:
                    # move is not possible
                    possible = False
                    break
            else:
                # get the row from the grid that is the surroundings at this level
                surrounding_row = chamber.grid[chamber.row_pointer + i:]
                # a move can be blocked by the walls or other rocks
                r_idx = get_last_index(r, 1)
                if (r_idx + 1) < 7:
                    if surrounding_row[r_idx + 1] == 0:
                        # move is possible
                        continue
                    else:
                        # move is not possible
                        possible = False
                        break
                else:
                    # move is not possible
                    possible = False
                    break
        if possible:
            # do transform
            pass
    elif action == "<":
        # see if the action is possible for each row of the rock
        rock.reversed()
        for i in range(rock_heigth):
            r = rock[i]
            # get the surrounding state
            # first check if there is any row in the grid at this level
            if len(chamber.grid) <= chamber.row_pointer + i:
                # if there is not then there is nothing to block but the walls
                # get the right edge of the rock at this row
                # see if it can move
                l_idx = get_first_index(r, 1)
                if (l_idx - 1) >= 0:
                    # move is possible
                    continue
                else:
                    # move is not possible
                    possible = False
                    break
            else:
                # get the row from the grid that is the surroundings at this level
                surrounding_row = chamber.grid[chamber.row_pointer + i:]
                # a move can be blocked by the walls or other rocks
                l_idx = get_first_index(r, 1)
                if (l_idx - 1) >= 0:
                    if surrounding_row[l_idx - 1] == 0:
                        # move is possible
                        continue
                    else:
                        # move is not possible
                        possible = False
                        break
                else:
                    # move is not possible
                    possible = False
                    break









        


# starting state of the chamber where the floor is row 0
grid = [[1,1,1,1,1,1,1]]

def main():

    jet_pattern = get_input_flat("17", True)
    print(jet_pattern)

    chamber = Chamber(grid, jet_pattern)

    test = [0,0,1,1,1,1,0]
    print(transform(">", test))

    

    # result_puzzle_1 = puzzle_1(2000000)
    # result_puzzle_2 = puzzle_2(0, 4000000)

    
    # print(f"Puzzle 1 answer: {result_puzzle_1}")
    # print(f"Puzzle 2 answer: {result_puzzle_2}")  
    

if __name__ == "__main__":
    main()