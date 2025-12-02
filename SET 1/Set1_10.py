# -*- coding: utf-8 -*-
"""
Created on Fri Jul 11 12:30:31 2025

@author: HP
"""

sec=int(input("Enter a Second :"))

hours = sec // 3600
rem = sec % 3600
minutes = rem // 60
seconds = rem % 60

print("hours is",hours)
print("Minutes is",minutes)
print("Second is",sec)