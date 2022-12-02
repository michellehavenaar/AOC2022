from Utils.tools import *


shapes = {
    "A" : "rock",
    "B" : "paper",
    "C" : "scissors",
    "X": "rock",
    "Y": "paper",
    "Z": "scissors"
}

shape_selected = {
    "rock" : 1,
    "paper" : 2,
    "scissors" : 3
}

outcome = { 
    "X": 0,
    "Y": 3,
    "Z": 6
}



def calc_outcome(round):
    score = 0
    your_shape = shapes[round[1]]
    #add score for the shape selected
    score += shape_selected[your_shape]
    if shapes[round[0]] == shapes[round[1]]:
        score+= 3
    elif shapes[round[0]] == "rock":
        if shapes[round[1]] == "paper":
            score+=6
    elif shapes[round[0]] == "paper":
        if shapes[round[1]] == "scissors":
            score+=6
    elif shapes[round[0]] == "scissors":
        if shapes[round[1]] == "rock":
            score+=6
    return score

def calc_outcome2(round):
    score = 0
    #add score for win,lose,draw
    score += outcome[round[1]]
    if score == 0:
        if shapes[round[0]] == "rock":
            score += shape_selected["scissors"]
        elif shapes[round[0]] == "paper":
            score += shape_selected["rock"]
        elif shapes[round[0]] == "scissors":
            score += shape_selected["paper"]

    elif score == 3:
        if shapes[round[0]] == "rock":
            score += shape_selected["rock"]
        elif shapes[round[0]] == "paper":
            score += shape_selected["paper"]
        elif shapes[round[0]] == "scissors":
            score += shape_selected["scissors"]
    
    elif score == 6:
        if shapes[round[0]] == "rock":
            score += shape_selected["paper"]
        elif shapes[round[0]] == "paper":
            score += shape_selected["scissors"]
        elif shapes[round[0]] == "scissors":
            score += shape_selected["rock"]
    
    return score




def main():
    input = get_input("02", False)

    data = clean_list_strings(input)
    strategy_guide = [d.split(" ") for d in data]


    def puzzle1(strategy_guide):
        total_score = 0
        for round in strategy_guide:
            result = calc_outcome(round)
            total_score += result
    
        return(total_score)

    def puzzle2(strategy_guide):
        total_score = 0
        for round in strategy_guide:
            result = calc_outcome2(round)
            total_score += result
        
        return(total_score)


    result_puzzle1 = puzzle1(strategy_guide)
    result_puzzle2 = puzzle2(strategy_guide)
    
    print(f"Puzzle 1 answer: {result_puzzle1}")
    print(f"Puzzle 2 answer: {result_puzzle2}")
   

if __name__ == "__main__":
    main()