from Utils.tools import *

def main():
    input = get_input("08", False)
    data = clean_list_strings(input)
    grid = [[int(el) for el in d]for d in data]
    
    def puzzle_1(grid):
        visible_trees_counter = 0
        width = len(grid[0])
        height = len(grid)
        outside_trees = (width*2) + (height*2) - 4

        for index, row in enumerate(grid[1:-1]):
            row_number = index+1
            for i in range(1, len(row)-1):
                # look to right
                trees_right = [tree for tree in row[i+1:]]
                # sort the list so the highest tree is in the front then we only check the first element
                trees_right.sort(reverse=True)
                if row[i] > trees_right[0]:
                    visible_trees_counter +=1
                else:
                    # look to left
                    trees_left = [tree for tree in row[:i]]
                    trees_left.sort(reverse=True)
                    if row[i] > trees_left[0]:
                        visible_trees_counter +=1
                    else:
                        # look up
                        # get column
                        col = get_column(grid,i)
                        trees_up = [tree for tree in col[:row_number]]
                        trees_up.sort(reverse=True)
                        if col[row_number] > trees_up[0]:
                            visible_trees_counter +=1
                        else:
                            # look down
                            trees_down = [tree for tree in col[row_number+1:]]
                            trees_down.sort(reverse=True)
                            if col[row_number] > trees_down[0]:
                                visible_trees_counter +=1
                            else:
                                # tree is not visible AT ALL
                                pass

        return(visible_trees_counter + outside_trees)

    def puzzle_2(grid):
        viewing_distances = []
        for index, row in enumerate(grid[1:-1]):
            row_number = index+1
            for i in range(1, len(row)-1):
                # look to right
                trees_right = [tree for tree in row[i+1:]]
                viewing_distance_right = 0
                for t in trees_right:
                    if row[i] >= t:
                        viewing_distance_right +=1
                        if row[i] == t:
                            # view is blocked
                            break
                    elif row[i] < t:
                        viewing_distance_right +=1
                        # view is blocked
                        break

                # look to left
                # put trees in list in reverse order for correct viewing order
                trees_left = [tree for tree in reversed(row[:i])]
                viewing_distance_left = 0
                for t in trees_left:
                    if row[i] >= t:
                        viewing_distance_left +=1
                        if row[i] == t:
                            # view is blocked
                            break
                    elif row[i] < t:
                        viewing_distance_left +=1
                        # view is blocked
                        break

                # look up
                # get column
                col = get_column(grid,i)
                trees_up = [tree for tree in reversed(col[:row_number])]
                viewing_distance_up = 0
                for t in trees_up:
                    if row[i] >= t:
                        viewing_distance_up +=1
                        if row[i] == t:
                            # view is blocked
                            break
                    elif row[i] < t:
                        viewing_distance_up +=1
                        # view is blocked
                        break
            
                # look down
                trees_down = [tree for tree in col[row_number+1:]]
                viewing_distance_down = 0
                for t in trees_down:
                    if row[i] >= t:
                        viewing_distance_down +=1
                        if row[i] == t:
                            # view is blocked
                            break
                    elif row[i] < t:
                        viewing_distance_down +=1
                        # view is blocked
                        break
                viewing_distance = viewing_distance_right * viewing_distance_left * viewing_distance_up * viewing_distance_down
                viewing_distances.append(viewing_distance)
        return max(viewing_distances)
            


    result_puzzle_1 = puzzle_1(grid)
    result_puzzle_2 = puzzle_2(grid)
    
    print(f"Puzzle 1 answer: {result_puzzle_1}")
    print(f"Puzzle 2 answer: {result_puzzle_2}")  

if __name__ == "__main__":
    main()