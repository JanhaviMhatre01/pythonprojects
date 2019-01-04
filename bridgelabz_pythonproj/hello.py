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

size = 11

slot = [None] * size
data = [[] for _ in range(10)]

print("stores key values ", slot)
# print("stores key data ", data)

filename = "/home/admin1/bridgelabz_pythonproj/samplelist.txt"
with open(filename) as f:
    values = f.read().split(" ")
    values[-1] = values[-1].strip()

print("values in file: ", values)

values = [int(x) for x in values]
def hash_function(x):

    return x % 11


# values = [int(value) for value in values]

# hashvalues = map(hash_function, values)
# hashvalues = list(hashvalues)
# print("hash values ",hashvalues)



def insert(data, key, values):
    for i in values:
        #slot[hash_function(key)] = i
        data[hash_function(key)].append(i)
        #print(data)

insert(slot, 15, 'cat')
# insert(slot, 15, 'dog')

#print(slot)
#print(data)