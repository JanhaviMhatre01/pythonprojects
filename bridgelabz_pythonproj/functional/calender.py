'''
/**********************************************************************************
* Purpose: Create the Week Object having a list of WeekDay objects each storing the day (i.e
* S,M,T,W,Th,..) and the Date (1,2,3..) . The WeekDay objects are stored in a Queue
* implemented using Linked List. Further maintain also a Week Object in a Queue to
* finally display the Calendar

* @author : Janhavi Mhatre
* @python version 3.7
* @platform : PyCharm
* @since 3-1-2019
*
***********************************************************************************/
'''
from utilities import utility
from utilities import datastructqueue
month = int(input("enter month : "))
year = int(input("enter year : "))

day = ['S', ' M', ' T', ' W', ' Th', 'F', ' S']    # store day names

days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  # store total number of days in every month

values = 1
d = 1

m = month
y = year
y0 = y - (14 - m) // 12
x = y0 + y0 // 4 - y0 // 100 + y0 // 400
m0 = m + 12 * ((14 - m) // 12) - 2
d0 = (d + x + 31 * m0 // 12) % 7

if utility.check_leap(str(year)):   # check whether year is leap
    days[1] = 29  # if year is leap then change the days of feb to 29
row = 6       # number of rows
column = 7  # number of rows

print("calender")

for i in range(0, 7):     # print 7 days
    print(day[i], end=' ')
print()
for i in range(row):    # add days
    for j in range(column):
        if values <= days[m - 1]:   # get total days in month
            if i == 0 and j < d0:   # get day of date 1
                datastructqueue.queue.enqueue(' ')  # print days
                continue
            datastructqueue.queue.enqueue(values)
            values += 1

for i in range(row):   # print dates

    for j in range(column):
        if datastructqueue.queue.size() > 0:
            x = datastructqueue.queue.dequeue()
            x1 = str(x).ljust(2)   # justification
            print(x1, end=' ')

    print()



