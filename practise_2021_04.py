from Utils.tools import *

def main():

    data = get_input_in_blocks("202104", True)

    nums, rest = data[0].split(","), data[1:]

    bingo_numbers = clean_list_ints(nums)

    board_data = [r.split("\n") for r in rest]



    def create_boards(board_data):
        list_of_boards = []
        for board in board_data:
            board_string = [b.split() for b in board if b != ""]
            board_int= [list(map(int,t)) for t in board_string]
            list_of_boards.append(board_int)
        return list_of_boards
     
    def mark_number(board, called_number):
        for row in board:
            for index, number in enumerate(row):
                if number == called_number:
                    row[index] = -1
                    return

    def check_row(board):
        for row in board:
            if sum(row)== -5:
                return True
        return False

    def check_col(board):
        for i in range(4):
            col = get_column(board,i)
            if sum(col) == -5:
                return True
        return False
    
    def calculate_score(board, winning_num):
        total = 0
        for row in board:
            total += sum(el for el in row if el > 0)
        score = total * winning_num
        return score


    def play_bingo(board_data: list, numbers: list, first_is_winner: bool):
        boards = create_boards(board_data)
        last_board = len(boards)
        winning_boards = []
        # call number
        for num in numbers:
            # check each board
            for board in boards:
                mark_number(board, num)
            # check for bingo
            for board in boards:
                row_complete = check_row(board)
                if row_complete:
                    winning_boards.append(board)
                    boards.remove(board)
                else:
                    col_complete = check_col(board)
                    if col_complete:
                        winning_boards.append(board)
                        boards.remove(board)


            if first_is_winner == True:
                if len(winning_boards) == 1:
                    # calculate score
                    final_score = calculate_score(winning_boards[0], num)
                    return final_score
            else:
                if len(winning_boards) == last_board:
                    # calculate score
                    final_score = calculate_score(winning_boards[-1], num)
                    return final_score


        


    result1 = play_bingo(board_data, bingo_numbers, True)
    result2 = play_bingo(board_data, bingo_numbers, False)

    print(f"final score of game 1: {result1}")
    print(f"final score of game 2: {result2}")

if __name__ == "__main__":
    main()