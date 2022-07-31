import csv
# dept_list = [199,200,208,210,200,207,240,269,260,263]


def read_dept_list():
    f = open("dept_list.csv", "r")
    data = list(csv.reader(f, delimiter='\t'))
    return data


def convert_to_int(data):
    temp = int(data[0])
    return temp


def compare_dept(data):
    i = 1
    increase_dept_count = 0
    while i < len(data):
        if convert_to_int(data[i-1]) < convert_to_int(data[i]):
            increase_dept_count += 1
        i += 1
    print(increase_dept_count)


if __name__ == '__main__':
    data = read_dept_list()
    compare_dept(data)