import random
import math


# from functional import flipcoin

################################################################################
def accept():
    a = input("enter: ")


################################ REPLACE USERNAME ################################################

def Username(username):
    sentence = "Hello <<username>>, How are you?"  # store given label in sentence
    print(sentence)

    if len(username) <= 3:  # check length of string whether it is greater than 3 or equal to 3
        print("username should contain 3 letters or more")

    else:
        u = sentence.replace("<<username>>", username)  # replacing <<username>> with proper name entered by user
        print(u)


################################# FLIP COIN #################################################

def flips(n):
    h = 0  # initialise head and tail to 0
    t = 0

    for i in range(0, n):  # range between 0 to n
        coinface = random.uniform(0, 1)  # store randomly generated number between 0 to 1
        if (coinface > 0.5):  # check if randomly generated number is greater than 0.5
            h += 1  # if condition is true increament heads

        else:  # otherwise increament tails
            t += 1
    print("no of heads: ", h, "out of", n)
    print("no of tails: ", t, "out of", n)
    print("percent of heads: ", (h / n) * 100)  # (h / n) * 100 calculates percentage of heads
    print("percent of heads: ", (t / n) * 100)  # (t / n) * 100 calculates percentage of heads


'''
    repeats()

def repeats():
    again = input("do you want to do it agian? 0:yes 1:no")
    if again == 0:
        flipcoin()

    else:
        print("thanku")


if __name__ == '__main__': repeats()
'''


################################# LEAP YEAR ####################################################

def checkleap(year):
    if len(year) != 4:  # check length of year is 4 or not
        print("invalid year..it should be of 4 digits")

    else:
        year = int(year)
        if (
                year % 4 == 0 or year % 400 == 0 and year % 100 == 0):  # check whether conditions are satisfied for leap year or not
            print(year, " is leap year")

        else:
            print("this is not leap year")


##################################### POWER OF TWO ###############################################

def powertwo(N):
    if 0 <= N < 31:  # number should be between 0-31.otherwise it will overflows integer value
        for i in range(0, N):
            while (i <= N):  # code will execute till i = input value of N
                print("2 to the power of", i, "=", 2 ** i) #2**i is 2^i
                break

    else:
        print("N should be in range of 0 - 31")


#################################### HARMONIC VALUE ################################
def harmonicvalue(N):
    value = 0                        #initialise sum equal to 0
    for i in range(1, N + 1):
        value += 1 / i               #add values which are in range of 1 to N+1

    print("harmonic value is :", value)


###################################### PRIME FACTORS ################################################

def prime(num):
    for j in range(2, num):     #as 1 is not prime number,start range from 2 to the given number
        while (num % j == 0):   #if value of num%j is zero then it
                                # is one of the prime factor. Division of number and first prime factor
                                # will give next factor
            print("prime factor:", j)
            num = num / j
    if num > 1:                    #check whether next factor is greater than 1 and if it is greater than
                                   #than 1 then it will be second prime factor
                                     #if 20 is given as input then prime factors will be 2,2,5
                                     # as 2*2*5 is equal to 20
        print("prime factor:", num)
    else:
        print()


#################################### Euclidean distance #############################

def distance(x, y):                        #take (x,y) cordinates as input and put the values
                                        #in formula : squareroot of (x*x+y*y)
    dist = pow((x * x + y * y), 0.5)
    print("Euclidean distance is: ", dist)


########################### ROOTS OF EQUATION #######################################

def qua(a, b, c):                                  #taking input of values of a,b,c and putting

    delta = (b * b) - (4 * a * c)                  #in provided formulas to calculate roots of given
                                                #quadratic equation
    # sqroot = math.sqrt(delta)
    Root1ofx = (-b + math.sqrt(delta)) / (2 * a)
    Root2ofx = (-b - math.sqrt(delta)) / (2 * a)

    print(Root1ofx, " ", Root2ofx)


################################ COUPON #############################################

def coupon(couponnumber):                      #take coupon number as input from user
    count = 0                                  #suppose it is 25. typecast it in int i.e
    num = [int(i) for i in str(couponnumber)]  #input string 25 will be int 2 and 5 in the
                                               #form of list
    print(num)                                 #count is used for number of random numbers
                                               #needed to generate distict coupons
    while (len(num) > 0):                      #generate random number between 0-9 and
        randomno = random.randint(0, 9)        #increment the count by 1. But if number
        count += 1                             #is repeated remove that number from list
        if randomno in num:                    #and decrement the count
            num.remove(randomno)
            count-=1
    print("total number of  random numbers to generate coupon: ", count)


################################### GAMBLER ##########################################

def gamblergame(stake, goal, turns):
    bets = 0
    wins = 0
    lose = 0

    for i in range(0, turns):
        amount = stake
        while (amount > 0 and amount < goal):
            bets += 1
            randomnum = random.randint(0, 1)
            if randomnum < 0.5:
                amount += 1
            else:
                amount -= 1

        if amount == goal:
            wins += 1
        else:
            lose += 1

    percentwins = 100 * (wins / turns)
    avg_bets = 1 * (bets / turns)

    print("total wins: ", wins, " out of ", turns)
    print("total lose: ", lose, " out of ", turns)
    print("% of games won ", percentwins)
    print("average bets are ", avg_bets)


######################################### 2D ARRAY ###################################
import numpy as np


def arrays(n, m):
    arr = []
    for i in range(0, n):
        arr.append([])
    for i in range(0, n):
        for j in range(0, m):
            arr[i].append(j)
            arr[i][j] = 0
    for i in range(0, n):
        for j in range(0, m):
            print("entry in row: ", i + 1, "entry in column: ", j + 1)
            arr[i][j] = int(input())
    # print(arr)
    a = np.array(arr)
    print(a)


#################################### DISTINCT TRIPLES ################################

def disttriples(a,n):

    count = 0
    for i in range(0, n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if (a[i] + a[j] +a[k] == 0):
                    print("triplets are",a[i], " ",a[j], " ",a[k])
                    count+=1
    print(count,"number of triplets")

################################## WIND CHILL #######################################

def win(t,v):
    if (t < 120 and v < 50 and v > 3):
        w = 35.74 + 0.6215 * t + (0.4275 * t - 35.75) * math.pow(v, 0.16)
        print("wind chill: ",w)

    else:
        print("condition not statisfied")