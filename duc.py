import mainapp as m

object_list = m.object_list_of_data

list_of_year = []

def list_of_year_building():
    for object in object_list:
        if object.year not in list_of_year:
            list_of_year.append(object.year)
    print(list_of_year)


list_of_year_building()
list_of_year.sort()
print(list_of_year)

def ()