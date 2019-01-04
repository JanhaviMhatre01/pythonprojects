'''
/**********************************************************************************
* Purpose: Create a Slot of 10 to store Chain of Numbers that belong to each Slot to
* efficiently search a number from a given set of number

* @author : Janhavi Mhatre
* @python version 3.7
* @platform : PyCharm
* @since 3-1-2019
*
***********************************************************************************/
'''


class Hashing:
    def __init__(self):
        self.size = 11     # size of slots is 11
        self.slot = [None] * self.size  # create list of given size
        self.data = [[] for _ in range(self.size)]  # create nested list of given size
        # print(self.slot)
        # print(self.data)
        filename = "/home/admin1/bridgelabz_pythonproj/samplelist.txt"
        with open(filename) as f:
            self.values = f.read().split(" ")
            self.values[-1] = self.values[-1].strip()
            self.values = [int(key) for key in self.values]
        print("elements in file ", self.values)  # file elements

    def hash_function(self, k):   # calculate hash function
        return k % 11             # key % size of slots
        # for self.key in self.values:
        #     self.h = self.key % 11
        #     return h

    def hash_list(self):
        h_list = []           # stores hash values
        for key in self.values:
            h_list.append(self.hash_function(key))    # append hash values to h_list
        print("hash values of elements in list ", h_list)

        for key in self.values:
            self.slot[self.hash_function(key)] = key    # append key according to hash values
            self.data[self.hash_function(key)].append(key)   # append key to list in list according to hash value

        print("with collision : ", self.slot)
        print("without collision ", self.data)



h = Hashing()
h.hash_list()
