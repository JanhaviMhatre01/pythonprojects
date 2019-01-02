class Node:
    def __init__(self, data=None, next=None):
        self.data = data  # data node
        self.next = None  # last element of list will alwasys has none .
        self.next_node = next

    def get_data(self):  # gets the data of node
        return self.data

    def get_next(self):  # gets next node
        return self.next

    def set_next(self, new_next):  # used while deleting: sets the next element to other next node.
        self.next = new_next


class LinkedList:  # wrapper class for node class. user will never interface with node
    def __init__(self):
        self.head = Node()  # never gonna contain any actual data and not indexable.  simply used as placeholder to allow us to point to first node.

    def add(self, data):  # appends  element to list
        new_node = Node(data)  # creates a new node using class node .
        current = self.head  # point to start iteration from ... first node
        while current.next != None:  # while next element  is not Null
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

        elements = []  # list to
        current_node = self.head
        while current_node.next != None:
            current_node = current_node.next
            elements.append(current_node.data)
        print('data in linked list ', elements)
        findword = input("Enter the element to search ")
        my_list.search(findword, elements)

    def search(self, data, elements):
        current = self.head
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
                print("Element found ")
                my_list.delete(data, elements)
                print("Element deleted: ")
                my_list.write(elements)
            else:
                current = current.get_next()
        if current is None:
            print("Data was not in list and added to list")
            my_list.add(data)
        return current

    def delete(self, data, elements):
        current = self.head
        previous = None
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True

            else:
                previous = current
                current = current.get_next()
        if current is None:
            print("Data not in list")
        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())

    def write(self, elements):
        f1 = open('/home/admin1/bridgelabz_pythonproj/sampletext.txt', 'w')
        f1.close()
        with open('/home/admin1/bridgelabz_pythonproj/sampletext.txt', 'a') as f:
            f.write(','.join(str(word) for word in elements))


my_list = LinkedList()

file = open("/home/admin1/bridgelabz_pythonproj/sampletext.txt", 'r')  # Open the file in Read mode into variable file
d = file.read().split(",")  # Read the file seperate by ,
d[-1] = d[-1].strip()

word_list = []
newd = str(d).strip('[]')
for word in d:
    word_list.append(word)

print('elements from  file : ', word_list)

for i in word_list:
    my_list.add(i)
print("data in linked list")
my_list.display()
my_list.display()
