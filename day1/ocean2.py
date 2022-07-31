import csv
# dept_list = [199,200,208,210,200,207,240,269,260,263]


def read_dept_list():
    f = open("input.txt", "r")
    data = f.readlines()
    return data


def convert_to_int(data):
    temp = int(data)
    return temp


def compare_dept(data):
    i = 1
    increase_dept_count = 0
    while i < len(data):
        if data[i-1] < data[i]:
            increase_dept_count += 1
        i += 1
    print(increase_dept_count)


def sum_each_three(dept_list):
    i = 0
    list_of_sum = []
    while i < (len(dept_list)-2):
        total_sum = convert_to_int(dept_list[i]) + convert_to_int(dept_list[i+1]) + convert_to_int(dept_list[i+2])
        list_of_sum.append(total_sum)
        i += 1
    return list_of_sum


if __name__ == '__main__':
    data = read_dept_list()
    results = sum_each_three(data)
    compare_dept(results)