'''
/**********************************************************************************
* Purpose: Prints the harmonic value: 1/1 + 1/2 + ... + 1/N
*
* @author : Janhavi Mhatre
* @python version 3.7
* @platform : PyCharm
* @since 21-12-2018
*
***********************************************************************************/
'''
from utilities import utility
a = [int(x) for x in input("enter list elements: ").split( )]
print(a)
n = len(a)
utility.disttriples(a,n)
