# -*- coding: utf-8 -*-
"""
Created on Tue Jul 29 13:57:59 2025

@author: HP
"""

import math
x1,y1=3.12,2.31
x2,y2=1.23,4.23
x3,y3=12.1,32.21

a = math.sqrt(math.pow(x1 - x2, 2) + math.pow(y1 - y2, 2))
b = math.sqrt(math.pow(x1 - x3, 2) + math.pow(y1 - y3, 2))
c = math.sqrt(math.pow(x2 - x3, 2) + math.pow(y2 - y3, 2))

s=(a+b+c)/2
values=s*(s-a)*(s-b)*(s-c)
area=math.sqrt(values)
print("Area of Circle: ",area)














