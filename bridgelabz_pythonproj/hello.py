class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext


class OrderedList:
    def __init__(self):
        self.head = None

    def search(self,item):
        current = self.head
        found = False
        stop = False
        while current != None and not found and not stop:
            if current.getData() == item:
                found = True
            else:
                if current.getData() > item:
                    stop = True
                else:
                    current = current.getNext()

        return found

    def display(self):  # to display list

        elements = []  # list to
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
            elements.append(current_node.data)
        print('data in linked list ', elements)
        #find_word = input("Enter the element to search ")
        #my_list.search(find_word, elements)

    def add(self,item):
        current = self.head
        previous = None
        stop = False
        while current != None and not stop:
            if current.getData() > item:
                stop = True
            else:
                previous = current
                current = current.getNext()

        temp = Node(item)
        if previous == None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)

    def isEmpty(self):
        return self.head == None

    


mylist = OrderedList()
# mylist.add(31)
# mylist.add(77)
# mylist.add(17)
# mylist.add(93)
# mylist.add(26)
# mylist.add(54)

file = open("/home/admin1/bridgelabz_pythonproj/sampleint.txt", 'r')  # Open the file in Read mode into variable file
d = file.read().split(",")  # Read the file separate by ,
d[-1] = d[-1].strip()

word_list = []
new = str(d).strip('[]')
for word in d:
    word_list.append(word)
    #word_list.sort()

print('elements from  file : ', word_list)

#mylist.display()


