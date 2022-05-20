# Grade Calculator MH 5/22
import math

def grade(missed,total,highestgrade):
    return math.ceil(highestgrade-(missed/total*highestgrade))

missed=int(input("How many problems were missed? "))
total=int(input("How many problems total? "))
highestgrade=int(input("What is the maximum grade? "))

print(grade(missed,total,highestgrade))
