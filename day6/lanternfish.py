def read_dept_list():
    f = open("test_input.txt", "r")
    input_data = f.readlines()
    return input_data


def calculate_instruction(fish_timer_data):
    print(fish_timer_data)
    for i in fish_timer_data:
        fish_timer_data = i.split(',')

    timer_reset = '6'
    new_fish_timer = '8'
    for i in range(80):
        print('day: ', i)
        for index in range(len(fish_timer_data)):
            fish_timer = int(fish_timer_data[index])
            if not fish_timer == 0:
                fish_timer -= 1
                fish_timer_data[index] = fish_timer
            elif fish_timer == 0:
                fish_timer_data[index] = timer_reset
                fish_timer_data.append(new_fish_timer)

    # print('fish', fish_timer_data)
    print('total fish', len(fish_timer_data))


if __name__ == '__main__':
    data = read_dept_list()
    calculate_instruction(data)