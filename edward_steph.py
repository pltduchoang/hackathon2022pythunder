
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

# for objecct in yes:
#     community.append(object.community)
# o = 0.00001
# for object in yes:
#     o += 0.000000001
#     if object.residentpop not in population:
#         if object.residentpop == 0:
#             o=0.00001
#         population.append(object.residentpop)

for object in yes:
    if object.sector not in sector_list:
        sector_list.append(object.sector)
del(sector_list[-1])
# input = input("Input community")
# def math():
#     print(x)
#     global input
#     # place = filter(check, x)
#     # for input in range(len(x)):
#     #     # print("hello")
#     #     print(x[])
       

# def check(l):
#     # if l == input:
#     for i in range(len(x)):
#         if i == input:
#             return True
#         else:
#             return False

# def combine():
#     global x
#     x = list(zip(community, count, population))

    


        # print(community)


# def readFile():
#     with open("data.csv", "r") as file:
#         l = 1
#         for line in file:
#             if l == 1:
#                 l += 1
#                 continue
#             items = line.rstrip().split(",")
#             # print(items)
#             object = (p.percent(items[1],items[3],items[4]))
#             print(object)
#             object_list.append(str(object))
#             # print(object_list)
#             # print(items[1])
#             # print(items[3])
#             community.append(items[1])
#             count.append(items[3])
#         comm = list(dict.fromkeys(community))
#         print(comm)
#         file.close()
#         return comm
# def math():

    # asd


# if __name__ == "__main__":
#     # readFile()
#     combine()
#     math()


list_of_crime_count = []
for item in community_list:
    crime_count = 0
    for object in yes:
        if object.community == item:
            crime_count += int(object.crimecount)
    list_of_crime_count.append(crime_count)
    # print(crime_count)
    # print(list_of_crime_count)

# print(community_list)

list_of_crime_percentage=[]
percentage = 0


print("Community Name        Percentage")
for z in range (len(community_list)):
    # if float(population[z]) != 0:
        # if percentage == (int(list_of_crime_count[z]) / 0) * 100:
        #     twat = 0
        #     print("Community Name        Percentage")
        #     print(community_list[z], twat)
        # else:
        # try:
    if population[z] == 0 or population[z] == '' or population[z] == "0":
            percentage = 0
            print(community_list[z],":       ",percentage,"%")
    else:

        percentage = (int(list_of_crime_count[z]) / int(float(population[z]))) * 100

    # except ZeroDivisionError:

        print(community_list[z],":       ",percentage,"%")
    # elif str(float(population[z])) == 0:
    #     percentage = 0
    #     print("Community Name        Percentage")
    #     print(community_list[z],"    ",percentage)
    # if float(population[z]) == ' ':
    #     continue

    # print (community_list[z])
    # print (list_of_crime_count[z])
    # print (population[z])



where = str(input("Enter Community Name(all CAPS): "))

# sector1 = []
# sector2 = []
# sector3 = []
# sector4 = []
# sector5 = []
# sector6 = []
# sector7 = []
# sector8 = []

# list5 = [[], [], [], [], [], [], [], []]

# list_of_comm_in_sector = []

# index1 = -1
# for i in sector_list:
#     index1 += 1
#     for obj in yes:
#         if str(obj.sector) == i:
#             for com in community_list:
#                 if com == obj.community:
#                     if obj.community == obj.sector == True:
#                         list5[index1].append(com)
# for j in list5:
#     print(j)

#             for thing in community:
#                 if object.community == thing:

#             list_of_comm_in_sector.append()
#             print(list_of_comm_in_sector)

# for z in range(len(sector_list)):
#     print(sector_list[z])
#     # print()


def check(where):
    # where = str(input("Enter Community Name(all CAPS): "))
    if where in community_list:
        return True
    else:
        return False

def oneCommunity():
    # where = communityMenu():
    filter_object = filter(check, where)
    filered = list(filter_object)
    print(filered)

def communityMenu():
    where = str(input("Enter Community Name(all CAPS): "))



def menu():
    print("Enter Sector of Calgary (1- North, 2-  South, 3- East, 4- West, 5 - all)")
    option = int(input("Enter Option"))
    if option == 1:
        oneCommunity()
    if option == 2:
        communityMenu()
    if option == 3:
        communityMenu()
    if option == 4:
        communityMenu()

# menu()
