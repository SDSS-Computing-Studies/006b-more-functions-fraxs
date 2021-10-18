#!python3
"""
##### Problem 2
Create a function that determines if a triangle is scalene, right or obtuse.  
3 input parameters:  
float: one side  
float: another side  
float: 3rd side  

return:
0 : triangle does not exist
1 : if the triangle is scalene
2 : if the triangle is right
3 : if the triangle is obtuse

Sample assertions:  
assert triangle(12,5,13) == 2     
assert triangle(5,3,3) == 1  
assert triangle(5,15,12) == 3  
assert triangle(1,1,4) == 0  
(2 points)
"""
def triangle(x,y,z):
    import math
    list1 = [x,y,z]
    list1.sort
    a = list1[0]
    b = list1[1]
    c = list1[2]
    if c > a+b:
        return 0
    elif math.sqrt( (a**2)+(b**2) ) == c:
        return 2
    elif c > math.sqrt( (a**2)+(b**2) ):
        return 3
    elif c < math.sqrt( (a**2)+(b**2) ):
        return 1

