from line import Line
from point import Point


def read_dept_list():
    f = open("puzzle_input.txt", "r")
    input_data = f.readlines()
    return parse_input(input_data)


def parse_input(input_data):
    # turn each row (which is a string)
    # into a Line(..,..) object
    # and return
    lines = []
    for row in input_data:
        # '4,5 -> 3,2'
        points_array = row.split(' -> ') #['4,5', '3,2']
        point_a_array = points_array[0].split(',') #['4', '5']
        point_b_array = points_array[1].split(',') #['3', '2']
        point_a = Point(int(point_a_array[0]), int(point_a_array[1])) # Point { x = 4, y = 5 }
        point_b = Point(int(point_b_array[0]), int(point_b_array[1])) # Point { x = 3, y = 2 }
        lines.append(Line(point_a, point_b)) # Line { point_a, point_b }
    return lines # [Line { .. }, Line { .. }, Line { .. }, ... ]


def calculate_instruction(list_of_lines):
    # find the biggest point of (x,y)
    # by scan all the input_data and keep track of the max value
    biggest_tmp = 0
    for line in list_of_lines:
        biggest_tmp = max(biggest_tmp, line.point_a.x, line.point_a.y, line.point_b.x, line.point_b.y)

    # draw empty canvas with '0'
    diagram = draw_empty_diagram(biggest_tmp)

    # draw input into empty diagram
    for line in list_of_lines:
        draw_diagram_with_input(diagram, line)

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
    current_point = line.point_a
    target_point = line.point_b
    diagram[current_point.y][current_point.x] += 1

    direction_x = 0 if current_point.x == target_point.x else (1 if current_point.x < target_point.x else -1)
    direction_y = 0 if current_point.y == target_point.y else (1 if current_point.y < target_point.y else -1)

    while not current_point == target_point:
        current_point.x += direction_x
        current_point.y += direction_y
        diagram[current_point.y][current_point.x] += 1


def draw_empty_diagram(max_number):
    max_number += 1
    empty_list = [[0 for col in range(max_number)] for row in range(max_number)]
    return empty_list


if __name__ == '__main__':
    data = read_dept_list()
    calculate_instruction(data)
