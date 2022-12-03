from Utils.tools import *

priorities = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def main():
    input = get_input("03", False)
    data = clean_list_strings(input)
    backpacks = []
    

    for d in data:
        comp1, comp2 = d[: len(d)//2], d[len(d)//2 :]
        backpack = [comp1, comp2]
        backpacks.append(backpack)

    groups = split_list_in_chunks(data, 3)

    
    def puzzle_1(list_of_backpacks):

        sum_of_priorities = 0
        for backpack in list_of_backpacks:
            backpack_comp1_set = set(backpack[0])
            backpack_comp2_set = set(backpack[1])

            intersection = backpack_comp1_set.intersection(backpack_comp2_set)

            duplicate = intersection.pop()

            priority = priorities.index(duplicate) + 1
            sum_of_priorities += priority

        return sum_of_priorities

    def puzzle_2(list_of_groups):

        sum_of_priorities = 0
        for group in list_of_groups:
            backpack_1 = set(group[0])
            backpack_2 = set(group[1])
            backpack_3 = set(group[2])

            #find intersections of three sets
            intersection_first_two_sets = backpack_1.intersection(backpack_2)
            intersection = intersection_first_two_sets.intersection(backpack_3)

            duplicate = intersection.pop()

            priority = priorities.index(duplicate) + 1
            sum_of_priorities += priority
        return sum_of_priorities


            

    


        
    result_puzzle_1 = puzzle_1(backpacks)
    result_puzzle_2 = puzzle_2(groups)
    
    print(f"Puzzle 1 answer: {result_puzzle_1}")
    print(f"Puzzle 2 answer: {result_puzzle_2}")



if __name__ == "__main__":
    main()