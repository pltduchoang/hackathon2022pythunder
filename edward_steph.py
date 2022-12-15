
import class_of_anything as c
# import os
import cool_class as p
import mainapp as m

object_list = []
community_list = []
community = []
count = []
population = []
sector_list = []
x=[]
yes=m.object_list_of_data

for object in yes:
    if object.community not in community_list:
        community_list.append(object.community)
        if object.residentpop == '' or object.residentpop =="0" or object.residentpop==0:
            population.append(0)
        elif object.residentpop == 0:
            population.append(0)
        population.append(object.residentpop)


for object in yes:
    count.append(object.crimecount)


# for object in yes:
#     if object.sector not in sector_list:
#         sector_list.append(object.sector)
# del(sector_list[-1])


list_of_crime_count = []
for item in community_list:
    crime_count = 0
    for object in yes:
        if object.community == item:
            crime_count += int(object.crimecount)
    list_of_crime_count.append(crime_count)

list_of_crime_percentage=[]
percentage = 0


print("{:>40}{:>20}".format("Community Name", "Percentage"))
for z in range (len(community_list)):
    if population[z] == 0 or population[z] == '' or population[z] == "0":
            percentage = 0
            print("{:>40}{:>20}{}".format(community_list[z],percentage,"%"))
    else:
        percentage = (int(list_of_crime_count[z]) / int(float(population[z]))) * 100
        rounded = round(percentage, 2)
        print("{:>40}{:>20}{}".format(community_list[z],rounded,"%"))




