
import operator as op

def get_input(day_number: str, test: bool):
    # gets raw data from the input file and outputs as a list with each line as an element
    # provide the number of the day as a string and set test to True to run the test input

    if (test == True):
        file_name_add = "test"
    else:
        file_name_add = ""

    file_name = f"Input/day{day_number}{file_name_add}.txt"

    print(f"Retrieving input from: {file_name}, Test is {test}")

    with open(file_name, 'r') as file:
        raw_data = [line for line in file]
        return raw_data


def clean_list_ints(list):
    int_list = [int(el) for el in list]
    return int_list

def clean_list_strings(list):
    string_list = [el.replace("\n", "") for el in list]
    return string_list

operator_dict = {
    '==': op.eq,
    '!=': op.ne,
    '<': op.lt,
    '<=': op.le,
    '>': op.gt,
    '>=': op.ge,
    }

def compare_list_int(list, compare_op: str):
    # compares elements in a list of integers, looking one element ahead, counts if comparison equals to true
    # compare operators: >, <, >=, <=, ==, !=
    # stops looking after the previous to last item has been compared to last
    count = 0
    for index, elem, in enumerate(list):
        if index < len(list)-1:
            if operator_dict[compare_op](elem, list[index+1]):
                count+=1

    return count