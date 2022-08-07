binary_list = ['00100', '11110', '10110', '10111', '10101', '01111', '00111', '11100', '10000', '11001', '00010', '01010']


def read_dept_list():
    f = open("puzzle_input.txt", "r")
    input_data = f.readlines()
    return input_data


def calculate_instruction(input_data):
    digits = []
    for row_index in range(len(input_data)):
        row = input_data[row_index]
        for char_index in range(len(row) -1):
            if len(digits) <= char_index:
                digits.append([])
            digits[char_index].append(row[char_index])

    results = []
    for row_index in digits:
        results.append(find_the_most(row_index))
    final_answer = compute_result(results)
    print(final_answer)


def find_the_most(rep_of_digit):
    score = 0
    for row_index in rep_of_digit:
        score += -1 if row_index == '0' else 1
    the_most = 1 if score >= 0 else 0
    return the_most


def compute_result(results_most_least):
    most_list = results_most_least
    least_list = []

    for element in most_list:
        least_list.append(1 if element == 0 else 0)

    my_most = convert_to_binary(''.join(map(str, most_list)))
    my_least = convert_to_binary(''.join(map(str, least_list)))

    return my_most * my_least


def convert_to_binary(array):
    return int(array, 2)


if __name__ == '__main__':
    data = read_dept_list()
    calculate_instruction(data)
