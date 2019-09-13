#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 16:36:23 2019

@author: lazybear
"""

#user input
total_cost = float(input('total cost'))
portion_saved = float(input('portion saved'))
annual_salary = float(input('Annual Salary'))

#default vars
portion_down_payment = 0.25
r = 0.04
monthly_salary = annual_salary/12
down_payment = portion_down_payment * total_cost

current_saving = 0
month = 0

#control flow
while(current_saving < down_payment):
    month+=1
    current_saving += monthly_salary * portion_saved + current_saving*(r/12)

print('It takes', month, 'months to save up for the down payment')
    
