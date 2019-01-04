'''
/**********************************************************************************
* Purpose: Write a program Calendar.java that takes the month and year as command­line
* arguments and prints the Calendar of the month. Store the Calendar in an 2D Array,
* the first dimension the week of the month and the second dimension stores the day
* of the week.

* @author : Janhavi Mhatre
* @python version 3.7
* @platform : PyCharm
* @since 3-1-2019
*
***********************************************************************************/
'''
from utilities import utility

month = int(input("enter month : "))
year = int(input("enter year : "))
day = ['S', ' M', ' T', ' W', ' Th', 'F', ' S']

days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

values = 1
d = 1
m = month
y = year
y0 = y - (14 - m) // 12
x = y0 + y0 // 4 - y0 // 100 + y0 // 400
m0 = m + 12 * ((14 - m) // 12) - 2
d0 = (d + x + 31 * m0 // 12) % 7

if utility.check_leap(str(year)):
    days[1] = 29
row = 6
column = 7
array = [[0 for j in range(column)] for i in range(row)]  # create 2d array

print('calender')

for i in range(0, 7):
    print(day[i], end=' ')  # get days
print()
for i in range(row):

    for j in range(column):

        if values <= days[m - 1]:  # get number of dates
            if i == 0 and j < d0:
                array[i][j] = ' '
                continue

            array[i][j] = values
            values += 1

for i in range(row):

    for j in range(column):
        if array[i][j] != 0:   # print dates
            x = array[i][j]
            x1 = str(x).ljust(2)  # justification or we can say padding
            print(x1, end=" ")

    print()
