
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


#append years to list



list_of_years = []
def list_years():
    for object in object_list:
        if str(object.year) not in list_of_years:
            list_of_years.append(object.year)
            list_of_years.sort()



list_of_communities = []
def list_community():
    for obj in object_list:
        if str(obj.community) not in list_of_communities:
            list_of_communities.append(obj.community)



list_of_sectors = []
def list_sector():
    for obj in object_list:
        if str(obj.sector) not in list_of_sectors:
            list_of_sectors.append(obj.sector)

list_sector()
print(list_of_sectors)


# def community_data_by_year(year):


#     object.year
#     object



#     # for obj in








def year_menu():
    list_years()
    print(list_of_years[1], list_of_years[2], list_of_years[3], list_of_years[4], list_of_years[5], list_of_years[0], )
    
    menu_year = ''  
    while menu_year !=0:
        #input option
        menu_year = int(input("\nYear Menu\n0 - Return to Main Menu\n1 - 2017\n2 - 2018\n3 - 2019\n4 - 2020\n5 - 2021\n6 - 2022\nEnter option: "))

        if menu_year == 0:
            pass

        elif menu_year == 1:
            community_data_by_year(2017)

            which_year = 2017
        
        elif menu_year == 2:

            which_year = 2018

        elif menu_year == 3:

            which_year = 2019

        elif menu_year == 4:

            which_year = 2020

        elif menu_year == 5:

            which_year = 2021

        elif menu_year == 6:

            which_year = 2022

        else: print("\nInvalid input. Please try again.")
    return which_year
year_menu()



    
