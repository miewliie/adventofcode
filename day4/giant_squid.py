def read_dept_list():
    f = open("puzzle_input.txt", "r")
    input_data = f.readlines()
    return input_data


def calculate_instruction(input_data):
    board_data = input_data.copy()

    # find the list of bingo number
    bingo_numbers = prepare_bingo_numbers(input_data)

    # prepare board in rows and columns
    boards = prepare_boards(board_data)

    # win bingo either row or column
    bingo_result = []
    for bingo_number in bingo_numbers:
        bingo_result = play_bingo(bingo_number, boards)
        if len(bingo_result) > 0:
            break
    # finding the sum of all unmarked numbers on that board
    # multiply that sum by the number that was just called when the board won
    final_score_of_won_board(bingo_result, bingo_number)


def final_score_of_won_board(bingo_result_board, bingo_number):
    print(bingo_result_board, bingo_number)
    bingo_number = int(bingo_number)
    sum_num = 0
    for row in bingo_result_board:
        for item in row:
            if not item == '*':
                sum_num += int(item)
    print('final result = ', sum_num * bingo_number)


def is_bingo(marked_board):
    # check for bingo on rows
    for row in marked_board:
        if row.count('*') == len(row):
            return True

    # check for bingo on columns
    for c in range(5):
        count = 0
        for r in range(5):
            if marked_board[r][c] == '*':
                count += 1
        if count == 5:
            return True

    return False


def play_bingo_single_board(bingo_number, board):
    for row in board:
        for item in range(len(row)):
            if row[item] == bingo_number:
                row[item] = row[item].replace(row[item], '*')


def play_bingo(bingo_number, boards):
    for board in boards:
        play_bingo_single_board(bingo_number, board)
        if is_bingo(board):
            return board
    return []


def prepare_boards(board_data):
    del board_data[0]

    boards = []
    board = []
    for row in board_data:
        if row == '\n':
            if len(board) > 0:
                boards.append(board)
                board = []
        else:
            board.append(row.split())
    boards.append(board)
    return boards


def prepare_bingo_numbers(input_data):
    bingo_input = input_data[0]
    bingo_input = bingo_input.split(',')
    bingo_numbers = []
    for number in bingo_input:
        bingo_numbers.append(number)
    return bingo_numbers


if __name__ == '__main__':
    data = read_dept_list()
    calculate_instruction(data)
