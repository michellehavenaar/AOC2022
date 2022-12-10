from Utils.tools import *

def draw_pixel(CRT, row, position, sprite):
    # determine type of pixel
    if position in sprite:
        pixel_type = "#"
    else:
        pixel_type = "."
    CRT[row] += pixel_type

def print_CRT(CRT):
    for row in CRT:
        print(CRT[row])


    

def main():
    input = get_input("10", False)
    data = clean_list_strings(input)

    instructions = [d.split() for d in data]

    # make a list of alternative instructions that represents what should be done per cycle
    alt_instructions = []
    for instruction in instructions:
        if instruction[0] == "noop":
            alt_instructions.append(0)
        if instruction[0] == "addx":
            alt_instructions.append(0)
            alt_instructions.append(int(instruction[1]))


    def puzzle_1(instructions):
        cycle = 0
        X = 1
        checkpoint = 20
        interval = 40
        signal_strengths = []

        for instruction in instructions:
            # during cycle
            cycle += 1
            if cycle == checkpoint:
                signal_strength = cycle * X
                signal_strengths.append(signal_strength)
                checkpoint += interval
            
            # after cycle
            X += instruction

        return (sum(signal_strengths))


    def puzzle_2(instructions):

        CRT = {
            1: "",
            2: "",
            3: "",
            4: "",
            5: "",
            6: ""
        }
        cycle = 0
        X = 1
        checkpoint = 41
        interval = 40
        current_row = 1
        drawing_position = 0

        for instruction in instructions:
            sprite = [X-1, X, X +1]
            cycle += 1
            # during cycle
            if cycle == checkpoint:
                # switch to new row
                current_row += 1
                # reset drawing position
                drawing_position = 0
                checkpoint += interval
            
            # draw pixel
            draw_pixel(CRT, current_row, drawing_position, sprite)
            # after cycle
            X += instruction
            drawing_position += 1
        
        print_CRT(CRT)


    result_puzzle_1 = puzzle_1(alt_instructions)
    
    
    print(f"Puzzle 1 answer: {result_puzzle_1}")
    # print(f"Puzzle 2 answer: {result_puzzle_2}")  
    puzzle_2(alt_instructions)

if __name__ == "__main__":
    main()