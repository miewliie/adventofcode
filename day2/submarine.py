# inst_list = ["forward 5", "down 5", "forward 8", "up 3", "down 8", "forward 2"]


def read_dept_list():
    f = open("input.txt", "r")
    data = f.readlines()
    # print(type(data[0]))
    return data


def split_str_num(instruction):
    return instruction.split(" ", 1)


def calculate_instruction(inst_list):
    horizontal_position = 0
    dept_position = 0
    i = 0
    while i < len(inst_list):
        result = split_str_num(inst_list[i])
        if result[0] == "forward":
            horizontal_position = horizontal_position + int(result[1])
        elif result[0] == "down":
            dept_position = dept_position + int(result[1])
        else:
            dept_position = dept_position - int(result[1])
        i += 1
    print('(hori: ', horizontal_position, ' * dept: ', dept_position, ') total = ', (horizontal_position * dept_position))


if __name__ == '__main__':
    data = read_dept_list()
    calculate_instruction(data)
