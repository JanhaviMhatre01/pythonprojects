'''
/**********************************************************************************
* Purpose: construct an algorithm to input a string of characters and check whether it is
* a palindrome. use a deque to store the characters of the string. We will process the string
* from left to right and add each character to the rear of the deque

* @author : Janhavi Mhatre
* @python version 3.7
* @platform : PyCharm
* @since 2-1-2019
*
***********************************************************************************/
'''


class Palindrome:
    def __init__(self):  # constructor for palindrome
        self.ele = "malayalam"            # input string to check whether it is palindrome
        self.list_string = list(self.ele)  # store input string in form of list
        self.dequeue_list = list()         # empty dequeue list which will store reverse string

    def remove_front(self):
        self.r = self.list_string.pop(0)   # remove 1st element
        self.insert_rear()

    def insert_rear(self):

        return self.dequeue_list.insert(1-len(self.ele), self.r)  # insert removed element at the end

    def show(self):
        return self.list_string, self.dequeue_list   # print original list and new list


p = Palindrome()

print(p.show())

for i in range(0, len(p.list_string)):
    p.remove_front()     # perform pop operation from 0 to length of list
    print(p.show())

new = "".join(p.dequeue_list)   # convert list to string
print(new)

if p.ele == new:            # check if original string is equal to new string
    print("palindrome")

else:
    print("not palindrome")
