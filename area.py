import math
def circle_stat(radius):
    area = math.pi *radius*2
    circumference = 2*math.pi*radius
    return area,circumference
a,c = circle_stat(5)
# print("area : " ,a,"circum :",c)

cube = lambda x: x**3
anothercube  = cube
print(anothercube(10))
