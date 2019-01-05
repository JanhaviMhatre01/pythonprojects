'''
/**********************************************************************************
* Purpose: Write a program Distance.java that takes two integer command­line arguments x
* and y and prints the Euclidean distance from the point (x, y) to the origin (0, 0). The
* formulae to calculate distance = sqrt(x*x + y*y). Use Math.power function
*
* @author : Janhavi Mhatre
* @python version 3.7
* @platform : PyCharm
* @since 21-12-2018
*
***********************************************************************************/
'''

from utilities import utility
x = int(input("enter x co ordinate: "))   # take (x,y) input
y = int(input("enter y co ordinate: "))


utility.distance(x,y)

