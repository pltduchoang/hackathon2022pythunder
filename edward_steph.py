
import class_of_anything as c
# import os
import cool_class as p
import mainapp as m

object_list = []
community_list = []
community = []
count = []
population = []
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

input = input("Input community")
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
        if input == item.community:
            crime_count += item.crimecount
    list_of_crime_count.append(crime_count)

list_of_crime_percentage=[]

for z in range (len(community_list)):
    print (community_list[x])
    print (crime_count[x])
    
