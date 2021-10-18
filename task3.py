#!python3

"""
Create a function that determines the length of a hypotenuse given the lengths of 2
shorter sides
2 input parameters
float: the length of one side of a right triangle
float: the length of the other side of a right triangle

return: float value for the length of the hypotenuse

Sample assertions:
assert hypotenuse(6,8) == 10
(2 points)
"""


def hypotenuse(x,y):
    import math
    side1 = x**2
    side2 = y**2
    hyp = math.sqrt(side1+side2)
    return hyp
assert hypotenuse(6,8) == 10