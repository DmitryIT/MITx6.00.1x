import math
"""
This function sums the area and square of the perimeter of the regular polygon.
The function returns the sum, rounded to 4 decimal places.
Input parameters: n - number of polygon sides
                  s - length of polygon side
Functions: area - computes area of the polygon
           perimeter - computes perimeter of the polygon
"""
def area(n,s):
    return (0.25 * n * s * s)/(math.tan(math.pi/n))

def perimeter(n,s):
    return n*s

def polysum(n,s):
    return round(area(n,s) + perimeter(n,s)**2,4)
