'''
/**********************************************************************************
* Purpose: Read .a List of Numbers from a file and arrange it ascending Order in a Linked List. Take user
* input for a number, if found then pop the number out of the list else insert the number in appropriate position
*
* @author : Janhavi Mhatre
* @python version 3.7
* @platform : PyCharm
* @since 28-12-2018
*
***********************************************************************************/
'''


class Node:
    def __init__(self, data=None):
        self.data = data  # data node
        self.next = None  # last element of list will always has none .
        self.next_node = next

    def get_data(self):  # gets the data of node
        return self.data

    def get_next(self):  # gets next node
        return self.next

    def set_next(self, new_next):  # sets the next element to other next node.
        self.next = new_next


class LinkedList:  # wrapper class for node class
    def __init__(self):
        self.head = Node()  # simply used as placeholder to
        # allow us to point to first node.

    def add(self, data):  # appends  element to list
        new_node = Node(data)  # creates a new node using class node .
        current = self.head  # point to start iteration from head
        while current.next is not None:  # while next element  is not Null
            current = current.next  # sets the current node to next node
        current.next = new_node  # create  the new node after current node

    def length(self):  # calculates length of list
        current = self.head  # at start nodes starts from Head
        total = 0  # variable to count the nodes.

        while current:  # while current = True
            total += 1  # incrementing total.
            current = current.get_next()  # current element = next element until loop finishes
        return total

    def display(self):  # to display list

        elements = []  # list to store elements in linked list
        current_node = self.head
        while current_node.next is not None:  # if there is no value in linked list then start loop
            current_node = current_node.next
            elements.append(current_node.data)   # append data to element list
        print('data in linked list ', elements)
        find_word = input("Enter the element to search ")
        my_list.search(find_word, elements)  # search in linked list, given number in elements list

    def search(self, data, elements):    # function to search element
        current = self.head
        found = False                # initialise that element to be search is not found
        while current and found is False:
            if current.get_data() == data:   # fetch the data using get_data
                found = True
                print("Element found ")
                my_list.delete(data, elements)   # if searched element found then delete that element from linked list

                print("Element deleted: ")
                my_list.write(elements)

            else:
                current = current.get_next()
        if current is None:
            print("Data was not in list and added to list")
            my_list.add(data)     # if searched element not found then add to list
            # at particular position such that list is sorted

        return current

    def delete(self, data, elements):         # delete function
        current = self.head
        previous = None
        found = False
        while current and found is False:           # search procedure
            if current.get_data() == data:
                found = True

            else:
                previous = current            # after deleting node assign previous node to current
                current = current.get_next()  # current node will get index of next
        if current is None:
            print("Data not in list")
        if previous is None:
            self.head = current.get_next()     # add node in particular position and get index of next
        else:
            previous.set_next(current.get_next())

    def write(self, elements):                # write in file
        f1 = open('/home/admin1/bridgelabz_pythonproj/sampleint.txt', 'w')  # open file in write mode
        f1.close()
        with open('/home/admin1/bridgelabz_pythonproj/sampleint.txt', 'a') as f:  # open file in append mode
            elements.sort()                                                # sort elements in file as it is ordered list
            f.write(','.join(str(word) for word in elements))   # added element should be ',' separated


my_list = LinkedList()   # declaring my_list as linked list

file = open("/home/admin1/bridgelabz_pythonproj/sampleint.txt", 'r')  # Open the file in Read mode into variable file
d = file.read().split(",")  # Read the file separate by ,
d[-1] = d[-1].strip()  # removes space after end element

word_list = []   # store elements from file in list
new = str(d).strip('[]')
for word in d:
    word_list.append(word)
    word_list.sort()      # sorting

print('elements from  file : ', word_list)

for i in word_list:
    my_list.add(i)  # add elements from list word_list to linked list

print("data in linked list")

my_list.display()   # display linked list without changes

my_list.display()    # display linked list with changes
