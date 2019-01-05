'''
/**********************************************************************************
* Purpose: 2d array of prime numbers which are anagram

* @author : Janhavi Mhatre
* @python version 3.7
* @platform : PyCharm
* @since 5-1-2019
*
***********************************************************************************/
'''
import numpy as np


class Prime:
    def __init__(self):

        self.prime_list = []

    def prime_num(self):

        for self.num in range(0, 1000):  # take range of 0-1000 numbers
            if self.num > 1:  # number should be greater than 1 as 1 is not prime and number should be non negative
                for self.x in range(2, self.num):  # range between 2 to given number as 2 is prime number
                    if (self.num % self.x) == 0:  # if given number mod number in range is 0 then it is prime
                        break
                else:
                    self.prime_list.append(self.num)

    # print(prime_list)

    # create duplicate array
    def anag(self):
        self.prime = self.prime_list.copy()  # copy list

        self.prime = [str(self.j) for self.j in self.prime]  # convert into string

        self.prime = [[self.n for self.n in self.j] for self.j in self.prime]  # convert "13" to ['1','3']
        # print(prime)

        self.anagram_list = []

        for self.i in range(len(self.prime)):
            for self.j in range(self.i + 1, len(self.prime)):
                if sorted(self.prime[self.i]) == sorted(
                        self.prime[self.j]):  # if sorted list are equal then numbers are anagram
                    self.anagram_list.append(self.prime[self.i])  # append both numbers to list
                    self.anagram_list.append(self.prime[self.j])
        # print(anagram_list)
        # anagram_list = [[int(n) for n in j] for j in anagram_list]
        self.ana = []
        for self.i in self.anagram_list:
            self.anagrams = "".join(map(str, self.i))  # convert separate strings to single string
            self.ana.append(self.anagrams)
        self.ana = [int(self.i) for self.i in self.ana]  # convert single string to integer
        print("anagrams ", self.ana)

        self.a = np.array(self.ana)  # use numpy to represent list in matrix form
        print('''
            "anagram numbers ................"
            ''')
        print(self.a)

    def non_anag(self):
        self.a_list = list(self.a)
        self.not_anagram = []
        for self.i in self.prime_list:
            if self.i not in self.a_list:
                self.not_anagram.append(self.i)
        # print(not_anagram)
        self.not_anagram = np.array(self.not_anagram)
        print('''
              "not anagram numbers ................"
              ''')
        print(self.not_anagram)


c = Prime()
c.prime_num()
c.anag()
c.non_anag()
