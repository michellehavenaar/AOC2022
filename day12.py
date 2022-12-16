from Utils.tools import *
from collections import deque


class Node():

    def __init__(self, position: tuple, value: str, elevation: int):
        self.distance = 0
        self.position = position
        self.value = value
        self.elevation = elevation



def look_left(current_pos: tuple, grid: list):
    x, y = current_pos
    if x != 0:
        value = grid[y][x-1]
        elevation = ord(value)
        neighbour = Node((x - 1, y), value, elevation)
        return neighbour
    else:
        return None

def look_right(current_pos: tuple, grid: list, width):
    x, y = current_pos
    if x < width-1:
        value = grid[y][x+1]
        elevation = ord(value)
        neighbour = Node((x + 1, y), value, elevation)
        return neighbour
    else:
        return None

def look_up(current_pos: tuple, grid: list):
    x, y = current_pos
    if y != 0:
        value = grid[y - 1][x]
        elevation = ord(value)
        neighbour = Node((x, y - 1), value, elevation)
        return neighbour
    else:
        return None

def look_down(current_pos: tuple, grid: list, height):
    x, y = current_pos
    if y < height-1:
        value = grid[y + 1][x]
        elevation = ord(value)
        neighbour = Node((x, y + 1), value, elevation)
        return neighbour
    else:
        return None

def main():


    input = get_input("12", False)
    data = clean_list_strings(input)
    

    grid = [[el for el in d]for d in data]
<<<<<<< HEAD
    # print(grid)

    width = len(grid[0])
    height = len(grid)
    # print(height)

    visited = []
    queue = []

    # find the starting point
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "S":
                start = Node((j,i), "S", ord("a"))



    print(start.position)


    # looking at start node first
    queue.append(start)

    end_found = False
    end_node = None

    while len(queue) > 0 or end_found:
        # get top of the queue
        current_node = queue.pop(0)
        # print(f"looking at node {current_node.position}")
        if current_node.value =="E":
            print("End found")
            # End is found
            end_found = True
            end_node = current_node
            break

        
        # look at all neighbours
        neighbours = [
            look_right(current_node.position, grid, width),
            look_left(current_node.position, grid),
            look_up(current_node.position, grid),
            look_down(current_node.position, grid, height)
        ]

        # print(neighbours)
        for neighbour in neighbours:
            if neighbour is not None:
                if neighbour.value == "E":
                    neighbour.elevation = 122
                # if neighbour is not yet visited
                # print(neighbour.position, neighbour.value)
                if neighbour.position in visited:
                    # print("node was allready visited")
                    continue
                else:
                # if not is_visited(visited, neighbour["pos"]):
                    if (neighbour.elevation - current_node.elevation) <= 1:
                        # valid move
                        # create child node
                        neighbour.parent = current_node
                        # print(f"adding new node {neighbour.position} to the queue with value {neighbour.value}")
                        queue.append(neighbour)

        # mark current node as visited
        visited.append(current_node.position)
        # print (f"length of queue is {len(queue)} and end found is {end_found}")

    print(f"end node is found at {end_node.position} with value { end_node.value}")


    # trace back from end node
    path = []
    trace_back = True
    node = end_node
    while trace_back:
        if node.parent == None:
            trace_back = False
        else:
            path.append(node.position)
            node = node.parent
    # print(path)
    print(len(path))

        
=======
>>>>>>> 8233b555d6e447753b467ed7d3a74beb53852eb0

    def puzzle_1(grid):


        width = len(grid[0])
        height = len(grid)


        visited = []
        queue = deque()

        # find the starting point
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "S":
                    start = Node((j,i), "S", ord("a"))




        # looking at start node first
        queue.append(start)

        end_node = None

        while len(queue) > 0:
            # get top of the queue
            current_node = queue.popleft()
            if current_node.value =="E":
                print("End found")
                # End is found
                end_node = current_node
                break

            
            # look at all neighbours
            neighbours = [
                look_right(current_node.position, grid, width),
                look_left(current_node.position, grid),
                look_up(current_node.position, grid),
                look_down(current_node.position, grid, height)
            ]

            for neighbour in neighbours:
                if neighbour is not None:
                    if neighbour.value == "E":
                        neighbour.elevation = 122
                    # if neighbour is not yet visited
                    if neighbour.position in visited:
                        continue
                    else:
                        if (neighbour.elevation - current_node.elevation) <= 1:
                            # valid move
                            # create child node
                            neighbour.distance = current_node.distance + 1
                            queue.append(neighbour)
                            visited.append(neighbour.position)


        print(f"end node is found at {end_node.position} with value { end_node.value} and distance {end_node.distance}")
        return end_node.distance

    def puzzle_2(grid):

        width = len(grid[0])
        height = len(grid)


        visited = []
        queue = deque()

        # find the end point and use it as the start
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "E":
                    start = Node((j,i), "E", ord("z"))



        # looking at start node first
        queue.append(start)

        end_node = None

        while len(queue) > 0:
            # get top of the queue
            current_node = queue.popleft()
            if current_node.value =="a" or current_node.value == "S":
                print("End found")
                # End is found
                end_node = current_node
                break

            
            # look at all neighbours
            neighbours = [
                look_right(current_node.position, grid, width),
                look_left(current_node.position, grid),
                look_up(current_node.position, grid),
                look_down(current_node.position, grid, height)
            ]

            for neighbour in neighbours:
                if neighbour is not None:
                    if neighbour.value == "S":
                        neighbour.elevation = 97
                    # if neighbour is not yet visited
                    if neighbour.position in visited:
                        continue
                    else:
                        if (neighbour.elevation - current_node.elevation) >= -1:
                            # valid move
                            # create child node
                            neighbour.distance = current_node.distance + 1
                            queue.append(neighbour)
                            visited.append(neighbour.position)


        print(f"end node is found at {end_node.position} with value { end_node.value} and distance {end_node.distance}")
        return end_node.distance


   



    result_puzzle_1 = puzzle_1(grid)
    result_puzzle_2 = puzzle_2(grid)

    

    
    
    print(f"Puzzle 1 answer: {result_puzzle_1}")
    print(f"Puzzle 2 answer: {result_puzzle_2}")  
    

if __name__ == "__main__":
    main()