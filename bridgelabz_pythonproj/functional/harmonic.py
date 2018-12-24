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
    N = int(input("enter harmonic value N: "))
    if (N != 0):  # checking if N is not equal to 0
        utility.harmonicvalue(N)
    else:
        raise ZeroDivisionError



except ZeroDivisionError:
    print('Handling run-time error: N should not be zero')

'''
if(N!=0):          #checking if N is not equal to 0

    utility.harmonicvalue(N)

else:
    print("N should not be 0")
'''