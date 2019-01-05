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

filename = "/home/admin1/bridgelabz_pythonproj/sample.txt"


with open(filename) as f:
     list_file = f.read().split(",")
     list_file[-1]=list_file[-1].strip()


utility.filesearching(list_file)

