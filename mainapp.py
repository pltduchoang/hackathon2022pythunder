import class_pythunder as c
import os

object_list_of_data = []
list_of_function_label = ['Exit','View stat by commnutiy','View stat by year','View stat by percentate over population','View stat by crime category']

here = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(here, "data.csv")
file_data = open(filename, "r")
file_data.readline()
for line in file_data:
    line_data = line.lstrip().rstrip().split(',')
    object_list_of_data.append(c.pythunder(line_data[0],line_data[1],line_data[2],line_data[3],line_data[4],line_data[5],line_data[6]))
    



def print_object():
    for object in object_list_of_data:
        print(object)

def main_menu():
    list_of_function = [0,communitiy_data_by_year]
    while True:
        print(f'Welcome to City of Calgary crime stat program')
        for i in range(len(list_of_function)):
            print(f'{i}  -   {list_of_function_label[i]}')
        user_choice = inputRangeCheck(input('Enter your option'))
        if user_choice == 0:
            break
        else:
            list_of_function[i]()
    
    
def inputRangeCheck(x):
    range_check = False
    while not range_check:
        if x.isdigit():
            if not int(x) in range (0,len()):
                x = input('Invalid, input not in range, try again: ')
            else:
                range_check = True
        else: 
            x = input('Invalid input, please enter number only again: ')
    return x




def communitiy_data_by_year():
    pass

def function_name_3():
    pass

def function_name_4():
    pass

def function_name_5():
    pass


# main_menu()

