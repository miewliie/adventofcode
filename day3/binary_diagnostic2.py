binary_list = ['00100', '11110', '10110', '10111', '10101', '01111', '00111', '11100', '10000', '11001', '00010', '01010']


def read_dept_list():
    f = open("puzzle_input.txt", "r")
    input_data = f.readlines()
    return input_data


def calculate_instruction(input_data):
    input_data_least = input_data.copy()

    most_common = calculate_the_most(input_data)
    least_common = calculate_the_least(input_data_least)

    print('final rating', convert_to_binary(most_common) * convert_to_binary(least_common))


def calculate_the_most(input_data):
    digits = []
    i = 0
    while len(input_data) > 1:
        for row_index in input_data:
            digits.append(row_index[i])

        final_score = find_the_score(digits)
        digits.clear()

        most_number = map_the_score(final_score)

        input_data = find_last_result(input_data, most_number, i)
        i += 1
    return input_data[0]


def calculate_the_least(input_data_least):
    digits = []
    i = 0
    while len(input_data_least) > 1:
        for row_index in input_data_least:
            digits.append(row_index[i])

        final_score = find_the_score(digits)
        digits.clear()

        most_number = map_the_score(final_score)

        least_number = '1' if most_number == '0' else '0'

        input_data_least = find_last_result(input_data_least, least_number, i)
        i += 1
    return input_data_least[0]


def map_the_score(final_score):
    if final_score == 0:
        most_number = '1'
    elif final_score > 0:
        most_number = '1'
    else:
        most_number = '0'
    return most_number


def find_last_result(input_data, number, i):
    indexes_to_remove = []

    # scan for elements to be removed
    for index in range(len(input_data)):
        digit = input_data[index]
        if not digit[i] == number:
            indexes_to_remove.insert(0, index)

    # remove elements
    for index in indexes_to_remove:
        del input_data[index]

    return input_data


def find_the_score(rep_of_digit):
    score = 0
    for row_index in rep_of_digit:
        score += -1 if row_index == '0' else 1
    return score


def convert_to_binary(item):
    return int(item, 2)


if __name__ == '__main__':
    data = read_dept_list()
    calculate_instruction(data)
