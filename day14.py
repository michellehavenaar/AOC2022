from Utils.tools import *


def create_lines(path):
    path_coords_list = []
    for i in range(len(path)-1):
        start_x,start_y = path[i]
        end_x, end_y = path[i+1]
        diff_x = abs(int(start_x) - int(end_x))
        diff_y = abs(int(start_y) - int(end_y))
        if start_x != end_x:
            # create horizontal line
            if start_x < end_x:
                hor_line = [(int(start_x) + i, int(start_y)) for i in range(diff_x+1)]
                path_coords_list.append(hor_line)
            else:
                hor_line = [(int(start_x) - i, int(start_y)) for i in range(diff_x+1)]
                path_coords_list.append(hor_line)
        else:
            # create vertical line
            if start_y < end_y:
                ver_line = [(int(start_x), int(start_y) + i) for i in range(diff_y+1)]
                path_coords_list.append(ver_line)
            else:
                ver_line = [(int(start_x), int(start_y) - i) for i in range(diff_y+1)]
                path_coords_list.append(ver_line)
    return(path_coords_list)







def main():
    input = get_input("14", False)
    raw_data = clean_list_strings(input)

    data = [rd.split(" -> ") for rd in raw_data]
    
    scan_list = [[tuple(el.split(",")) for el in d] for d in data]
    



    def puzzle_1(scan_list):

        scan = {}
        for path in scan_list:
            path_coords = create_lines(path)
            for line in path_coords:
                for coord in line:
                    x,y = coord
                    if y in scan:
                        scan[y].add(x)
                    else:
                        scan[y] = {x}

        # find the lowest row
        lowest_row = max(scan)
        

        # drop sand

        sand_unit = 0

        edge_reached = False

        while not edge_reached:
            sand_unit +=1
        
            unblocked = True
            x = 500
            y = 0

            while unblocked:
                # try one down
                new_y = y + 1
                if new_y > lowest_row:
                    edge_reached = True
                    break
                if new_y in scan:
                    if x in scan[new_y]:
                        # try one down and one left
                        new_x = x - 1
                        if new_x in scan[new_y]:
                            # try one down and one right
                            new_x = x + 1
                            if new_x in scan[new_y]:
                                # sand unit stops
                                if y in scan:
                                    scan[y].add(x)
                                    unblocked = False
                                else:
                                    scan[y] = {x}
                            else:
                                x = new_x
                                y = new_y
                        else: 
                            x = new_x
                            y = new_y
                    else:
                        y = new_y
                else:
                    y = new_y
                

        
        return (sand_unit -1)

    def puzzle_2(scan_list):

        scan = {}
        for path in scan_list:
            path_coords = create_lines(path)
            for line in path_coords:
                for coord in line:
                    x,y = coord
                    if y in scan:
                        scan[y].add(x)
                    else:
                        scan[y] = {x}

        # find the lowest row
        lowest_row = max(scan)
        # create floor
        floor = lowest_row + 2
        

        # drop sand

        sand_unit = 0

        source_blocked = False

        while not source_blocked:
            sand_unit +=1

            unblocked = True
            x = 500
            y = 0

            while unblocked:
                # try one down
                new_y = y + 1
                if new_y in scan:
                    if x in scan[new_y]:
                        # try one down and one left
                        new_x = x - 1
                        if new_x in scan[new_y]:
                            # try one down and one right
                            new_x = x + 1
                            if new_x in scan[new_y]:
                                # sand unit stops
                                if y in scan:
                                    scan[y].add(x)
                                    unblocked = False
                                    if x == 500 and y == 0:
                                        source_blocked = True
                                        break
                                else:
                                    scan[y] = {x}
                            else:
                                x = new_x
                                y = new_y
                        else: 
                            x = new_x
                            y = new_y
                    else:
                        y = new_y
                elif new_y == floor: 
                    # sand unit stops
                    if y in scan:
                        scan[y].add(x)
                        unblocked = False
                    else:
                        scan[y] = {x}

                else:
                    y = new_y
                
        
        return (sand_unit)
    
            
        
 





            

    result_puzzle_1 = puzzle_1(scan_list)
    result_puzzle_2 = puzzle_2(scan_list)

    
    print(f"Puzzle 1 answer: {result_puzzle_1}")
    print(f"Puzzle 2 answer: {result_puzzle_2}")  
    

if __name__ == "__main__":
    main()