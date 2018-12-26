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
try:
    intlist = list(input("Enter elements separated by spaces").split(" "))
    intlist = [int(x) for x in intlist]

except ValueError:
    print("only int")


utility.userint(intlist)



