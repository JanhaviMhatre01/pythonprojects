'''
/**********************************************************************************
* Purpose: Ensure parentheses must appear in a balanced fashion.

* @author : Janhavi Mhatre
* @python version 3.7
* @platform : PyCharm
* @since 26-12-2018
*
***********************************************************************************/
'''


class Stack:
    def __init__(self):
        self.items = []

    def push(self, data):
        self.items.append(data)

    def pop(self):
        return self.items.pop()

    def show(self):
        # print(self.items)
        return self.items

    def isEmpty(self):
        return self.items == []

    def peek(self):  # top of the stack means last data
        if not self.isEmpty():
            return self.items[-1]

    def __sizeof__(self):
        # return self.items
        print(len(self.items))


s = Stack()

exp = "(5+6)∗(7+8)/(4+3)(5+6)∗(7+8)/(4+3)"

for c in exp:
    if c == '(':
        s.push(c)

    elif c == ')':

        if s.isEmpty():
            is_balanced = False
            break
        s.pop()

else:
    if s.isEmpty():
        is_balanced = True
    else:
        is_balanced = False

if is_balanced:
    print(True)
else:
    print(False)
