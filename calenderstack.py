'''
/**********************************************************************************
* Purpose: calender using stack

* @author : Janhavi Mhatre
* @python version 3.7
* @platform : PyCharm
* @since 5-1-2019
*
***********************************************************************************/
'''
from utilities import utility
from utilities import datastructqueue
'''
store week days and total number of days in list.
this calender is implemented using stack operations
We are creating 2 stacks hence there are two objects of same class stack 
Operation works as : Push elements in one stack then pop that element and push to another stack
At the end justify the dates and pop the starting dates if the starting days are blank
The reason we have to maintain 2 stacks is stack works on LIFO so the last day will displayed at 1st
date if 2nd stack is not used.
'''
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

print('calender')

for i in range(0, 6 + 1):
    print(day[i], end=' ')
print()
for i in range(row):

    for j in range(column):

        if values <= days[m - 1]:
            if i == 0 and j < d0:
                datastructqueue.stack.push(' ')
                continue

            datastructqueue.stack.push(values)
            values += 1

for i in range(datastructqueue.stack.size()):
    stack_element = datastructqueue.stack.pop()
    #print(stack_element)
    datastructqueue.stack1.push(stack_element)

for i in range(row):

    for j in range(column):
        if datastructqueue.stack1.size() > 0:
            x = datastructqueue.stack1.pop()
            x1 = str(x).ljust(2)
            print(x1, end=" ")

    print()
