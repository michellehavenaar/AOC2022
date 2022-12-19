from Utils.tools import *
import re

def main():
    input = get_input("15", False)
    data = clean_list_strings(input)

    report = [[el for el in re.findall("-?(?:\d+?)+", d)]for d in data]
    

    no_beacon_in_row = set()
    beacon_in_row = set()


    def puzzle_1(y_row):
        for r in report:
            x1, y1, x2, y2 = int(r[0]),int(r[1]),int(r[2]),int(r[3])
            man_dist = abs(x1 - x2) + abs(y1 -y2)
            if y2 == y_row:
                beacon_in_row.add(x2)
            if y1 < y_row:
                if (y1 + man_dist) >= y_row:
                    # if the perimiter of the signal scan reaches the y_row looking down
                    for i in range(man_dist + 1):
                        if (y1 + man_dist)-i >= y_row:
                            # from signal to right and from signal to left
                            # put the x coord in the set
                            no_beacon_in_row.add(x1 + i)
                            no_beacon_in_row.add(x1 - i)
            elif y1 > y_row:
                if (y1 - man_dist) <= y_row:
                    # if the perimiter of the signal scan reaches the y_row looking up
                    for i in range(man_dist + 1):
                        if (y1 - man_dist)+i <= y_row:
                            # from signal to right and from signal to left
                            # put the x coord in the set
                            no_beacon_in_row.add(x1 + i)
                            no_beacon_in_row.add(x1 - i)
            elif y1 == y_row:
                # signal is at the same row as y_row 
                # so all the coords from signal to left and to right for the man_dist should be added
                for i in range(man_dist + 1):
                    no_beacon_in_row.add(x1 + i)
                    no_beacon_in_row.add(x1 - i)

        # remove the actual beacons from the set
        no_beacon_in_row.difference_update(beacon_in_row)

        return len(no_beacon_in_row)


    def puzzle_2(range_start, range_end):
        gap = None
        for row in range(range_start,range_end + 1):
            row_list = []
            y_row = row
            # per row, look at each line in the report and calculate the range of x coords 
            # that would be covered by that signal in the row we are looking at
            # but make it sparse to save time (it still takes long but approx 1 minute is fine by me :D)
            for r in report:
                x1, y1, x2, y2 = int(r[0]),int(r[1]),int(r[2]),int(r[3])
                man_dist = abs(x1 - x2) + abs(y1 -y2)
                if y1 < y_row:
                    if (y1 + man_dist) >= y_row:
                        # if the perimiter of the signal scan reaches the y_row looking down
                        # take abs difference between the row of the signal and row we are looking at
                        # the x coord can be extended left and right by the man dist - the difference 
                        # between the signal row and row we are looking at
                        a_diff = abs(y1 - y_row)
                        left_bound = x1 - (man_dist - a_diff)
                        right_bound = x1 + (man_dist - a_diff)
                        if left_bound < range_start:
                            left_bound = range_start
                        if right_bound > range_end:
                            right_bound = range_end
                        row_list.append([left_bound, right_bound])
                elif y1 > y_row:
                    if (y1 - man_dist) <= y_row:
                        # if the perimiter of the signal scan reaches the y_row looking up
                        a_diff = abs(y1 - y_row)
                        left_bound = x1 - (man_dist - a_diff)
                        right_bound = x1 + (man_dist - a_diff)
                        if left_bound < range_start:
                            left_bound = range_start
                        if right_bound > range_end:
                            right_bound = range_end
                        row_list.append([left_bound, right_bound])
                elif y1 == y_row:
                    # signal is at the same row as y_row 
                    # so all the coords from signal to left and to right for the man_dist should be added
                    a_diff = abs(y1 - y_row)
                    left_bound = x1 - (man_dist - a_diff)
                    right_bound = x1 + (man_dist - a_diff)
                    if left_bound < range_start:
                        left_bound = range_start
                    if right_bound > range_end:
                        right_bound = range_end
                    row_list.append([left_bound, right_bound])
            # sort the list so the coordinates should overlap or attach to eachother
            # if they don't there is a gap
            # or the gap is at the start or the end
            row_list.sort()
            sparse = []

            for r in row_list:
                x1, x2 = r
                if len(sparse) == 0:
                    sparse = [x1,x2]
                else:
                    s1, s2 = sparse
                    if x1 >= s1 and x1 <= s2:
                        if x2 <= s2:
                            continue
                        else:
                            sparse[1] = x2
                            continue
                    elif x1 > s2 and (x1 - s2) == 1:
                        # attach on the right
                        sparse[1] = x2
                        continue
                    else:
                        # coord in list did not overlap or could not be attached, there is a gap
                        gap = x1 - 1
                        print(f"gap is {gap}")
                        break
                        
            if gap:
                return (gap * 4000000) + row
            if len(sparse) == 2:
                if sparse[0] != range_start and sparse[1] == range_end:
                    # gap is at the start
                    gap = range_start
                    return (gap * 4000000) + row
                elif sparse[0] == range_start and sparse[1] != range_end:
                    # gap is at the end
                    gap = range_end
                    return (gap * 4000000) + row
          

        

    result_puzzle_1 = puzzle_1(2000000)

    # beware this might take a minute (literally 68 seconds)
    result_puzzle_2 = puzzle_2(0, 4000000)

    
    print(f"Puzzle 1 answer: {result_puzzle_1}")
    print(f"Puzzle 2 answer: {result_puzzle_2}")  
    

if __name__ == "__main__":
    main()