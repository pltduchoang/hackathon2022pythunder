# import class_of_anything as c
# import os

# object_list = []

# here = os.path.dirname(os.path.abspath(__file__))
# filename = os.path.join(here, "DATA_FILE_NAME_HERE")
# file_data = open(filename, "r")
# for line in file_data:
#     line_data = line.lstrip().rstrip().split('REPLACE_BY_ANY_THING')
#     object_list.append(c.pythunder(line_data[0],line_data[1],line_data[2],line_data[3],line_data[4],line_data[5],line_data[6],line_data[8]))


# def print_object():
#     for object in object_list:
#         print(object)

# def function_name_1():
#     pass

# def function_name_1():
#     pass

# def function_name_1():
#     pass

# def function_name_1():
#     pass

# def function_name_1():
#     pass


import class_of_anything as c
import os

object_list_of_cases = []

here = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(here, "practice.csv")
file_data = open(filename, "r")
file_data.readline()
for line in file_data:
    line_data = line.lstrip().rstrip().split(',')
    object_list_of_cases.append(c.pythunder(line_data[1],line_data[2],line_data[3],line_data[4]))

category_list = []

for object in object_list_of_cases:
    if object.cat not in category_list:
        category_list.append(object.cat)

print (category_list)


community_list = []

for object in object_list_of_cases:
    if object.community not in community_list:
        community_list.append(object.community)

crime_count_list = []

for ech_community in community_list:
    crime_count = 0
    for object in object_list_of_cases:
        if object.community == ech_community:
            crime_count += int(object.count)
    crime_count_list.append(crime_count)

print(community_list)

print(crime_count_list)

for x in range (len(community_list)):
    print (community_list[x])
    print (crime_count_list[x])

crime_count_list.sort()
print(crime_count_list[-1])