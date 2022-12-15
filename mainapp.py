import class_pythunder as c
import os

object_list_of_data = []

here = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(here, "data.csv")
file_data = open(filename, "r")
for line in file_data:
    line_data = line.lstrip().rstrip().split(',')
    object_list_of_data.append(c.pythunder(line_data[0],line_data[1],line_data[2],line_data[3],line_data[4],line_data[5],line_data[6]))


def print_object():
    for object in object_list_of_data:
        print(object)

def function_name_1():
    pass

def function_name_2():
    pass

def function_name_3():
    pass

def function_name_4():
    pass

def function_name_5():
    pass

print_object()
