from Utils.tools import *
import json



def compare(left, right):

    #check the longest list
    longest_list_len = max(len(left), len(right))

    for i in range(longest_list_len):
        if i >= len(left):
            # outgrew the range of left
            # print(f"left side is smaller, so inputs are in the RIGHT order")
            sorted = True
            return sorted
        elif i >= len(right):
            # outgrew the range of right
            # print(f"right side is smaller, so inputs are in the WRONG order")
            sorted = False
            return sorted
        l, r = left[i], right[i]

        if isinstance(l, int) and isinstance(r, int):
            if l < r:
                # print(f"left side is smaller, so inputs are in the RIGHT order")
                sorted = True
            elif l > r:
                # print(f"right side is smaller, so inputs are in the WRONG order")
                sorted = False
            else:
                # print(f"left and right are equal, continue")
                sorted = None
                continue

        elif isinstance(l, list) and isinstance(r, list):
            sorted = compare(l,r)

        elif isinstance(l, int) and isinstance(r, list):
            new_left = [l]
            sorted = compare(new_left,r)
        elif isinstance(l, list) and isinstance(r, int):
            new_right = [r]
            sorted = compare(l, new_right)

        if sorted is not None:
            return sorted
            
    
        
   
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
    # use the compare function to determine if they are in the right order
    # ordered means left is smaller
        is_sorted = compare(left_copy[left_copy_index], right_copy[right_copy_index])
        if is_sorted:
            arr[sorted_index] = left_copy[left_copy_index]
            left_copy_index += 1
        else:
            arr[sorted_index] = right_copy[right_copy_index]
            right_copy_index += 1
        
        sorted_index = sorted_index + 1

    # get the remainding elements in the copy lists
    while left_copy_index < len(left_copy):
        arr[sorted_index] = left_copy[left_copy_index]
        left_copy_index = left_copy_index + 1
        sorted_index = sorted_index + 1

    while right_copy_index < len(right_copy):
        arr[sorted_index] = right_copy[right_copy_index]
        right_copy_index = right_copy_index + 1
        sorted_index = sorted_index + 1



def main():
    input = get_input_in_blocks("13", False)

    distress_signal = [[json.loads(packet) for packet in pair.split()]for pair in input ]

    distress_signal_2 = []
    for pair in distress_signal:
        for packet in pair:
            distress_signal_2.append(packet)

    def puzzle_1(distress_signal):

        sorted_pairs = []

        for i,pair in enumerate(distress_signal):
            pair_index = i+1

            is_sorted = compare(pair[0], pair[1])
            if is_sorted:
                sorted_pairs.append(pair_index)

        return(sum(sorted_pairs))

    def puzzle_2(distress_signal):
        
        #add dividers
        distress_signal.append([[2]])
        distress_signal.append([[6]])

        merge_sort(distress_signal, 0, len(distress_signal)-1)

        index_divider_2 = distress_signal.index([[2]])+1
        index_divider_6 = distress_signal.index([[6]])+1
        return(index_divider_2 * index_divider_6)
        
       
    

   
    result_puzzle_1 = puzzle_1(distress_signal)
    result_puzzle_2 = puzzle_2(distress_signal_2)

    
    print(f"Puzzle 1 answer: {result_puzzle_1}")
    print(f"Puzzle 2 answer: {result_puzzle_2}")  
    

if __name__ == "__main__":
    main()