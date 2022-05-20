# Grade Calculator MH 5/22
import math

def grade(missed,total,highestgrade):
    return math.ceil(highestgrade-(missed/total*highestgrade))

print(grade(2.25,6,100))
