
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

for object in yes:
    count.append(object.crimecount)

for objecct in yes:
    community.append(object.community)

for object in yes:
    population.append(object.residentpop)

for object in yes:
    sector_list.append(object.sector)

# input = input("Input community")
def math():
    print(x)
    global input
    # place = filter(check, x)
    # for input in range(len(x)):
    #     # print("hello")
    #     print(x[])
       

def check(l):
    # if l == input:
    for i in range(len(x)):
        if i == input:
            return True
        else:
            return False

def combine():
    global x
    x = list(zip(community, count, population))

    


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

print(community_list)

list_of_crime_percentage=[]


for z in range (len(community_list)):
    print (community_list[z])
    print (list_of_crime_count[z])
where = str(input("Enter Community Name(all CAPS): "))

def check(where):
    # where = str(input("Enter Community Name(all CAPS): "))
    if where in community_list:
        return True
    else:
        return False

def oneCommunity():
    # where = communityMenu():
    filter_object = filter(check, where)

def communityMenu():
    where = str(input("Enter Community Name(all CAPS): "))



def menu():
    print("Enter Sector of Calgary (1- North, 2-  South, 3- East, 4- West, 5 - all)")
    option = int(input("Enter Option"))
    if option == 1:
        communityMenu()
    if option == 2:
        communityMenu()
    if option == 3:
        communityMenu()
    if option == 4:
        communityMenu()

    
