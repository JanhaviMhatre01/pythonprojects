'''
/**********************************************************************************
* Purpose: A program with cubic running time. Read in N integers and counts the
* number of triples that sum to exactly 0.
*
* @author : Janhavi Mhatre
* @python version 3.7
* @platform : PyCharm
* @since 22-12-2018
*
***********************************************************************************/
'''
from utilities import utility
a = [int(x) for x in input("enter list elements: ").split( )]
print(a)
n = len(a)
utility.dist_triples(a, n)
