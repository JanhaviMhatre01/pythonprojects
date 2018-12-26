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
list_string=["janhavi","rohini","nikhil","pushkar","abhishek","gautami"]
list_int=[7,3,5,2,1]
#
key=int(input("enter number to be search: "))
utility.binarysearchint(list_int,key)
#
key2=input("enter string to be search: ")
utility.binarysearchstring(list_string,key2)

utility.bubblesortint(list_int)
utility.bubblesortstring(list_string)
utility.insertionsortint(list_int)
utility.insertionsortstring(list_string)







