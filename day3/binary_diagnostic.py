binary_list = ['00100', '11110', '10110', '10111', '10101', '01111', '00111', '11100', '10000', '11001', '00010', '01010']


def read_dept_list():
    f = open("puzzle_input.txt", "r")
    input_data = f.readlines()
    return input_data


def calculate_instruction(input_data):
    i = 0
    digit_one = []
    digit_two = []
    digit_three = []
    digit_four = []
    digit_five = []
    digit_six = []
    digit_seven = []
    digit_eight = []
    digit_nine = []
    digit_ten = []
    digit_eleven = []
    digit_twelve = []
    results = []
    while i < len(input_data):
        x = 1
        while x <= len(input_data[i]):
            all_char = input_data[i]
            if x == 1:
                result1 = all_char[0]
                digit_one.append(result1)
            elif x == 2:
                result2 = all_char[1]
                digit_two.append(result2)
            elif x == 3:
                result3 = all_char[2]
                digit_three.append(result3)
            elif x == 4:
                result4 = all_char[3]
                digit_four.append(result4)
            elif x == 5:
                result5 = all_char[4]
                digit_five.append(result5)
            elif x == 6:
                result6 = all_char[5]
                digit_six.append(result6)
            elif x == 7:
                result7 = all_char[6]
                digit_seven.append(result7)
            elif x == 8:
                result8 = all_char[7]
                digit_eight.append(result8)
            elif x == 9:
                result9 = all_char[8]
                digit_nine.append(result9)
            elif x == 10:
                result10 = all_char[9]
                digit_ten.append(result10)
            elif x == 11:
                result11 = all_char[10]
                digit_eleven.append(result11)
            else:
                result12 = all_char[11]
                digit_twelve.append(result12)
            x += 1
        i += 1

    results.append(count_value(digit_one))
    results.append(count_value(digit_two))
    results.append(count_value(digit_three))
    results.append(count_value(digit_four))
    results.append(count_value(digit_five))
    results.append(count_value(digit_six))
    results.append(count_value(digit_seven))
    results.append(count_value(digit_eight))
    results.append(count_value(digit_nine))
    results.append(count_value(digit_ten))
    results.append(count_value(digit_eleven))
    results.append(count_value(digit_twelve))
    print('x ', results)
    final_result = convert_to_binary(results)
    print(final_result)


def count_value(rep_of_digit):
    zero = 0
    one = 0
    i = 0
    while i < len(rep_of_digit):
        if rep_of_digit[i] == '0':
            zero += 1
        else:
            one += 1
        i += 1
    the_most = find_the_most(zero, one)
    the_least = find_the_least(zero, one)
    return the_most, the_least


def convert_to_binary(results_most_least):
    i = 0
    most_list = []
    least_list = []
    while i < len(results_most_least):
        position = results_most_least[i]
        most_list.append(position[0])
        least_list.append(position[1])
        i += 1
    my_most = ''.join(map(str, most_list))
    my_least = ''.join(map(str, least_list))
    return int(my_most, 2) * int(my_least, 2)


def find_the_most(zero, one):
    if zero > one:
        return 0
    else:
        return 1


def find_the_least(zero, one):
    if zero < one:
        return 0
    else:
        return 1


if __name__ == '__main__':
    data = read_dept_list()
    calculate_instruction(data)
