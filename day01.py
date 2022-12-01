from Utils.tools import *


def main():

    input = get_input_in_blocks("01", False)

    data = [el.split("\n") for el in input]

    calories_per_elf = [clean_list_ints(d) for d in data]

    total_calories_per_elf = [sum(elf) for elf in calories_per_elf]
    
    def puzzle1(list_of_totals):
        return(max(list_of_totals))

    def puzzle2(list_of_totals):

        top_three = []
        for _ in range(3):
            max_elf = max(list_of_totals)
            top_three.append(max_elf)
            max_index = list_of_totals.index(max_elf)
            list_of_totals.pop(max_index)

        return sum(top_three)



    result_puzzle1 = puzzle1(total_calories_per_elf)
    result_puzzle2 = puzzle2(total_calories_per_elf)
    print(f"Puzzle 1 answer: {result_puzzle1}")
    print(f"Puzzle 2 answer: {result_puzzle2}")


if __name__ == "__main__":
    main()