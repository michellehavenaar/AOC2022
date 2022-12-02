from Utils.tools import *


shapes = {
    "A" : "rock",
    "B" : "paper",
    "C" : "scissors",
    "X": "rock",
    "Y": "paper",
    "Z": "scissors"
}

shape_points = {
    "rock" : 1,
    "paper" : 2,
    "scissors" : 3
}

predetermined_outcome = { 
    "X": 0,
    "Y": 3,
    "Z": 6
}

rules = {
    # [rock,paper,scissors]
    # list holds the resulting points for that combination
    # 0 = lose, 3 = draw, 6 = win
    "rock" : [3,6,0],
    "paper" : [0,3,6],
    "scissors" : [6,0,3]
}

index = {
    "rock": 0,
    "paper": 1,
    "scissors": 2
}

def calculate_score(round):
    score = 0
    elf_shape = shapes[round[0]]
    your_shape = shapes[round[1]]
    score += shape_points[your_shape]
    possible_outcomes = rules[elf_shape]
    round_outcome = possible_outcomes[index[your_shape]]
    score += round_outcome
    return score

def calculate_score2(round):
    score = 0
    elf_shape = shapes[round[0]]
    score += predetermined_outcome[round[1]]
    required_shape_index = rules[elf_shape].index(predetermined_outcome[round[1]])
    # get key by value from dict index
    required_shape = get_dict_key_by_value(required_shape_index, index)
    score += shape_points[required_shape]
    return score


def main():
    input = get_input("02", False)

    data = clean_list_strings(input)
    strategy_guide = [d.split(" ") for d in data]

    def puzzle_1(strategy_guide):
        total_score = 0

        for round in strategy_guide:
            result = calculate_score(round)
            total_score += result
        return total_score

    def puzzle_2(strategy_guide):
        total_score = 0

        for round in strategy_guide:
            result = calculate_score2(round)
            total_score += result
        return total_score



    result_puzzle_1 = puzzle_1(strategy_guide)
    result_puzzle_2 = puzzle_2(strategy_guide)
    
    print(f"Puzzle 1 answer: {result_puzzle_1}")
    print(f"Puzzle 2 answer: {result_puzzle_2}")
   

if __name__ == "__main__":
    main()