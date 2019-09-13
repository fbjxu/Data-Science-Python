# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# =============================================================================
# iterate over tuples
# =============================================================================

tswift = ((2014,"Katy"),
          (2014, "Harry"),
          (2012,"Jake"), 
          (2010,"Taylor"), 
          (2008,"Joe"),
          (2008, "Joe"))    

def get_data(aTuple):
    """
    aTuple, tuple of tuples (int, string)
    Extracts all integers from aTuple and sets 
    them as elements in a new tuple. 
    Extracts all unique strings from from aTuple 
    and sets them as elements in a new tuple.
    Returns a tuple of the minimum integer, the
    maximum integer, and the number of unique strings
    """
    num = ()
    words = ()
    for a in aTuple:
        num += (a[0],) #when concatenate tuples, remember the tuple singleton is (a,)
        if a[1] not in words:
            words += (a[1],)
    
    maxnumber = max(num)
    minnumber = min(num)
    numdistinctword = len(words)
    
    return (maxnumber, minnumber, numdistinctword)

print(get_data(tswift))

# =============================================================================
# iterate over list: sum of elements
# =============================================================================

L = [1,3,4,5,6]

#using loops
total = 0
for i in range(len(L)):
    total += L[i]
print(total)

#using pythonic approach
total = 0
for i in L:
    total += i
print(total)

# =============================================================================
# convert lists to strings and back
# =============================================================================
s = "i<3 cs"
list(s) #convert string to list: each char is an element in the list
s.split(" ") #convert string to list but seperate elements based on the provided character
L = ["a","b","c"]
'***'.join(L) #convert list to string

# =============================================================================
# Alias: mutation and iteration: how to use cloning to avoid list's side effects
# =============================================================================
def remove_dups(L1, L2):
    for e in L1:
        if e in L2:
            L1.remove(e)
      
def remove_dups_new(L1,L2):
    L3 = L1[:]
    for e in L3:
        if e in L2:
            L1.remove(e)
    return None

L1 = [1, 2, 3, 4]
L2 = [1, 2, 5, 6]
remove_dups(L1, L2)
print(L1, L2)

L1 = [1, 2, 3, 4]
L2 = [1, 2, 5, 6]
remove_dups_new(L1, L2)
print(L1, L2)