'''
/**********************************************************************************
* Purpose: Write a Util Static Function to calculate monthlyPayment that reads in three
* command­line arguments P, Y, and R and calculates the monthly payments you
* would have to make over Y years to pay off a P principal loan amount at R per cent
* interest compounded monthly.
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

p = int(input("enter principal loan amount p: "))
y = int(input("enter years y: "))
r = int(input("enter rate r: "))

utility.monthly_pay(p, y, r)