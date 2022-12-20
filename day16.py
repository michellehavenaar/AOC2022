from Utils.tools import *
import re
from collections import deque


class Valve():
    def __init__(self, name, flow_rate, neighbours):
        self.name = name
        self.flow_rate = flow_rate
        self.neighbours = neighbours
        self.distances_to_all = {}

    def update_distances(self, valve_name, distance):
        self.distances_to_all[valve_name] = distance



def main():
    input = get_input("16", True)
    data = clean_list_strings(input)
    report = [d.split(";") for d in data]

    # dict of all the valves
    valves = {}

    pattern_name = re.compile(r"\b[A-Z]{2}\b")
    pattern_flow_rate = re.compile(r"\d+")

    for r in report:
        valve_name = pattern_name.findall(r[0])
        flow_rate = pattern_flow_rate.findall(r[0])
        neighbours = pattern_name.findall(r[1])
        new_valve = Valve(valve_name[0], int(flow_rate[0]), neighbours)
        valves[new_valve.name] = new_valve


    # bfs to calculate the distances from each node to each node
    def bfs(start, destination):
        visited.append(start.name)
        queue.append([start, 0])
        temp_list = []

        while queue:
            current = queue.popleft()
            current_valve, current_dist = current
            if current_valve.name == destination.name:
                start.update_distances(destination.name, current_dist)
                break
            
            for neighbour in current_valve.neighbours:
                if neighbour not in visited:
                    visited.append(neighbour)
                    temp_list.append(neighbour)
                    neighbour_obj = valves[neighbour]
                    neighbour_dist = current_dist + 1
                    queue.append([neighbour_obj, neighbour_dist])
           


    # calculate the distances from each node to each node
    for valve_s in valves:
        start = valves[valve_s]
        for valve_e in valves:
            end = valves[valve_e]

            visited = []
            queue = deque()

            bfs(start, end)

    
    for valve in valves:
        print(valves[valve].name)
        print(valves[valve].distances_to_all)

    



    # visited = set()
    # stack = deque()
    # time_left = 30
    # t = 0

    
            



   





















    # result_puzzle_1 = puzzle_1(scan_list)
    # result_puzzle_2 = puzzle_2(scan_list)

    
    # print(f"Puzzle 1 answer: {result_puzzle_1}")
    # print(f"Puzzle 2 answer: {result_puzzle_2}")  
    

if __name__ == "__main__":
    main()  