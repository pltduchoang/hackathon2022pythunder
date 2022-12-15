import class_pythunder as c
import mainapp as m


grand_list = m.object_list_of_data

# def searchCommunity():
#     comm_names = []
#     search = input("Enter Community: ")
#     j = 0
#     for k in grand_list:
#         com_sort = c.Community(grand_list[j].DATA1, grand_list[j].DATA3, grand_list[j].DATA4)
#         comm_names.append(com_sort)
#         j += 1   
#         if search == com_sort.community:
#             print(com_sort)

list_of_sector = []
for object in grand_list:
    if object.sector not in list_of_sector:
        list_of_sector.append(object.sector)
del(list_of_sector[-1])

def menu():
    for i in range(len(list_of_sector)):
        print(f'{i+1}  -  {list_of_sector[i]}') 
    print('Enter 0 to back to main menu')
    user_choice=input('Enter sector')
    viewBySector(list_of_sector[int(user_choice)-1])

def viewBySector(x):
    list_of_community = []
    for object in grand_list:
        if object.sector == x and object.community not in list_of_community:
            list_of_community.append(object.community)
    list_of_crime_count = []
    
    
    for community in list_of_community:
        crime_counter = 0

        for object in grand_list:
            if object.community == community:
                crime_counter += int(object.crimecount)
                
        list_of_crime_count.append(crime_counter)

    
    
    
    percentage = 0    
    for z in range(len(list_of_community)):
        
        # percentage = int(list_of_crime_count[z])/int(population_list[z]) 
        print(f'{"Name of community":<25}{"Crime from 2017":<15}')
        print(f'{list_of_community[z]:<25} {list_of_crime_count[z]:<15}')

    
    while True:
        user_find = input("Enter specific community name: ").upper()
        if user_find != 0:
            x=0
            while x in range (len(list_of_community)+1):
                if x < len(list_of_community) and list_of_community[x] == user_find:
                    print(f'{"Name of community: ":<25}{"Crime from 2017":<15}')
                    print(f'{list_of_community[x]:<25} {list_of_crime_count[x]:<15}')
                    break
                if x == len(list_of_community):
                    print('Communnity Name not found!')
                else:
                    x += 1
                
        if user_find == 0:

            break
    menu()        
    
# searchCommunity(
print(list_of_sector)
menu()
