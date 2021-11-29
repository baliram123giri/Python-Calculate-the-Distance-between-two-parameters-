#class defination
import math
from types import MethodDescriptorType
class Distance():
    #1. Property

    #2. Constructor

    #3. Method
    def calculateDistance(self,x1,x2,y1,y2):
        x = x1 - x2
        x = x*x
        y = y1 - y2
        y = y*y
        return math.sqrt(x+y)

    pass
#2. Lets create a class object
myObject = Distance()

#3.now call the claculateDistance MethodDescriptorType
result = myObject.calculateDistance(3,7,2,8)
print(f"the distance between is : {result}")