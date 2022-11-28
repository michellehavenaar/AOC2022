from Utils.tools import *


def main():

    data = data = get_input("202101", True)

    def puzzle1(data):
        depth_measurements = clean_list_ints(data)

        answer = compare_list_int(depth_measurements, "<")
        return answer

            
    def puzzle2(data):
        depth_measurements = clean_list_ints(data)

        list_of_sums = []

        for index, elem in enumerate(depth_measurements):
            if index < len(depth_measurements)-2:
                three_measurement_window = [elem, depth_measurements[index+1], depth_measurements[index+2]]
                sum_of_measurements = sum(three_measurement_window)
                list_of_sums.append(sum_of_measurements)

        answer = compare_list_int(list_of_sums, "<")
        return answer


    

    result_puzzle1 = puzzle1(data)
    result_puzzle2 = puzzle2(data)    

    print(f"Answer for puzzle 1: {result_puzzle1}")
    print(f"Answer for puzzle 2: {result_puzzle2}")


if __name__ == "__main__":
    main()