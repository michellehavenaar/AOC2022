from Utils.tools import *
import re
from collections import deque
from copy import deepcopy


def get_stack_from_list(stack_list, number):
    return stack_list[number-1]

def get_top_crates(stack_list):
    top_crates = ""
    for stack in stack_list:
        top_crate = stack.pop()
        top_crates += top_crate

    return top_crates


def main():
    input = get_input_in_blocks("05", False)

    stack_data_raw = input[0].split("\n")
    completed_stack_data = [stack.replace("    ", "0 ") for stack in stack_data_raw]
    stack_data = [[el for el in re.findall ("\w+", s)]for s in completed_stack_data[:-1]]

    procedure_data = input[1].split("\n")
    procedures = [[int(el) for el in re.findall ("\d+", p)] for p in procedure_data]

    stacks = []


    width = len(stack_data[0])


    # get the column which is the data per stack
    for i in range(width):
        column_of_crates = get_column(stack_data, i)
        initial_stack = deque()
        for c in reversed(column_of_crates):
            if c != "0":
                initial_stack.append(c) 
        stacks.append(initial_stack)

    # make a copy of the initial stacks to use in the second puzzle
    stacks_for_puzzle_2 = deepcopy(stacks)


    def puzzle_1(list_of_stacks):
        for procedure in procedures:
            amount = procedure[0]
            start = procedure[1] 
            end = procedure[2]
            move_from = get_stack_from_list(list_of_stacks, start)
            move_to = get_stack_from_list(list_of_stacks, end)
            for _ in range(amount):
                crate = move_from.pop()
                move_to.append(crate)

        # now get all the top crates
        top_crates = get_top_crates(list_of_stacks)

        return top_crates

    def puzzle_2(list_of_stacks):
        for procedure in procedures:
            amount = procedure[0]
            start = procedure[1] 
            end = procedure[2]
            move_from = get_stack_from_list(list_of_stacks, start)
            move_to = get_stack_from_list(list_of_stacks, end)
            crates = []
            for _ in range(amount):
                crate = move_from.pop()
                crates.insert(0,crate)
            move_to.extend(crates)
        
        # now get all the top crates
        top_crates = get_top_crates(list_of_stacks)
        
        return top_crates




    result_puzzle_1 = puzzle_1(stacks)
    result_puzzle_2 = puzzle_2(stacks_for_puzzle_2)
    
    print(f"Puzzle 1 answer: {result_puzzle_1}")
    print(f"Puzzle 2 answer: {result_puzzle_2}")   


if __name__ == "__main__":
    main()