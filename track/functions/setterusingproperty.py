from os import name
from _winapi import REALTIME_PRIORITY_CLASS
class Student:
    def __init__(self,roll,name):
        self.__roll=roll
        self.__name=name
    @property
    def roll(self):
        return self.__roll
    @property
    def name(self):
        return self.__name
    @roll.setter
    def roll(self,roll):
        self.__roll=roll
    @name.setter
    def name(self,name):
        self.__name=name
s1=Student(11,"Vinnu")
print(s1.roll)
print(s1.name)

s1.roll=22

s1.name="vinu"
print(s1.roll)
print(s1.name)