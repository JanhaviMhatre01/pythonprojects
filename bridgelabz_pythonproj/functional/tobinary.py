'''
/**********************************************************************************
* Purpose: Write a static function toBinary that outputs the binary (base 2) representation of
* the decimal number typed as the input. It is based on decomposing the number into
* a sum of powers of 2
* logic :
* @author : Janhavi Mhatre
* @python version 3.7
* @platform : PyCharm
* @since 27-12-2018
*
***********************************************************************************/
'''
from utilities import utility

n = int(input("enter the number to see its binary representation: "))

utility.convert_binary(n)

print(utility.convert_binary(n))
