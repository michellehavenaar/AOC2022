from Utils.tools import *
import re

def main():
    input = get_input("04", False)
    data = clean_list_strings(input)

    sections_per_pair_strings = [d.replace("-", ",") for d in data]
    sections_per_pair = [[int(s) for s in section.split(",")] for section in sections_per_pair_strings]


    def puzzle_1(list_of_sections):
        count = 0

        for section in list_of_sections:
            if section[0] >= section[2] and section[1] <= section[3]:
                count +=1
            
            elif section[2] >= section[0] and section[3] <= section[1]:
                count +=1

        return count

    def puzzle_2(list_of_sections):
        count = 0

        for section in list_of_sections:
            if section[0] >= section[2] and section[0] <= section [3]:
                count +=1
            elif section[1] >= section[2] and section[0] <= section [3]:
                count +=1

        return count
    


    result_puzzle_1 = puzzle_1(sections_per_pair)
    result_puzzle_2 = puzzle_2(sections_per_pair)
    
    print(f"Puzzle 1 answer: {result_puzzle_1}")
    print(f"Puzzle 2 answer: {result_puzzle_2}")   


if __name__ == "__main__":
    main()