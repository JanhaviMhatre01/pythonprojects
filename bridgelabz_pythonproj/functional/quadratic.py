'''
/**********************************************************************************
* Purpose: Write a program Quadratic.java to find the roots of the equation a*x*x + b*x + c.
* Since the equation is x*x, hence there are 2 roots.
*
* @author : Janhavi Mhatre
* @python version 3.7
* @platform : PyCharm
* @since 21-12-2018
*
***********************************************************************************/
'''

from utilities import utility

print("quadratic equation in form of a*x*x + b*x + c")
a = int(input("value of a: "))
b = int(input("value of b: "))
c = int(input("value of c: "))

utility.qua(a, b, c)
