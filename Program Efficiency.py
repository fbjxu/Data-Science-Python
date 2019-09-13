#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 15:12:06 2019

@author: lazybear
"""
#linear bisection search algorithm
def bisect_search_linear(L,e):
    if len(L) == 0 :
        return False
    elif len(L) ==1:
        return L[0] == e
    else:
        mid = (0 + len(L) -1) //2
        print('low:', L[0], 'high:', L[len(L)-1])
        if L[mid] == e:
            return True
        if L[mid] < e:
            return bisect_search_linear(L[mid+1:],e)
        else:
            return bisect_search_linear(L[:mid],e)

#logarithmic bisection search algorithm
def bisect_search(L,e):
    '''
    L is the list to search the element e
    '''
    def bisect_helper(L,e,low, high):
        print('low:', str(low), 'high:', str(high))
        if low == high:
            return L[low] == e
        mid = (low+high)//2
        if L[mid] == e:
            return True
        elif L[mid] > e:
            if mid == low:
                return L[mid] == e
            return bisect_helper(L,e,low, mid-1)
        else:
            return bisect_helper(L,e,mid+1, high)
    
    if len(L) == 0:
        return False
    else:
        return bisect_helper(L, e, 0, len(L)-1)

test = []
for i in range(100):
    test.append(i)

bisect_search(test, 76)
            
def genSubsets(L):
    if len(L) == 0:
        return [[]] #list of empty list
    smaller = genSubsets(L[:-1]) # all subsets without last element
    extra = L[-1:] # create a list of just last element
    new = []
    for small in smaller:
        new.append(small+extra)  # for all smaller solutions, add one with last element
    return smaller+new  # combine those with last element and those without


testSet = [1,2,3,4,5]
print(genSubsets(testSet))