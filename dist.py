my_dist = {
    "name1":"akshay",
    "name2":"aditya",
    "name3":"sangeeta"
}

# print(my_dist)
# print(my_dist.get("name3"))
# print(my_dist["name1"])

# if "name2" in my_dist:
#     print("ok")

# for key,value in my_dist.items():
#     print(key,":", value)

# my_dist["name2"]="gunda"
# print(my_dist) 


for key in my_dist:
    print(key,my_dist[key])

my_dist["name3"] ="ami"
print(my_dist) 

# my_dist.pop("name1")
# print(my_dist)

my_dist.popitem()
print(my_dist)

# my_dist.pop()
# print(my_dist)

del my_dist["name1"]
print(my_dist) 

my_dist["name1"]="akshay"
print(my_dist)

my_print_copy = my_dist.copy()
print(my_print_copy)

my_dist["name4"]="om"
print(my_dist)
print(my_print_copy)


del my_dist["name1"]
print(my_dist)
print(my_dist)
