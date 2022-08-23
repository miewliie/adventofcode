def read_dept_list():
    f = open("puzzle_input.txt", "r")
    input_data = f.readlines()
    return input_data


def calculate_instruction(input_data):
    list_of_lines = prepare_input_data(input_data)

    # verify all 2 points to have similar value to be aligned with
    # drawing the vertical or horizontal line theory
    final_result = filter_range_of_lines(list_of_lines)

    # find the biggest point of (x,y)
    # by scan all the input_data and keep track of the max value
    biggest_tmp = 0
    for line in final_result:
        for item in line:
            biggest_tmp = find_the_biggest(item, biggest_tmp)

    # draw empty canvas with '0'
    diagram = draw_empty_diagram(biggest_tmp)

    # draw input into empty diagram
    for line in final_result:
        draw_diagram_with_input(diagram, line)

    # print to see the diagram (visual)
    # for i in diagram:
    #     print(i)

    # find the point where at least 2 line overlap (>=2)
    total_point = find_area_line_overlap(diagram)
    print('total result', total_point)


def find_area_line_overlap(diagram):
    total_result = 0
    for line in diagram:
        for point in line:
            if point >= 2:
                total_result += 1

    return total_result


def draw_diagram_with_input(diagram, line):
    # find x or y is changed in line
    if is_vertical_line(line):
        draw_vertical_diagram(diagram, line)
    else:
        draw_horizontal_diagram(diagram, line)
    # once you know x or y changed then you know if u will draw vertical or horizontal line to diagram
    # eg x changed, find the min and max of x values from the line
    # draw until arrive at max(x)


def draw_horizontal_diagram(diagram, line):
    # find min and max of y from line
    tmp_axis = []
    x_axis = 0
    for point in line:
        axis = point.split(',')
        x_axis = int(axis[0])
        y_axis = int(axis[1])
        tmp_axis.append(y_axis)

    point_a = tmp_axis[0]
    point_b = tmp_axis[1]
    if point_a < point_b:
        while point_a <= point_b:
            diagram[point_a][x_axis] += 1
            point_a += 1
    elif point_b < point_a:
        while point_b <= point_a:
            diagram[point_b][x_axis] += 1
            point_b += 1
    else:
        diagram[point_a][x_axis] += 1


def draw_vertical_diagram(diagram, line):
    # find min and max of x from line
    tmp_axis = []
    y_axis = 0
    for point in line:
        axis = point.split(',')
        y_axis = int(axis[1])
        x_axis = int(axis[0])
        tmp_axis.append(x_axis)

    point_a = tmp_axis[0]
    point_b = tmp_axis[1]
    if point_a < point_b:
        while point_a <= point_b:
            diagram[y_axis][point_a] += 1
            point_a += 1
    elif point_b < point_a:
        while point_b <= point_a:
            diagram[y_axis][point_b] += 1
            point_b += 1
    else:
        diagram[y_axis][point_b] += 1


def is_vertical_line(line):
    tmp_point = []
    for point in line:
        axis = point.split(',')
        x = axis[0]
        y = axis[1]
        if not tmp_point == []:
            if not int(tmp_point[0]) == int(x) and int(tmp_point[1]) == int(y):
                return True
            else:
                return False
        else:
            tmp_point = axis


def draw_empty_diagram(max_number):
    max_number += 1
    empty_list = [[0 for col in range(max_number)] for row in range(max_number)]
    return empty_list


def filter_range_of_lines(list_of_lines):
    position_to_remove = []
    for index in range(len(list_of_lines)):
        # list out position of not similar input
        if is_dissimilar(list_of_lines[index]):
            position_to_remove.insert(0, index)

    # send list to remove
    for item in position_to_remove:
        del list_of_lines[item]

    return list_of_lines


def is_dissimilar(line):
    tmp_axis = []
    for point in line:
        axis = point.split(',')
        x = axis[0]
        y = axis[1]
        if not tmp_axis == []:
            if not int(tmp_axis[0]) == int(x) and not int(tmp_axis[1]) == int(y):
                return True
        else:
            tmp_axis = axis
    return False


def find_the_biggest(point, big_tmp):
    biggest_number = big_tmp
    axis = point.split(',')
    for i in axis:
        biggest_number = max(biggest_number, int(i))
    return biggest_number


def prepare_input_data(input_data):
    lines = []
    for row in input_data:
        lines.append(row.split(' -> '))
    return lines


if __name__ == '__main__':
    data = read_dept_list()
    calculate_instruction(data)
