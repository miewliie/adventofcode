# inst_list = ["forward 5", "down 5", "forward 8", "up 3", "down 8", "forward 2"]


def read_dept_list():
    f = open("input.txt", "r")
    data = f.readlines()
    return data


def split_str_num(instruction):
    return instruction.split(" ", 1)


def calculate_instruction(inst_list):
    horizontal_position = 0
    depth_position = 0
    aim = 0
    i = 0
    while i < len(inst_list):
        result = split_str_num(inst_list[i])
        if result[0] == "forward":
            horizontal_position = horizontal_position + int(result[1])
            depth_position = depth_position + (aim * int(result[1]))
        elif result[0] == "down":
            aim = aim + int(result[1])
        else:
            aim = aim - int(result[1])
        i += 1
    print('horizontal * depth = ', horizontal_position * depth_position)


if __name__ == '__main__':
    data = read_dept_list()
    calculate_instruction(data)
