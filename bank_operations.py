'''
/**********************************************************************************
* Purpose: Write a Queue Class to enqueue and dequeue people to either deposit
* or withdraw money and maintain the cash balance

* @author : Janhavi Mhatre
* @python version 3.7
* @platform : PyCharm
* @since 2-1-2019
*
***********************************************************************************/
'''


class Banks:
    total = 10000                     # initial amount in bank

    def __init__(self):  # constructor for bank
        self.Bank = [1, 2, 3, 4, 5]  # create queue Bank as a list

    def dequeue(self):
        return self.Bank.pop(0)  # after operations remove people from queue

    def show(self):
        return self.Bank          # display queue

    def withdraw(self):
        if self.total == 0:           # if the amount in bank is 0 then user can not withdraw
            print("only deposit")
            self.choice()              # choice between deposit or exit

        else:
            self.i = int(input("withdraw amount: "))     # withdraw amount
            self.remain = self.total - self.i            # remaining amount after withdraw
            print("remaining amount = ", self.remain)
            print(self.total)
            self.total = self.remain                    # current amount in bank
            print("total: ", self.total)
            self.dequeue()                              # remove user after withdraw task
            self.show()                                 # display the remaining queue

    def deposit(self):
        self.i = int(input("deposit amount: "))          # deposit amount
        self.remain = self.total + self.i                 # amount after deposit
        print("remaining amount = ", self.remain)
        print(self.total)
        self.total = self.remain                          # current amount after deposit
        print("total: ", self.total)
        self.dequeue()                                   # remove user after deposit
        self.show()                                      # display remaining queue

    def choice(self):                   # choose between withdraw, deposit or exit
        ch = int(input("1 : withdraw    2 : deposit    any : exit"))
        if ch == 1:
            q.withdraw()

        elif ch == 2:
            q.deposit()

        else:
            self.dequeue()              # if user choose to exit
            print("token removed")      # remove that token from queue


q = Banks()
print(q.show())

for n in range(0, len(q.Bank)):     # process will execute till end of queue
    print("welcome")
    print("your token number : ", q.Bank[0])
    q.choice()
