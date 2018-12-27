'''
/**********************************************************************************
* Purpose: To the Util Class add temperatur Conversion static function, given the temperature
* in fahrenheit as input outputs the temperature in Celsius or viceversa
* logic :
*
* @author : Janhavi Mhatre
* @python version 3.7
* @platform : PyCharm
* @since 26-12-2018
*
***********************************************************************************/
'''

from utilities import utility
n = int(input("select 1 for fahrenheit to Celsius..... and select 2 for Celsius to fahrenheit "))
if n == 1:                                                # choose between 1/2

    f = int(input("temperature in fahrenheit: "))         # 1 for fahrenheit to Celsius
    utility.f_to_c(f)                                       # 2 for Celsius to fahrenheit

elif n == 2:
    c = int(input("temperature in Celsius: "))
    utility.c_to_f(c)

else:                            # if user choose other than 1/2 it will show wrong choice
    print("wrong choice")
