#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 17:58:19 2019

@author: lazybear
"""

class Animal(object):
    def __init__(self, age):
        self.age = age
        self.name = None
    def get_age(self):
        return self.age
    def get_name(self):
        return self.name
    def set_age(self, newage):
        self.age = newage
    def set_name(self, newname):
        self.name = newname
    def __str__(self): #note for __str__ it has to be return in the end. Not print()
        return "animal " + str(self.name) + ":" + str(self.age)
    
        
        
class Cat(Animal):
    def speak(self):
        print("meow")
        
    def __str__(self):
        return "cat " + str(self.name) + ":" + str(self.age)

kitty = Cat(3)

class Person(Animal):
    def __init__(self, name, age):#note that the order of the parameter matters!
        Animal.__init__(self, age)
        self.set_name(name) #note that there is no assignment needed! The setter function
                     #can be directly used 
        self.friend = []
    
    def get_friends(self):
        return self.friend
    
    def add_friend(self, fname):
        if not fname in self.friend:
            self.friend.append(fname)
    
    def speak(self):
        print("hello")
    
    def age_diff(self, other):
        other_age = other.age
        self_age = self.age
        diff = abs(other_age - self_age)
        print( str(diff) + ' years of differences')
    
    def __str__(self):
        return 'Person ' + str(self.name) + ':' + str(self.age)

print("\n---- person tests ----")
p1 = Person("jack", 30)
p2 = Person("jill", 25)
print(p1.get_name())
print(p1.get_age())
print(p2.get_name())
print(p2.get_age())
print(p1)
p1.speak()
p1.age_diff(p2)


import random

class Student(Person):
    def __init__(self, name, age, major = None):
        Person.__init__(self, name, age)
        self.major = major
    
    def change_major(self, major):
        self.major = major
        
    def speak(self):
        r = random.random() #gives back float [0,1) note the float does not include 1 but include 0
        if r < .25:
            print('I have homework')
        elif r>=.25 and r<.5:
            print('I need to sleep')
        elif .5<=r<=7.5:
            print('I should eat')
        else:
            print('I am watching tv')
    
    def __str__(self):
        return 'Student: ' + str(self.name) + ':' + str(self.age)+":"+str(self.major)

print("\n---- student tests ----")
s1 = Student('alice', 20, "CS")
s2 = Student('beth', 18)
print(s1) #should print Student:alice:20:CS
print(s2) #should print Student:beth:18:None
print(s1.get_name(),"says:", end=" ") 
s1.speak() #should print: alice says XXXX
print(s2.get_name(),"says:", end=" ")
s2.speak()

class Rabbit(Animal):
    tag = 1 #class variable
    def __init__(self, age, parent1 = None, parent2 = None): #Argument Default
        Animal.__init__(self, age)
        self.parent1 = parent1
        self.parent2 = parent2
        self.rid = Rabbit.tag #access class variable
        Rabbit.tag += 1 #increment class variable changes it for all instances that may 
                        #refer to it
    #getter functions
    def get_rid(self):
        return str(self.rid).zfill(3) #method on a string to pad the beginning with zeros (001)
    
    def get_parent1(self):
        return self.parent1
    
    def get_parent2(self):
        return self.parent2
    
    def __add__(self, other):
        # returning object of same type as this class
        return Rabbit(0, self, other)
    
    def __eq__(self, other): #use rid instead of parents themselves: 
                            #that will return none since __eq__ define equal sign for rabbit objects
        parents_same = self.parent1.rid == other.parent1.rid \
            and self.parent2.rid == other.parent2.rid # use \ when one line can't fit
        parents_opposite = self.parent1.rid == other.parent2.rid \
            and self.parent2.rid == other.parent1.rid
        return parents_same or parents_opposite
    def __str__(self):
        return "rabbit:"+ self.get_rid()
    


print("\n---- rabbit tests ----")
print("---- testing creating rabbits ----")
r1 = Rabbit(3)
r2 = Rabbit(4)
r3 = Rabbit(5)
print("r1:", r1)
print("r2:", r2)
print("r3:", r3)
print("r1 parent1:", r1.get_parent1())
print("r1 parent2:", r1.get_parent2())

print("---- testing rabbit addition ----")
r4 = r1+r2   # r1.__add__(r2)
print("r1:", r1)
print("r2:", r2)
print("r4:", r4)
print("r4 parent1:", r4.get_parent1())
print("r4 parent2:", r4.get_parent2())

print("---- testing rabbit equality ----")
r5 = r3+r4
r6 = r4+r3
print("r3:", r3)
print("r4:", r4)
print("r5:", r5)
print("r6:", r6)
print("r5 parent1:", r5.get_parent1())
print("r5 parent2:", r5.get_parent2())
print("r6 parent1:", r6.get_parent1())
print("r6 parent2:", r6.get_parent2())
print("r5 and r6 have same parents?", r5 == r6)
print("r4 and r6 have same parents?", r4 == r6)

    
    
        
    
        