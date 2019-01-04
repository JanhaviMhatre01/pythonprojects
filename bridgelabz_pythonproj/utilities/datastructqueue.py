'''
this is basic code for creating Node and queue in which nodes stores values. enqueue is used to
add elements. dequeue use to remove element. Size will give size of linked list. show is used to
display linked list
'''



class Node:

    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Queue:
    front = None
    rear = None

    def __init__(self):

        pass

    def enqueue(self, data):

        node = Node(data)

        if self.front == None and self.rear == None:

            self.front = node
            self.rear = node

        else:

            self.rear.next = node
            self.rear = self.rear.next

    def show(self):

        if self.front == None:
            print("Linked List  is empty")
            return

        while self.front.next != None:
            print(self.front.data)
            self.front = self.front.next

        print(self.front.data)

    def dequeue(self):

        temp = self.front
        self.front = self.front.next
        return temp.data

    def is_empty(self):

        if self.front == None:
            return True
        else:
            return False

    def size(self):

        size = 1
        traverse = self.front
        if self.front == None:
            return 0

        while traverse.next != None:
            traverse = traverse.next
            size += 1
        return size


queue = Queue()
