
import operator as op
import re

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


def get_input_flat(day_number: str, test: bool):
    # gets raw data from the input file and outputs as a string from the open file
    # provide the number of the day as a string and set test to True to run the test input

    if (test == True):
        file_name_add = "test"
    else:
        file_name_add = ""

    file_name = f"Input/day{day_number}{file_name_add}.txt"

    print(f"Retrieving input from: {file_name}, Test is {test}")

    with open(file_name, 'r') as file:
        raw_data = file.read()
        return raw_data

def get_input_in_blocks(day_number: str, test: bool):
    # gets raw data from the input file and outputs as a list with each block as an element
    # provide the number of the day as a string and set test to True to run the test input

    if (test == True):
        file_name_add = "test"
    else:
        file_name_add = ""

    file_name = f"Input/day{day_number}{file_name_add}.txt"

    print(f"Retrieving input from: {file_name}, Test is {test}")

    with open(file_name, 'r') as file:
        raw_data = file.read()
        content_blocks = raw_data.split("\n\n")
        return content_blocks


def clean_list_ints(list):
    int_list = [int(el) for el in list]
    return int_list

def clean_list_strings(list):
    string_list = [el.replace("\n", "") for el in list]
    return string_list

def split_list_in_chunks(list, chunksize: int):
    # list split into chunks of size (chunksize)
    chunked_list = [list[i: i + chunksize] for i in range(0, len(list), chunksize)]
    return chunked_list




operator_dict = {
    '==': op.eq,
    '!=': op.ne,
    '<': op.lt,
    '<=': op.le,
    '>': op.gt,
    '>=': op.ge,
    '+': op.add,
    '-': op.sub,
    '*': op.mul,
    '/': op.truediv,
    '//': op.floordiv
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


def get_first_index(list:list, value):
    i = list.index(value)
    return i

def get_last_index(list: list, value):
    list.reverse()
    i = list.index(value)
    list.reverse()
    return (len(list) - i) - 1


def get_column(matrix, i):
    # gets a column in a matrix
    # matrix should be a 2d list
    # [[1,2,3],[4,5,6],[7,8,9]]
    # i = 1 gives [2,5,8]
        column = [row[i] for row in matrix]
        return column

def get_dict_key_by_value(val, my_dict):
    for key, value in my_dict.items():
        if val == value:
            return key


def merge_sort(arr, left_index, right_index):
    if left_index >= right_index:
        return
    
    mid = (left_index + right_index) //2
    merge_sort(arr, left_index, mid)
    merge_sort(arr, mid +1, right_index)
    merge(arr, left_index, right_index, mid)


def merge(arr, left_index, right_index, middle):

    # Make copies the 2 lists
    left_copy = arr[left_index:middle + 1]
    right_copy = arr[middle+1:right_index+1]

    # pointers
    left_copy_index = 0
    right_copy_index = 0
    sorted_index = left_index

    while left_copy_index < len(left_copy) and right_copy_index < len(right_copy):

        # If our left_copy has the smaller element, put it in the list at the position of the sorted pointer
        # and update pointers
        if left_copy[left_copy_index] <= right_copy[right_copy_index]:
            # print(f"left {left_copy[left_copy_index]} is smaller or equal then right {right_copy[right_copy_index]}")
            # print(f"insert left at sorted index {sorted_index}")
            arr[sorted_index] = left_copy[left_copy_index]
            left_copy_index += 1
        else:
            # print(f"left {left_copy[left_copy_index]} is greater or equal then right {right_copy[right_copy_index]}")
            # print(f"insert right at sorted index {sorted_index}")
            arr[sorted_index] = right_copy[right_copy_index]
            right_copy_index += 1

        sorted_index = sorted_index + 1

    # get the remainding elements in the copy lists
    while left_copy_index < len(left_copy):
        # print(f"remaining element {left_copy[left_copy_index]}")
        # print(f"insert at sorted index {sorted_index}")
        arr[sorted_index] = left_copy[left_copy_index]
        left_copy_index = left_copy_index + 1
        sorted_index = sorted_index + 1

    while right_copy_index < len(right_copy):
        # print(f"remaining element {right_copy[right_copy_index]}")
        # print(f"insert at sorted index {sorted_index}")
        arr[sorted_index] = right_copy[right_copy_index]
        right_copy_index = right_copy_index + 1
        sorted_index = sorted_index + 1