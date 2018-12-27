'''
/**********************************************************************************
* Purpose: To the Util Class add dayOfWeek static function that takes a date as input and
* prints the day of the week that date falls on.
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
day = int(input("enter day: "))
if day > 0 and day <32:
    Month = int(input("enter month: "))
    if Month>0 and Month<13:
        year = input("enter year: ")
        if len(year)==4:
            utility.dayweek(day,Month,year)
        else:
            print("invalid year")
    else:
        print("invalid month")

else:
    print("invalid input")