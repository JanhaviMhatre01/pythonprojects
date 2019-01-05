'''
/**********************************************************************************
* Purpose: prime numbers which are anagram using queue

* @author : Janhavi Mhatre
* @python version 3.7
* @platform : PyCharm
* @since 5-1-2019
*
***********************************************************************************/
'''
from utilities import datastructqueue
from functional import primeanagram
l = primeanagram.c.a_list
for i in l:
    datastructqueue.queue.enqueue(i)  # push ith element to stack
print("queue ...")
for i in range(0, datastructqueue.queue.size()):
    print(datastructqueue.queue.dequeue(), end=" ")   # print pop elements
