import class_of_anything as c
import os

object_list = []

here = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(here, "DATA_FILE_NAME_HERE")
file_data = open(filename, "r")
for line in file_data:
    line_data = line.lstrip().rstrip().split('REPLACE_BY_ANY_THING')
    object_list.append(c.pythunder(line_data[0],line_data[1],line_data[2],line_data[3],line_data[4],line_data[5],line_data[6],line_data[8]))


def print_object():
    for object in object_list:
        print(object)

def function_name_1():
    pass

def function_name_1():
    pass

def function_name_1():
    pass

def function_name_1():
    pass

def function_name_1():
    pass

