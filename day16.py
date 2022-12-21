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


class State():
    def __init__(self, position:str, time:int, unopened:list, valves_dict:dict, score = 0):
        self.position = position
        self.valve = valves_dict[position]
        self.time = time
        self.unopened = unopened
        self.score = score

    def is_terminal_state(self):
        if len(self.unopened) == 0:
            return True 
        else:
            return False






def main():
    input = get_input("16", False)
    data = clean_list_strings(input)
    report = [d.split(";") for d in data]

    # dict of all the valves
    valves = {}
    unopened_valves = []

    pattern_name = re.compile(r"\b[A-Z]{2}\b")
    pattern_flow_rate = re.compile(r"\d+")

    for r in report:
        valve_name = pattern_name.findall(r[0])
        flow_rate = pattern_flow_rate.findall(r[0])
        neighbours = pattern_name.findall(r[1])
        new_valve = Valve(valve_name[0], int(flow_rate[0]), neighbours)
        valves[new_valve.name] = new_valve
        if int(flow_rate[0]) > 0:
            unopened_valves.append(valve_name[0])


    

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

    
    # # create the starting state
    starting_state = State("AA", 30, unopened_valves, valves)
    

    def generate_states(state):
        new_states = []
        # make a new state for all the valves that have not been opened yet
        # and open the valve, this takes 1 minute off the time left
        for u in state.unopened:
            position = u
            # first check if there is time left to reach the valve and open it
            # (current time left - the time it takes to travel to the unopend valve) - 1 minute to open it
            time_left = (state.time - state.valve.distances_to_all[position]) - 1
            if time_left > 0:
                # get the valve object we want to travel to 
                unopened_valve = valves[position]
                score = state.score + open_valve(unopened_valve, time_left)
                # create a new unopened list (minus the one we just opened)
                new_unopened = [u for u in state.unopened if u != position]
                new_state = State(position, time_left, new_unopened, valves, score)
                new_states.append(new_state)
        return new_states

    def open_valve(valve, time_left):
        # releases pressure per minute of time left
        score = valve.flow_rate * time_left
        return score

    
        
    def dfs(state):
        if state.is_terminal_state():
            return state.score

        new_states = generate_states(state)
        # if there were no new states that could be made
        if len(new_states) == 0:
            return state.score

        best_score = 0

        for s in new_states:
            score_s = dfs(s)
            best_score = max(best_score, score_s)

        return best_score

    
    result = dfs(starting_state)
    print(result)

    




    # result_puzzle_1 = puzzle_1("AA")
    # # result_puzzle_2 = puzzle_2(scan_list)

    
    # print(f"Puzzle 1 answer: {result_puzzle_1}")
    # # print(f"Puzzle 2 answer: {result_puzzle_2}")  
    

if __name__ == "__main__":
    main()  