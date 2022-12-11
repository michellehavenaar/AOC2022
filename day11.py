from Utils.tools import *
import re
import operator
import math

class MonkeyBusiness:
    
    def __init__(self):
        self.monkeys = []

    def add_monkey(self, monkey):
        self.monkeys.append(monkey)

    # def get_monkey(self, monkey_number):
    #     for monkey in self.monkeys:
    #         if monkey.number == monkey_number:
    #             return monkey
    
    def throw_item(self, item, monkey_number):
        for monkey in self.monkeys:
            if monkey.number == monkey_number:
                monkey.items.append(item)

    def most_active_monkeys(self, number):
        monkeys_activity = []
        for monkey in self.monkeys:
            monkeys_activity.append(monkey.activity)
        monkeys_activity.sort(reverse = True)
        return monkeys_activity[:number]






class Monkey:

    def __init__(self, number, items: list, operation: dict, test: dict):
        self.number = number
        self.items = items
        self.operation = operation
        self.test = test
        self.activity = 0

    def calculate_worry_lvl(self, item):
        operator = self.operation["operator"]
        input = self.operation["input"]
        if input == "old":
            new_worry_level = operator_dict[operator](item, item)
        else:
            new_worry_level = operator_dict[operator](item, int(input))
        return new_worry_level

    def perform_test(self, worry_lvl):
        mod = self.test["mod"]
        if worry_lvl % mod == 0:
            # print(f"worry level {worry_lvl} is divisible by {mod}")
            return self.test["true"]
        else:
            # print(f"worry level {worry_lvl} is not divisible by {mod}")
            return self.test["false"]


    


def main():
    
    input = get_input_in_blocks("11", False)
    
    notes = [i.split("\n") for i in input]


    def puzzle_1(rounds):

        monkey_business = MonkeyBusiness()

        for i in range(len(notes)):
            monkey_number = i
            starting_items = [int(el) for el in re.findall ("\d+", notes[i][1])]
            operation_raw = notes[i][2].split("= ")
            operation = operation_raw[1].split(" ")
            op = {
                "operator": operation[1],
                "input" : operation[2]
            }
            test_data = notes[i][3:]
            mod = [int(el) for el in re.findall("\d+", test_data[0])]
            true = [int(el) for el in re.findall("\d+", test_data[1])]
            false = [int(el) for el in re.findall("\d+", test_data[2])]
            test = {
                "mod": mod[0],
                "true": true[0],
                "false": false[0]
            }
            new_monkey = Monkey(monkey_number, starting_items, op, test)
            monkey_business.add_monkey(new_monkey)

        for _ in range(1, rounds +1):
            # print(f"round {i}")
            for monkey in monkey_business.monkeys:
                # monkey inspects item if there are items
                while len(monkey.items) > 0:
                    item = monkey.items.pop(0)
                    monkey.activity += 1
                    # print(f"Monkey number {monkey.number} inspects item with worry level: {item}")
                    # print(monkey.operation)
                    # worry intesifies
                    worry_level = monkey.calculate_worry_lvl(item)
                    # print(f"new worry level is {worry_level}")
                    # monkey gets bored
                    new_worry_level = operator.floordiv(worry_level, 3)
                    # print(f"worry level is decreased to {new_worry_level}")
                    receiving_monkey = monkey.perform_test(new_worry_level)
                    # monkey throws item
                    monkey_business.throw_item(new_worry_level, receiving_monkey)
                    # print(f"monkey throws item to monkey number {receiving_monkey}")
            
        for monkey in monkey_business.monkeys:
            print(monkey.items)
            print(monkey.activity)
        return(math.prod(monkey_business.most_active_monkeys(2)))



    def puzzle_2(rounds):

        monkey_business = MonkeyBusiness()

        for i in range(len(notes)):
            monkey_number = i
            starting_items = [int(el) for el in re.findall ("\d+", notes[i][1])]
            operation_raw = notes[i][2].split("= ")
            operation = operation_raw[1].split(" ")
            op = {
                "operator": operation[1],
                "input" : operation[2]
            }
            test_data = notes[i][3:]
            mod = [int(el) for el in re.findall("\d+", test_data[0])]
            true = [int(el) for el in re.findall("\d+", test_data[1])]
            false = [int(el) for el in re.findall("\d+", test_data[2])]
            test = {
                "mod": mod[0],
                "true": true[0],
                "false": false[0]
            }
            new_monkey = Monkey(monkey_number, starting_items, op, test)
            monkey_business.add_monkey(new_monkey)

        modulo = 1
        for monkey in monkey_business.monkeys:
            modulo *= monkey.test["mod"]
        print(f"product of all the mods is: {modulo}")

        for _ in range(1,rounds +1):
            # print(f"round {i}")
            for monkey in monkey_business.monkeys:
                # monkey inspects item if there are items
                while len(monkey.items) > 0:
                    item = monkey.items.pop(0)
                    monkey.activity += 1
                    # print(f"Monkey number {monkey.number} inspects item with worry level: {item}")
                    # print(monkey.operation)
                    # worry intesifies
                    worry_level = monkey.calculate_worry_lvl(item)
                    # print(f"new worry level is {worry_level}")
                    # monkey gets bored
                    # mod = monkey.test["mod"]
                    # remainder = worry_level % mod
                    new_worry_level = worry_level % modulo
                    # print(f"worry level is decreased to {new_worry_level}")
                    receiving_monkey = monkey.perform_test(new_worry_level)
                    # monkey throws item
                    monkey_business.throw_item(new_worry_level, receiving_monkey)
                    # print(f"monkey throws item to monkey number {receiving_monkey}")
            
        for monkey in monkey_business.monkeys:
            print(monkey.items)
            print(monkey.activity)
        return(math.prod(monkey_business.most_active_monkeys(2)))





        





    # result_puzzle_1 = puzzle_1(20)
    result_puzzle_2 = puzzle_2(10000)

    

    
    
    # print(f"Puzzle 1 answer: {result_puzzle_1}")
    print(f"Puzzle 2 answer: {result_puzzle_2}")  
    

if __name__ == "__main__":
    main()