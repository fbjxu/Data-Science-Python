#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 08:45:08 2019

@author: lazybear
"""

#dealing with exceprions
#use exception when asking user for input and user provides invalid input

try:
    a = int(input("please provide an int: "))
    b = int(input("provide another int: "))
    print(a/b)
except:
    print("bug in user input")
    

#handeling specific error
try:
    a = int(input("please provide an int: "))
    b = int(input("provide another int that is not 0: "))
    print("a/b = ", a/b)
    print("a+b = ", a+b)

except ValueError:
    print("can't convert input to numbers")

except ZeroDivisionError:
    print("can't divide by zero")

except:
    print("Something went very wrong")
    
#other exceptions: else and finally
    
try:
    a = int(input("please enter an int"))
    b = int(input("Please enter another int"))
    print(a/b)
except:
    print("something went wrong")
else:
    print("the try block has been complete")
finally:
    print("this is normally used for clean-up code that should be run no matter what")
    
#exceptions as control flow
def get_ratios(L1, L2):
    """
    assume L1 L2 lists containing equal length of ints
    returns L3 such that L3[i] = L1[i] / L2[i]
    """
    L3 = []
    for i in range(len(L1)):
        try:
            L3.append(L1[i]/L2[i])
        
        except ZeroDivisionError:
            L3.append(float('nan'))
            
        except:
            raise ValueError("get_ratios called with bad arg")
        else:
            print("succeed")
        finally:
            print("print no matter what")
    return L3


L1 = [1,2,3,4]
L2 = [1,3,0,'a']
L3 = get_ratios(L1,L2)  
print(L3)  

#examples of exceptions
test_grades = [[['peter', 'parker'], [80.0, 70.0, 85.0]], [['bruce', 'wayne'], [100.0, 80.0, 74.0]]]

def get_avg(grade):
    """
    takes in grade of type list
    returns the average of the elements from the list
    """
    try:
        result = sum(grade)/len(grade)
    except ZeroDivisionError:
        print("warning: no grade data")
        result = 0
    return result

#test get_avg function
a = []
print(get_avg(a))



def get_new_class(data):
    """
    takes in a class data of the structure: each element has two parts: student name and student grades. 
    each part is a list
    """
    new_data = []
    for person in data:
        new_data.append([person[0], person[1], get_avg(person[1])])
    return new_data



test_grades = [[['peter', 'parker'], [80.0, 70.0, 85.0]], 
              [['bruce', 'wayne'], [100.0, 80.0, 74.0]],
              [['captain', 'america'], [80.0, 70.0, 96.0]],
              [['deadpool'], []]]

print(get_new_class(test_grades))


#Assertion
def avg(grades):
    assert len(grades) != 0, 'no grades data'
    return sum(grades)/len(grades)


avg([])
