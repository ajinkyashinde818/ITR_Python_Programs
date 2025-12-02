x1,y1=[int(p)for p in input("Enter the Co-ordinates of First point \n").split(",")]
x2,y2=[int(p)for p in input("Enter the Co-ordinates of Second point \n").split(",")]
import math
if(y1==y2):
    value1=math.pow((x1-x2),2)
   
    distance=math.sqrt(value1)
    print("Point are paraller to X-Axis")
    print("Distance = ",distance)
    
else:
    print("Point are not paraller to X-Axis")