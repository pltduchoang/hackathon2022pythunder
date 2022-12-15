
#break & enter
#assult theft from vehicle 
#theft of vehicle
#assult
#street robbery
#violence other
#


#Population

import mainapp as m
import class_pythunder as c
import os

object_list = m.object_list_of_data

# here = os.path.dirname(os.path.abspath(__file__))
# filename = os.path.join(here, "DATA_FILE_NAME_HERE")
# file_data = open(filename, "r")
# for line in file_data:
#     line_data = line.lstrip().rstrip().split('REPLACE_BY_ANY_THING')
#     object_list.append(c.pythunder(line_data[0],line_data[1],line_data[2],line_data[3],line_data[4],line_data[5],line_data[6],line_data[8]))



list_of_years = []

#count number of years
def function_name_1():
    for object in object_list:
            # var1 = 0

                
            # if str(f'{object.year}').isdigit() == True:
            #     var1 += 
        if str(object.year) not in list_of_years:
            list_of_years.append(object.year)



function_name_1()
print(list_of_years)