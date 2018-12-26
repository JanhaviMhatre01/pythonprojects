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

################################## STOPWATCH #######################################
import time
def stopwatch(startvalue):
    try:
        if(startvalue==1):
            start = time.time()
            print("starting..........")

            print("hello,how are you?")

            stopvalue = int(input("enter 0 to start: "))
        else:
            raise ValueError
        if(stopvalue==0):
            print("ending........")
            end = time.time()
            print("elapsed time:  ", round((end - start),2))
        else:
            raise ValueError
    except ValueError:
        print("wrong value")

################################## TIC TAC TOE #######################################

board = [' ' for i in range(10)]

def insertletter(letter,pos):
    board[pos]=letter

def freespace(pos):
    return board[pos]==' '

def printboard(board):
    print("  |  | ")
    print(board[1] + ' ' + board[2] + ' ' + board[3] + ' ')
    print("  |  | ")
    print("---------")
    print("  |  | ")
    print( board[4] + ' ' + board[5] + ' ' + board[6] + ' ')
    print("  |  | ")
    print("---------")
    print("  |  | ")
    print(board[7] + ' ' + board[8] + ' ' + board[9] + ' ')
    print("  |  | ")

def winner(b,l):
    return (b[1]==l and b[2]==l and b[3]==l or
    b[4] == l and b[5] == l and b[6] == l or
    b[7] == l and b[8] == l and b[9] == l or
    b[1] == l and b[4] == l and b[7] == l or
    b[2] == l and b[5] == l and b[8] == l or
    b[3] == l and b[6] == l and b[9] == l or
    b[1] == l and b[5] == l and b[9] == l or
    b[3] == l and b[5] == l and b[7] == l)

def playermove():
    run = True
    while run:
        move = input("select between 1-9: ")
        try:
            move=int(move)
            if move>0 and move<10:
                if freespace(move):
                    run = False
                    insertletter('x',move)
                else:
                    print("this is occupied")

            else:
                print("invalid number")

        except:
            print("type integer")
def computermove():
    possiblemove = [x for x,letter in enumerate(board) if letter == ' ' and x!=0]
    move = 0
    for let in ['o','x']:
        for i in possiblemove:
            boardcopy = board[:]
            boardcopy[i]= let
            if winner(boardcopy,let):
                move = i
                return move

    corner = []
    for i in possiblemove:
        if i in [1,3,7,9]:
            corner.append(i)

    if len(corner)>0:
        move = selectrandom(corner)
        return move

    if 5 in possiblemove:
        move=5
        return move

    edge = []
    for i in possiblemove:
        if i in [2,4,6,8]:
            edge.append(i)

    if len(edge) > 0:
        move = selectrandom(edge)
        return move





def selectrandom(li):
    ln = len(li)
    r = random.randrange(0,ln)
    return li[r]

def fullboard(board):
    if board.count(' ')>1:
        return False
    else:
        return True

def main():
    printboard(board)
    while not(fullboard(board)):


        if not (winner(board, ('x'))):
            move = computermove()
            if move == 0:
                print("tie")
            else:
                insertletter('o',move)
                print("computer move: ",move)
            printboard(board)

        else:
            print("user won")
            break

        if not (winner(board,('o'))):
            playermove()
            printboard(board)

        else:
            print("computer won")
            break

    if fullboard(board):
        print("tie")

################################## PERMUTATION #######################################

def permutationpy(data):
    if len(data) == 0:
        return ['']
    prev_list = permutationpy(data[1:len(data)])
    next_list = []
    for i in range(0, len(prev_list)):
        for j in range(0, len(data)):
            new_str = prev_list[i][0:j] + data[0] + prev_list[i][j:len(data) - 1]
            if new_str not in next_list:
                next_list.append(new_str)
    return next_list

################################## ANAGRAM ###########################################

def anagramcheck(str1,str2):
    list_str1 = list(str1)
    list_str2 = list(str2)
    if len(list_str1)!=len(list_str2):
        print("not anagram")
    else:
        for i in range(len(list_str1)-1):
            for j in range(len(list_str1)-1):
                if(list_str1[j]>list_str1[j+1]):
                    list_str1[j+1], list_str1[j]=list_str1[j],list_str1[j+1]


        print("sorted 1: ",list_str1)
        for p in range(len(list_str2) - 1):
            for q in range(len(list_str2) - 1):
                if (list_str2[q] > list_str2[q+1]):
                    list_str2[q+1], list_str2[q] = list_str2[q], list_str2[q+1]

        print("sorted 2: ", list_str2)

        if(list_str1==list_str2):
            print("it is anagram")
        else:
            print("not anagram")




################################## PRIME NUMBERS ###########################################

def primenumbers():
    for num in range(0,1000):
        if num>1:
            for i in range(2,num):
                if (num%i)==0:
                    break
            else:
                print(num)

################################## PALINDROM ########################################
def checkcondition():
    list_prime=[]
    for num in range(0,1000):
        if num>1:
            for i in range(2,num):
                if (num%i)==0:
                    break
            else:
                list_prime.append(num)

    print(list_prime)
    #result = map(palindrom, list_prime)
    #print(list(result))
    palindrom(list_prime)
def palindrom(number):
    l=[]
    for num in number:
        num = str(num)
        rev = num[::-1]
        if num==rev:
            l.append(int(rev))
    print("palindrom number ",l)

##################################### ALGORITHMS ###################################
elapsed_time={}

def binarysearchint(list_int,key):
    s1 = time.time()
    list_int.sort()
    start = 0
    print(list_int)
    end = len(list_int)
    for i in range(start,end):
        mid = start + (end - start) // 2

        if list_int[mid] == key:
            #globals() ['index'] = mid
            print("found at ", mid, "index")
            break

        elif key > list_int[mid]:
            start = mid

        else:
            end = mid

    else:
        print("not found")
    e1=time.time()
    el1=e1-s1
    elapsed_time.update({"binary int":el1})
    #print(elapsed_time)


def binarysearchstring(list_string,key2):
    s2 = time.time()
    list_string.sort()
    start = 0
    print(list_string)

    end = len(list_string)

    for i in range(start,end):
        mid = start + (end - start) // 2

        if list_string[mid] == key2:
            print("found at ", mid)
            break

        elif (key2 > list_string[mid]):
            start = mid

        else:
            end = mid
    else:
        print("not found")
    e2 = time.time()
    el2 = e2 - s2
    elapsed_time.update({"binary string": el2})
    #print(elapsed_time)

def bubblesortint(list_int):
    s3 = time.time()
    length = len(list_int)
    for i in range(1,length-1):
        print("pass ",i)

        for j in range(0,length-1):
            if list_int[j]>list_int[j+1]:
                temp = list_int[j+1]
                list_int[j+1]=list_int[j]
                list_int[j]=temp
        print("after pass ",i," ",list_int)
    print("total pass required: ",i)
    e3 = time.time()
    el3 = e3 - s3
    elapsed_time.update({"bubble sort int": el3})



def bubblesortstring(list_string):
    s4 = time.time()
    length = len(list_string)
    for i in range(1, length - 1):
        print("pass ", i)

        for j in range(0, length - 1):
            if list_string[j] > list_string[j + 1]:
                temp = list_string[j + 1]
                list_string[j + 1] = list_string[j]
                list_string[j] = temp
        print("after pass ", i, " ", list_string)
    print("total pass required: ", i)
    e4 = time.time()
    el4 = e4 - s4
    elapsed_time.update({"bubble sort string": el4})

def insertionsortint(list_int):
    s5 = time.time()
    length = len(list_int)
    for i in range(0,length):

        for j in range(i-1,-1,-1):
            if list_int[j] > list_int[j + 1]:
                temp = list_int[j + 1]
                list_int[j + 1] = list_int[j]
                list_int[j] = temp
    print("after sort ",list_int)
    e5 = time.time()
    el5 = e5 - s5
    elapsed_time.update({"insertion sort int": el5})


def insertionsortstring(list_string):
    s6 = time.time()
    length = len(list_string)
    for i in range(0, length):

        for j in range(i - 1, -1, -1):
            if list_string[j] > list_string[j + 1]:
                temp = list_string[j + 1]
                list_string[j + 1] = list_string[j]
                list_string[j] = temp
    print("after sort ",list_string)
    e6 = time.time()
    el6 = e6 - s6
    elapsed_time.update({"insertion sort string": el6})
    sorted_elapsed = sorted(elapsed_time.items(),key=lambda x:x[1])
    #elapsed_time.sort()
    print("sorted elapsed time",sorted_elapsed)

########################################## GUESS NUMBER #############################

def guess(low,k):
    mid = low +(k-low)//2


    if (k-low)== 1:
        print("your number is ",mid)


    else:
        print("is your number less than ",mid)
        b = int(input("if yes type 0 else 1 "))
        if b==0:
            guess(low,mid)

        else:
            guess(mid,k)

################################ READ FILE ##########################################

def filesearching(list_file):
    key2 = input("enter word to be search ")
    binarysearchstring(list_file,key2)

################################### INSERTION SORT ##################################

def userstring(stringlist):
    insertionsortstring(stringlist)

################################### BUBBLE SORT #####################################
def bubblesort(listinteger):
    for p in range(len(listinteger) - 1):
        for q in range(len(listinteger) - 1):
            if (listinteger[q] > listinteger[q + 1]):
                listinteger[q + 1], listinteger[q] = listinteger[q], listinteger[q + 1]

    print("sorted : ", listinteger)


def userint(intlist):
    bubblesort(intlist)
################################### MERGE SORT ##########################################
def merge_sort(array):
    if len(array) <= 1:
        return array

    mid = int(len(array) / 2)
    l=array[:mid]
    r=array[mid:]
    print("left",l)
    print("right",r)
    left = merge_sort(l)
    print(left)
    right = merge_sort(r)
    print(right)

    return merge(left, right)


def merge(left, right):
    result = []
    leftindex = rightindex = 0

    while leftindex < len(left) and rightindex < len(right):

        if left[leftindex] < right[rightindex]:

            result.append(left[leftindex])
            leftindex += 1

        else:

            result.append(right[rightindex])
            rightindex += 1

    result.extend(left[leftindex:])
    result.extend(right[rightindex:])

    return result


################################# VENDING MACHINE ###################################
def vending(notes):
    pass

################################## TEMPERATURE CONVERSION ###########################

def ftoc(f):
    c=(f-32)*(5 / 9)     #formula for calculation

    print("temperature in Celsius: ",c)


def ctof(c):
    f=(c* (9/5)) + 32    #formula for calculation

    print("temperature in fahrenheit: ",f)

############################ SQUREROOT OF NUMBER####################################
def sqrnum(c):
    t=c
    epsilon = 1e-15
    while abs(t-c/t)>epsilon*t:
        t=(c/t+t)/2.0
    print("Square Root : ",t)

################################# MONTHLY PAYMENT###################################
def monthlypay(p,y,r):
    totalmonths=12*y
    mrate=r/(12*100)
    payment=p*mrate/1-(1+mrate)**(-totalmonths)
    print("Payment : ",payment)

############################## DAY OF WEEK #########################################
def dayweek(day,Month,year):

    month = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December",
    }

    days= {
        0: "Sunday",
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thusday",
        5: "Friday",
        6: "Saturday",
    }

    print(day, month.get(Month), year)

    year1 = year - (14 - Month) // 12
    x = year1 + year1 // 4 - year1 // 100 + year1 // 400
    month1 = Month + 12 * ((14 - Month) // 12) - 2
    date1 = (day + x + 31 * month1 // 12) % 7
    print(date1," : ",days.get(date1))
