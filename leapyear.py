'''
/**********************************************************************************
* Purpose: Determine if it is a Leap Year. Year should be of 4 digits.
* logic : first check given year is of 4 digits. Then check conditions for leap year
*
* @author : Janhavi Mhatre
* @python version 3.7
* @platform : PyCharm
* @since 21-12-2018
*
***********************************************************************************/
'''
from utilities import utility
year = input("enter year: ")   # ask user to enter year to check year is leap year or not
utility.check_leap(year)