def read_dept_list():
    f = open("puzzle_input.txt", "r")
    input_data = f.readlines()
    return input_data


def calculate_instruction(fish_timer_data):
    for i in fish_timer_data:
        fish_timer_data = i.split(',')

    print(fish_timer_data)

    state = [0 for x in range(9)]

    for string_element in fish_timer_data:
        state[int(string_element)] += 1

    print(state)
    timer_reset_int = 6
    for i in range(256):
        new_fish = state.pop(0)
        state.append(new_fish)
        state[timer_reset_int] += new_fish

    print('total fish', sum(state))


if __name__ == '__main__':
    data = read_dept_list()
    calculate_instruction(data)