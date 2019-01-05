'''
/**********************************************************************************
* Purpose: his program takes a command­line argument N and prints a table of the
* powers of 2 that are less than or equal to 2^N.
*
* @author : Janhavi Mhatre
* @python version 3.7
* @platform : PyCharm
* @since 21-12-2018
*
***********************************************************************************/
'''
from utilities import utility
N = int(input("enter power value N: "))  # take power value from user i.e if 2^N then ask for N
utility.power_two(N)