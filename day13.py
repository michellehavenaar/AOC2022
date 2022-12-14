from Utils.tools import *
import json


def main():
    input = get_input_in_blocks("13", True)
    # print(input)

    distress_signal = [[json.loads(packet) for packet in pair.split()]for pair in input ]
    print(distress_signal)
   
    # result_puzzle_1 = puzzle_1(grid)
    # result_puzzle_2 = puzzle_2(grid)

    
    # print(f"Puzzle 1 answer: {result_puzzle_1}")
    # print(f"Puzzle 2 answer: {result_puzzle_2}")  
    

if __name__ == "__main__":
    main()