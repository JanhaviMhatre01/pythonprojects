'''
/**********************************************************************************
* Purpose: prime numbers in 2d array of range 100

* @author : Janhavi Mhatre
* @python version 3.7
* @platform : PyCharm
* @since 5-1-2019
*
***********************************************************************************/
'''

prime_list=[]
for num in range(0, 1000):  # take range of 0-1000 numbers
    if num > 1:  # number should be greater than 1 as 1 is not prime and number should be non negative
        for x in range(2, num):  # range between 2 to given number as 2 is prime number
            if (num % x) == 0:  # if given number mod number in range is 0 then it is prime
                break
        else:
            prime_list.append(num)
#print(prime_list)
row = 10           # total rows require
column= 25          # total columns require
limit = 100        # range

arr = [[0 for y in range(column)] for x in range(row)]  # 2d array
#print(arr)
ele = 0  # get element from list

for x in range(row):
    for y in range(column):
        if ele < len(prime_list):
            if prime_list[ele] <= limit:
                arr[x][y] = prime_list[ele]  # append element to array
                ele += 1  # increment element value

    limit += 100  # after printing values between range of 100 increment limit

for i in range(row):  # printing 2d array

    for j in range(column):

        if arr[i][j] != 0:
            print(arr[i][j], end=" ")

    print()





