# -*- coding: utf-8 -*-
"""
Created on Fri Jul 11 12:39:06 2025

@author: HP
"""

days=int(input("Enter the Days:"))

years=days//365
rdays=years%365

month=rdays//30
rdays=rdays%30


weeks = rdays // 7
rdays %= 7


print("Years is",years)
print("Month is",month)
print("Weeks:", weeks)
print("Days:", rdays)



