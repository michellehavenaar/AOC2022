from Utils.tools import *
import re

def main():
    input = get_input("15", True)
    # print(input)
    data = clean_list_strings(input)
    # print(data)

    report = [[el for el in re.findall("-?(?:\d+?)+", d)]for d in data]
    # print(report)
    y_row = 10

    for r in report:
        x1, y1, x2, y2 = int(r[0]),int(r[1]),int(r[2]),int(r[3])
        print(x1, y1, x2, y2)
        man_dist = abs(x1 - x2) + abs(y1 -y2)
        print(man_dist)
        if y1 < y_row:
            if (y1 + man_dist) >= y_row:
                print("interesting")
            else:
                print("will not reach y row")
        elif y1 > y_row:
            if (y1 - man_dist) <= y_row:
                print("interesting")
            else:
                print("will not reach y row")
        elif y1 == y_row:
            print("interesting")
        

    # result_puzzle_1 = puzzle_1(scan_list)
    # result_puzzle_2 = puzzle_2(scan_list)

    
    # print(f"Puzzle 1 answer: {result_puzzle_1}")
    # print(f"Puzzle 2 answer: {result_puzzle_2}")  
    

if __name__ == "__main__":
    main()