x,y=[int(a)for a in input("Enter co-ordinates of a point \n").split(",")]
position=None

if x>0 and y>0:
    position="First Quadrant"
elif x<0 and y>0:
    position="Second Quadrant"
    
elif x<0 and y<0:
    position="Thrid Quadrant"
    
elif x>0 and y<0:
    position="Fourth Quadrant"
    
elif x>0 and y==0:
    position="Positive X-Axis"
    
elif x<0 and y==0:
    position="Negative X-Axis"
    
elif x==0 and y>0:
    position="Positive Y-Axis"
    
elif x==0 and y<0:
    position="Negative X-Axis"
    
else:
    position="Origin"
    
print("Point with Co-ordinatos ",x," , " ,y, " lise on ",position)