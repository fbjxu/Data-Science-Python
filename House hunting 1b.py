#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 16:56:51 2019

@author: lazybear
"""

#user input
total_cost = float(input('total cost'))
portion_saved = float(input('portion saved'))
annual_salary = float(input('Annual Salary'))
semi_annual_raise = float(input('Semi-annual raise'))

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
    if month%6 == 0:
        monthly_salary *= (1+semi_annual_raise)

print('It takes', month, 'months to save up for the down payment')
    