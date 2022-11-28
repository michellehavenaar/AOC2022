from Utils.tools import *

def main():

    data = data = get_input("202102", True)

    def puzzle1(data):
        command_data = clean_list_strings(data)
        split_commands = [command.split(" ") for command in command_data]
        list_of_commands = [tuple(c) for c in split_commands]

        horizontal_pos = 0
        depth = 0
        for x, y in list_of_commands:
            if x == "forward":
                horizontal_pos += int(y)
            elif x == "down":
                depth += int(y)
            elif x == "up":
                depth -= int(y)

        answer = horizontal_pos * depth
        return answer



    def puzzle2(data):
        command_data = clean_list_strings(data)
        split_commands = [command.split(" ") for command in command_data]
        list_of_commands = [tuple(c) for c in split_commands]

        horizontal_pos = 0
        depth = 0
        aim = 0
        for x, y in list_of_commands:
            if x == "forward":
                horizontal_pos += int(y)
                depth += (aim * int(y))
            elif x == "down":
                aim += int(y)
            elif x == "up":
                aim -= int(y)
            # print(f"Horizontal position: {horizontal_pos}")
            # print(f"Depth: {depth}")
            # print(f"Aim: {aim}")


        answer = horizontal_pos * depth
        return answer

    
    
    
    result_puzzle1 = puzzle1(data)
    result_puzzle2 = puzzle2(data)



    print(f"Answer for puzzle 1: {result_puzzle1}")
    print(f"Answer for puzzle 2: {result_puzzle2}")
        





if __name__ == "__main__":
    main()