import math
#1. Function Defintaion
def distance (x1,x2,y1,y2):
    x = x1-x2 
    x = x*x
    y = y1-y2
    y = y*y
    return math.sqrt(x+y) # fruitful Functions
   
 #2. Function calling
result = distance(3,7,2,8)
print("the distance between two point is : {}".format(result))
             