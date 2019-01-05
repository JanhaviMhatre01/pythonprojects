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

try:  # handle error if user input is 0
    N = int(input("enter harmonic value N: "))
    if N != 0:  # checking if N is not equal to 0
        utility.harmonic_value(N)
    else:
        raise ZeroDivisionError     # number can not be divided by 0 hence raise exception to handle it



except ZeroDivisionError:
    print('Handling run-time error: N should not be zero')  # if user input is 0 then print this error


