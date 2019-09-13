#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 17:08:10 2019

@author: lazybear
"""

semi_annual_raise = .07
r = 0.04
portion_down_payment = .25
total_cost = 1000000.0

#user-provided var
annual_salary = float(input('annual salary'))

#derived vars

down_payment = portion_down_payment * total_cost

#program starts
step = 0
month = 36
current_saving = 0

low = 0
high = 10000



while abs(current_saving-down_payment)>100:
    current_saving = 0
    monthly_salary = annual_salary/12
    portion_saved = int(round((low+high)/2))
    step +=1
    
    print('Step:', step)
    print('current guess:', portion_saved/100, 'percent' )
    
#calculate savings based on the guessed portion_saved rate
    for i in range(1,month+1):
        current_saving += monthly_salary*portion_saved/10000 + current_saving*(r/12)
        if i % 6 == 0:
            monthly_salary *= (1+semi_annual_raise)
            
    print('Current saving amount', current_saving)
#    implement bisection search
    if current_saving > down_payment:
        high = portion_saved
        
    else:
        low = portion_saved
    
    if abs(portion_saved-10000)<=1:
        print('does not stand')
        break
#    if step >=30:
#        break


if abs(portion_saved-10000)>1:
    print('step taken', step)
    print('best saving rate', portion_saved/100, 'percent')
    
    
    
        
        
   
    
    