from Utils.tools import *


rocks = {
    1: [[0,0,2,2,2,2,0]],
    2: [[0,0,0,2,0,0,0],
        [0,0,2,2,2,0,0],
        [0,0,0,2,0,0,0]],
    3: [[0,0,0,0,2,0,0],
        [0,0,0,0,2,0,0],
        [0,0,2,2,2,0,0]],
    4: [[0,0,2,0,0,0,0],
        [0,0,2,0,0,0,0],
        [0,0,2,0,0,0,0],
        [0,0,2,0,0,0,0]],
    5: [[0,0,2,2,0,0,0],
        [0,0,2,2,0,0,0]]
}



class Chamber():

    def __init__(self, grid, jet_patttern):
        self.rock = 0
        self.height = 0
        self.row_pointer = 0
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

    def print_chamber(self):
        print(f"Chamber has {self.rock} fallen rocks and height {self.height}")
        for g in self.grid[::-1]:
            print(g)

    def update_row_pointer(self):
        self.row_pointer -=1

    def update_height(self):
        self.height = len(self.grid)-1


def rock_falls(chamber):
    number = chamber.rock % 5
    if number == 0:
        number = 5
    rock = rocks[number]
    return rock

def transform_rock(rock, chamber):
    rock_height = len(rock)
    action = chamber.jet_pattern[chamber.jet_pointer]
    new_rock = []
    for i in range(rock_height):
        r = rock[i]
        new_row = []
        if action == ">":
            new_row.append(0)
            for j in range(1,7):
                new_row.append(r[j-1])
        elif action == "<":
            for j in range(6):
                new_row.append(r[j+1])
            new_row.append(0)
        new_rock.append(new_row) 
    return new_rock



def try_move_by_jets( rock, chamber):
    rock_height = len(rock)
    action = chamber.jet_pattern[chamber.jet_pointer]
    # see if the action is possible for each row of the rock
    reverse_rock = rock[::-1]
    possible = True
    if action == ">":
        for i in range(rock_height):
            r = reverse_rock[i]
            # get the surrounding state
            # first check if there is any row in the grid at this level
            if len(chamber.grid) <= chamber.row_pointer + i:
                # if there is not then there is nothing to block but the walls
                # get the right edge of the rock at this row
                # see if it can move
                r_idx = get_last_index(r, 2)
                if (r_idx + 1) < 7:
                    # move is possible
                    continue
                else:
                    # move is not possible
                    possible = False
                    break
            else:
                # get the row from the grid that is the surroundings at this level
                surrounding_row = chamber.grid[chamber.row_pointer + i]
                # a move can be blocked by the walls or other rocks
                r_idx = get_last_index(r, 2)
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

    elif action == "<":
        for i in range(rock_height):
            r = reverse_rock[i]
            if len(chamber.grid) <= chamber.row_pointer + i:
                l_idx = get_first_index(r, 2)
                if (l_idx - 1) >= 0:
                    continue
                else:
                    possible = False
                    break
            else:
                surrounding_row = chamber.grid[chamber.row_pointer + i]
                l_idx = get_first_index(r, 2)
                if (l_idx - 1) >= 0:
                    if surrounding_row[l_idx - 1] == 0:
                        continue
                    else:
                        possible = False
                        break
                else:
                    possible = False
                    break
    return possible

def try_move_down(rock, chamber):
    # see if the action is possible for all the rows of the rock
    rock_height = len(rock)
    reverse_rock = rock[::-1]
    possible = True
    for i in range(rock_height):
        r = reverse_rock[i]
        pointer = chamber.row_pointer
        # check the row below if it exists
        if pointer + i <= len(chamber.grid):
            row_below = chamber.grid[(pointer + i)-1]
            for j in range(7):
                if sum([r[j], row_below[j]]) > 2:
                    # move down is not possible
                    possible = False
                    return possible
    return possible

def transform_rows(rock, chamber):
    rock_height = len(rock)
    pointer = chamber.row_pointer
    reverse_rock = rock[::-1]
    for i in range(rock_height):
        r = reverse_rock[i]
        # get the surrounding state
        # if the row we look at falls in the current grid
        if pointer + i < len(chamber.grid):
            current_row = chamber.grid[pointer + i]
            # merge rock into the row
            new_row = []
            for j in range(7):
                sum = r[j] + current_row[j]
                if sum == 3:
                    raise Exception (f"3 not allowed rock number {chamber.rock}")
                elif sum == 2:
                    new_row.append(1)
                else:
                    new_row.append(sum)
            chamber.grid[pointer + i] = new_row
        else:
            new_row = []
            for el in r:
                if el == 2:
                    new_row.append(1)
                else:
                    new_row.append(el)
            chamber.grid.append(new_row)




# starting state of the chamber where the floor is row 0
grid = [[1,1,1,1,1,1,1]]

def main():

    jet_pattern = get_input_flat("17", False)

    chamber = Chamber(grid, jet_pattern)

    def puzzle_1(amount_of_rocks):
        # dropping rocks
        for _ in range (amount_of_rocks):
            chamber.rock_appears()
            fr = rock_falls(chamber)

            proceed = True

            while proceed:
                if try_move_by_jets(fr, chamber):
                    # transform the rock to right or left
                    fr = transform_rock(fr, chamber)
                chamber.update_jet_pointer()
                
                if try_move_down(fr, chamber):
                    chamber.update_row_pointer()
                else:
                    proceed = False
            
            # rock has been blocked
            transform_rows(fr, chamber)
            chamber.update_height()



        return chamber.height
    

    result_puzzle_1 = puzzle_1(2022)

    
    print(f"Puzzle 1 answer: {result_puzzle_1}")
    

if __name__ == "__main__":
    main()