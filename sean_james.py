import class_pythunder as c
import mainapp as m


grand_list = m.object_list_of_data

def searchCommunity():
    comm_names = []
    search = input("Enter Community: ")
    j = 0
    for k in grand_list:
        com_sort = c.Community(grand_list[j].DATA1, grand_list[j].DATA3, grand_list[j].DATA4)
        comm_names.append(com_sort)
        j += 1   
        if search == com_sort.community:
            print(com_sort)

def crimeCount():
    pass

def pop():
    pass

# searchCommunity()
