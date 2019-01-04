'''
/**********************************************************************************
* Purpose: Ensure parentheses must appear in a balanced fashion.

* @author : Janhavi Mhatre
* @python version 3.7
* @platform : PyCharm
* @since 28-12-2018
*
***********************************************************************************/
'''


class Stack:      # create class stack
    def __init__(self):
        self.elements = []   # constructor for stack and store stack elements in list

    def push(self, data):
        self.elements.append(data)    # push function will append data to the stack

    def pop(self):                    # pop function will remove data from stack
        return self.elements.pop()

    def show(self):
        # print(self.items)
        return self.elements         # display stack

    def isEmpty(self):
        return self.elements == []     # checking whether stack is empty or not

    def peek(self):  # take starting element of stack
        if not self.isEmpty():
            return self.elements[-1]   # -1 represents top element of list

    def __sizeof__(self):
        # return self.items
        print(len(self.elements))  # length of stack


s = Stack()   # object of class Stack

exp = "(5+6)∗(7+8)/(4+3)(5+6)∗(7+8)/(4+3)"   # expression to be check

for i in exp:
    if i == '(':      # if ( found then push to stack
        s.push(i)

    elif i == ')':     # if ) found then pop (

        if s.isEmpty():  # check stack is empty or not
            is_balanced = False  # consider exp is not balanced
            break
        s.pop()

else:
    if s.isEmpty():
        is_balanced = True  # if balanced then print true
    else:
        is_balanced = False  # if not balanced print false

if is_balanced:
    print(True)
else:
    print(False)
