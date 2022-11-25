
def get_input(day_number: str, test: bool):
    #gets raw data from the input file and outputs as a list with each line as an element
    if (test == True):
        file_name_add = "test"
    else:
        file_name_add = ""

    file_name = f"Input/day{day_number}{file_name_add}.txt"

    print(f"Retrieving input from: {file_name}, Test is {test}")

    with open(file_name, 'r') as file:
        raw_data = [line for line in file]
        return raw_data


def get_input_2(day_number: str, test: bool):
    if (test == True):
        file_name_add = "test"
    else:
        file_name_add = ""

    file_name = f"Input/day{day_number}{file_name_add}.txt"

    print(f"Retrieving input from: {file_name}, Test is {test}")

    with open(file_name, 'r') as file:
        raw_data = file.read()
        data = raw_data.split(",")

        return data

#with open('Input/day00.txt', 'r') as file:
        #file_content = file.read()
        #print(file_content)