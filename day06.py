from Utils.tools import *

datastream = get_input_flat("06", False)


def main():

    def puzzle_1(data):
        for i in range(len(data)):
            if i > 3:
                start = i - 4
                sequence = data[start:i]
                sequence_set = set(sequence)
                if len(sequence) == len(sequence_set):
                    return i
        
    def puzzle_2(data):
        for i in range(len(data)):
            if i > 13:
                start = i - 14
                sequence = data[start:i]
                sequence_set = set(sequence)
                if len(sequence) == len(sequence_set):
                    return i




    result_puzzle_1 = puzzle_1(datastream)
    result_puzzle_2 = puzzle_2(datastream)
    
    print(f"Puzzle 1 answer: {result_puzzle_1}")
    print(f"Puzzle 2 answer: {result_puzzle_2}")   


if __name__ == "__main__":
    main()