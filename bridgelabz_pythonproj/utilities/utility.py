import random
import math
import numpy as np
import time


# REPLACE USERNAME

def username_change(username):
    sentence = "Hello <<username>>, How are you?"  # store given label in variable
    print(sentence)

    if len(username) <= 3:  # check length of string whether it is greater than 3 or equal to 3
        print("username should contain 3 letters or more")

    else:
        u = sentence.replace("<<username>>", username)  # replacing <<username>> with proper name entered by user
        print(u)


# FLIP COIN

def flips(n):
    h = 0  # initialise head and tail to 0
    t = 0

    for i in range(0, n):  # range between 0 to n
        coin_face = random.uniform(0, 1)  # store randomly generated number between 0 to 1
        if coin_face > 0.5:  # check if randomly generated number is greater than 0.5
            h += 1  # if condition is true increment heads

        else:  # otherwise increment tails
            t += 1
    print("no of heads: ", h, "out of", n)
    print("no of tails: ", t, "out of", n)
    print("percent of heads: ", (h / n) * 100)  # (h / n) * 100 calculates percentage of heads
    print("percent of heads: ", (t / n) * 100)  # (t / n) * 100 calculates percentage of heads


# LEAP YEAR

def check_leap(year):
    if len(year) != 4:  # check length of year is 4 or not
        print("invalid year..it should be of 4 digits")  # if not then print error

    else:
        year = int(year)
        if (
                year % 4 == 0 or year % 400 == 0 and year % 100 == 0):  # check whether conditions are satisfied
            # for leap year or not
            print(year, " is leap year")

        else:
            print("this is not leap year")


# POWER OF TWO

def power_two(n):
    if 0 <= n < 31:  # number should be between 0-31.otherwise it will overflows integer value
        for i in range(0, n):  # takes all the values between 0 to N
            while i <= n:  # code will execute till i = input value of N
                print("2 to the power of", i, "=", 2 ** i)  # 2**i is 2^i
                break  # breaks while loop

    else:
        print("N should be in range of 0 - 31")


# HARMONIC VALUE

def harmonic_value(n):
    value = 0  # initialise sum equal to 0
    for i in range(1, n + 1):
        value += 1 / i  # add values which are in range of 1 to N+1

    print("harmonic value is :", value)


# PRIME FACTORS

def prime(num):
    for j in range(2, num):  # as 1 is not prime number,start range from 2 to the given number
        while num % j == 0:  # if value of num%j is zero then it
            # is one of the prime factor. Division of number and first prime factor
            # will give next factor
            print("prime factor:", j)
            num = num / j
    if num > 1:  # check whether next factor is greater than 1 and if it is greater than
        # than 1 then it will be second prime factor
        # if 20 is given as input then prime factors will be 2,2,5
        # as 2*2*5 is equal to 20
        print("prime factor:", num)
    else:
        print()


# Euclidean distance

def distance(x, y):  # take (x,y) co ordinates as input and put the values

    dist = pow((x * x + y * y), 0.5)  # in formula : square root of (x*x+y*y)
    print("Euclidean distance is: ", dist)


# ROOTS OF EQUATION

def qua(a, b, c):  # taking input of values of a,b,c and putting

    delta = (b * b) - (4 * a * c)  # in provided formulas to calculate roots of given
    # quadratic equation
    # square root = math.sqrt(delta)

    first_root = (-b + math.sqrt(delta)) / (2 * a)
    second_root = (-b - math.sqrt(delta)) / (2 * a)

    print(first_root, " ", second_root)


# COUPON

def coupon(coupon_number):  # take coupon number as input from user
    count = 0  # suppose it is 25. typecast it in int i.e
    num = [int(i) for i in str(coupon_number)]  # input string 25 will be int 2 and 5 in the form of list

    print(num)  # count is used for number of random numbers
    # needed to generate distinct coupons
    while len(num) > 0:  # generate random number between 0-9 and
        random_no = random.randint(0, 9)  # increment the count by 1. But if number
        count += 1  # is repeated remove that number from list
        if random_no in num:  # and decrement the count
            num.remove(random_no)
            count -= 1
    print("total number of  random numbers to generate coupon: ", count)


# GAMBLER

def gambler_game(stake, goal, turns):
    bets = 0  # initialise bets, wins, lose to zero at first
    wins = 0
    lose = 0

    for i in range(0, turns):  # play between 0 to turns i.e. number of trials
        amount = stake  # store stake in variable to check whether amount is increasing or not
        while 0 < amount < goal:  # play till amount is zero or gambler is broken
            bets += 1  # every time increment bets by 1
            random_num = random.randint(0, 1)  # generate number between 1/0
            if random_num < 0.5:  # if number is less than 0.5 increment amount by 1
                amount += 1
            else:
                amount -= 1  # decrement by 1

        if amount == goal:  # when goal is reached increment wins
            wins += 1
        else:
            lose += 1  # increment lose if goal not reach

    percent_wins = 100 * (wins / turns)  # calculate percent of wins
    avg_bets = 1 * (bets / turns)  # average bets

    print("total wins: ", wins, " out of ", turns)
    print("total lose: ", lose, " out of ", turns)
    print("% of games won ", percent_wins)
    print("average bets are ", avg_bets)


# 2D ARRAY


def arrays(n, m):
    arr = []  # create empty array
    for i in range(0, n):  # taking range between 0 to number of rows
        arr.append([])  # append null values
    for i in range(0, n):
        for j in range(0, m):  # taking range between 0 to number of columns
            arr[i].append(j)  # for every row append respective column
            arr[i][j] = 0  # initialise array to zero
    for i in range(0, n):
        for j in range(0, m):
            print("entry in row: ", i + 1, "entry in column: ", j + 1)  # entries for column and row
            arr[i][j] = int(input())
    # print(arr)
    a = np.array(arr)  # initial output will be in single row. so to convert it in matrix form use numpy
    print(a)


# DISTINCT TRIPLES

def dist_triples(a, n):
    count = 0  # count for number of distinct triples
    for i in range(0, n - 2):  # take arr[0], arr[1], arr[2] to compare
        for j in range(i + 1, n - 1):  # i,j,k represents respective numbers to be compare
            for k in range(j + 1, n):
                if a[i] + a[j] + a[k] == 0:  # this is required condition to find distinct triples
                    print("triplets are", a[i], " ", a[j], " ", a[k])
                    count += 1  # when triples are found increment count by 1
    print(count, "number of triplets")


# WIND CHILL

def win(t, v):
    if t < 120 and 50 > v > 3:  # checking conditions for temperature and speed
        w = 35.74 + 0.6215 * t + (0.4275 * t - 35.75) * math.pow(v, 0.16)  # formula for windchill
        print("wind chill: ", w)

    else:
        print("condition not satisfied")


# STOPWATCH


def stopwatch(start_value):  # import time
    try:
        if start_value == 1:  # if user enter one
            start = time.time()  # start timer using time.time()
            print("starting..........")

            print("hello,how are you?")  # execute this

            stop_value = int(input("enter 0 to start: "))
        else:
            raise ValueError
        if stop_value == 0:
            print("ending........")
            end = time.time()  # end time using time.time()
            print("elapsed time:  ", round((end - start), 2))  # subtract start time and end time
        else:
            raise ValueError
    except ValueError:  # if user enters other than 1/0 then raise exception
        print("wrong value")


# TIC TAC TOE

board = [' ' for i in range(10)]  # initialise board with range 10 just to add extra space


def insert_letter(letter, pos):  # to add x or o at particular position
    board[pos] = letter


def free_space(pos):  # read or check empty tile
    return board[pos] == ' '


def print_board(board):  # print board of 9x9
    print("  |  | ")
    print(board[1] + ' ' + board[2] + ' ' + board[3] + ' ')  # represents tile numbers
    print("  |  | ")
    print("---------")
    print("  |  | ")
    print(board[4] + ' ' + board[5] + ' ' + board[6] + ' ')
    print("  |  | ")
    print("---------")
    print("  |  | ")
    print(board[7] + ' ' + board[8] + ' ' + board[9] + ' ')
    print("  |  | ")


def winner(b, l):  # take value from tile and store it in common variable
    return (b[1] == l and b[2] == l and b[3] == l or
            b[4] == l and b[5] == l and b[6] == l or  # if the values are equal then it is winning condition
            b[7] == l and b[8] == l and b[9] == l or
            b[1] == l and b[4] == l and b[7] == l or
            b[2] == l and b[5] == l and b[8] == l or
            b[3] == l and b[6] == l and b[9] == l or
            b[1] == l and b[5] == l and b[9] == l or
            b[3] == l and b[5] == l and b[7] == l)


def player_move():  # player move
    run = True  # while player is playing
    while run:
        move = input("select between 1-9: ")  # select between 1-9 as board have 9 tiles
        try:
            move = int(move)  # converting string value in integer
            if 0 < move < 10:
                if free_space(move):
                    run = False  # after entering move players turn will stop
                    insert_letter('x', move)  # insert x on players move
                else:
                    print("this is occupied")  # if already occupied

            else:
                print("invalid number")  # if number is not in range of 1 to 9

        except ValueError:
            print("type integer")  # if user enter string value


def computer_move():
    possible_move = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    move = 0
    for let in ['o', 'x']:  # possible letters on board
        for i in possible_move:  # possible moves can be empty or 'o'
            board_copy = board[:]  # board[:] copy the board in variable
            board_copy[i] = let
            if winner(board_copy, let):  # check winning condition
                move = i  # if move is winning move then select move
                return move

    corner = []  # create corner array which store corner tiles
    for i in possible_move:
        if i in [1, 3, 7, 9]:  # corner tiles
            corner.append(i)  # place computer move of corner tile

    if len(corner) > 0:
        move = select_random(corner)  # select random corner tile
        return move

    if 5 in possible_move:  # if winning tile is middle tile 5 then computer will go for 5
        move = 5
        return move

    edge = []  # edge array
    for i in possible_move:
        if i in [2, 4, 6, 8]:  # edge tiles
            edge.append(i)

    if len(edge) > 0:  # select non empty edge randomly
        move = select_random(edge)
        return move


def select_random(li):  # select randomly from corner array or edge array and store array in li
    ln = len(li)  # length of li
    r = random.randrange(0, ln)  # from range 1 to ln select random number for computer move
    return li[r]


def full_board(board):  # check whether all tiles are occupied
    if board.count(' ') > 1:  # if any of the tile is empty then board is not full
        return False
    else:
        return True


def main():  # main code to execute tic tac toe
    print_board(board)  # print the board
    while not (full_board(board)):  # when board is not full

        if not (winner(board, ('x'))):  # if user is not winner then computer will play
            move = computer_move()
            if move == 0:  # if no moves left then print  tie game
                print("tie")
            else:
                insert_letter('o', move)  # if not then insert computer move
                print("computer move: ", move)
            print_board(board)  # print updated board

        else:
            print("user won")
            break

        if not (winner(board, ('o'))):
            player_move()  # player move
            print_board(board)  # print updated board after player move

        else:
            print("computer won")
            break

    if full_board(board):  # if board is full and no winning condition is satisfied
        print("tie")  # then print tie


# PERMUTATION

def permutation_py(data):
    if len(data) == 0:  # if length of string is 0 then return empty list
        return ['']
    prev_list = permutation_py(data[1:len(data)])  # recursive function to store list in new list except 0th element
    next_list = []  # create empty list
    for i in range(0, len(prev_list)):  # read new list and old list
        for j in range(0, len(data)):
            new_str = prev_list[i][0:j] + data[0] + prev_list[i][j:len(data) - 1]  # take one string and attach
            if new_str not in next_list:  # remaining strings
                next_list.append(new_str)  # if new generated strings are not in new list then append them
    return next_list


# ANAGRAM

def anagram_check(str1, str2):
    list_str1 = list(str1)  # convert string in list format
    list_str2 = list(str2)
    if len(list_str1) != len(list_str2):  # if length is not equal then is is not anagram
        print("not anagram")
    else:  # if length is equal
        for i in range(len(list_str1) - 1):
            for j in range(len(list_str1) - 1):
                if list_str1[j] > list_str1[j + 1]:  # sort the elements in list
                    list_str1[j + 1], list_str1[j] = list_str1[j], list_str1[j + 1]  # swap

        print("sorted 1: ", list_str1)

        for p in range(len(list_str2) - 1):
            for q in range(len(list_str2) - 1):
                if list_str2[q] > list_str2[q + 1]:  # sorting
                    list_str2[q + 1], list_str2[q] = list_str2[q], list_str2[q + 1]  # swap

        print("sorted 2: ", list_str2)

        if list_str1 == list_str2:  # if both the sorted list are equal then it's anagram
            print("it is anagram")
        else:
            print("not anagram")


# PRIME NUMBERS

def prime_numbers():
    for num in range(0, 1000):  # take range of 0-1000 numbers
        if num > 1:  # number should be greater than 1 as 1 is not prime and number should be non negative
            for i in range(2, num):  # range between 2 to given number as 2 is prime number
                if (num % i) == 0:  # if given number mod number in range is 0 then it is prime
                    break
            else:
                print(num)


# PALINDROME

def check_condition():  # taking prime numbers between 0-1000
    list_prime = []
    for num in range(0, 1000):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                list_prime.append(num)

    print(list_prime)

    palindrome(list_prime)


def palindrome(number):  # every prime number which is palindrome is always anagram
    p = []  # create list
    for num in number:
        num = str(num)  # convert int to string
        rev = num[::-1]  # reverse string
        if num == rev:  # if original number is equal to reverse string then it is palindrome
            p.append(int(rev))  # append number
    print("palindrome number ", p)


# ALGORITHMS
elapsed_time = {}    # create a dictionary for storing elapsed time


def binarysearchint(list_int, key):
    s1 = time.time()           # store starting time
    list_int.sort()            # sort list
    start = 0                   # initial position
    print(list_int)
    end = len(list_int)          # length of list will be the end
    for i in range(start, end):   # execute till start to end
        mid = start + (end - start) // 2       # calculate mid

        if list_int[mid] == key:         # if mid is element to be search then print found
            # globals() ['index'] = mid
            print("found at ", mid, "index")
            break

        elif key > list_int[mid]:    # if element to be search is greater than mid then mid is new start
            start = mid

        else:
            end = mid         # if element to be search is less than mid then mid is new end

    else:
        print("not found")
    e1 = time.time()            # record end time
    el1 = e1 - s1             # elapsed time
    elapsed_time.update({"binary int": el1})  # adding to dictionary


def binarysearchstring(list_string, key2):
    s2 = time.time()
    list_string.sort()
    start = 0
    print(list_string)

    end = len(list_string)

    for i in range(start, end):
        mid = start + (end - start) // 2

        if list_string[mid] == key2:
            print("found at ", mid)
            break

        elif key2 > list_string[mid]:
            start = mid

        else:
            end = mid
    else:
        print("not found")
    e2 = time.time()
    el2 = e2 - s2
    elapsed_time.update({"binary string": el2})
    # print(elapsed_time)


def bubblesortint(list_int):
    s3 = time.time()
    length = len(list_int)
    for i in range(1, length - 1):
        print("pass ", i)

        for j in range(0, length - 1):
            if list_int[j] > list_int[j + 1]:
                temp = list_int[j + 1]
                list_int[j + 1] = list_int[j]
                list_int[j] = temp
        print("after pass ", i, " ", list_int)
    print("total pass required: ", i)
    e3 = time.time()
    el3 = e3 - s3
    elapsed_time.update({"bubble sort int": el3})


def bubblesortstring(list_string):
    s4 = time.time()
    length = len(list_string)
    i = 0
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
    for i in range(0, length):

        for j in range(i - 1, -1, -1):
            if list_int[j] > list_int[j + 1]:
                temp = list_int[j + 1]
                list_int[j + 1] = list_int[j]
                list_int[j] = temp
    print("after sort ", list_int)
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
    print("after sort ", list_string)
    e6 = time.time()
    el6 = e6 - s6
    elapsed_time.update({"insertion sort string": el6})
    sorted_elapsed = sorted(elapsed_time.items(), key=lambda x: x[1])
    # elapsed_time.sort()
    print("sorted elapsed time", sorted_elapsed)


# GUESS NUMBER

def guess(low, k):
    mid = low + (k - low) // 2

    if (k - low) == 1:
        print("your number is ", mid)

    else:
        print("is your number less than ", mid)
        b = int(input("if yes type 0 else 1 "))
        if b == 0:
            guess(low, mid)

        else:
            guess(mid, k)


# READ FILE

def filesearching(list_file):
    key2 = input("enter word to be search ")
    binarysearchstring(list_file, key2)


# INSERTION SORT

def userstring(stringlist):
    insertionsortstring(stringlist)


# BUBBLE SORT
def bubblesort(listinteger):
    for p in range(len(listinteger) - 1):
        for q in range(len(listinteger) - 1):
            if listinteger[q] > listinteger[q + 1]:
                listinteger[q + 1], listinteger[q] = listinteger[q], listinteger[q + 1]

    print("sorted : ", listinteger)


def userint(intlist):
    bubblesort(intlist)


# MERGE SORT

def merge_sort(array):
    if len(array) <= 1:
        return array

    mid = int(len(array) / 2)
    l = array[:mid]
    r = array[mid:]
    print("left", l)
    print("right", r)
    left = merge_sort(l)
    print(left)
    right = merge_sort(r)
    print(right)

    return merge(left, right)


def merge(left, right):
    result = []
    left_index = right_index = 0

    while left_index < len(left) and right_index < len(right):

        if left[left_index] < right[right_index]:

            result.append(left[left_index])
            left_index += 1

        else:

            result.append(right[right_index])
            right_index += 1

    result.extend(left[left_index:])
    result.extend(right[right_index:])

    return result


# VENDING MACHINE
notes = (1000, 500, 100, 50, 10, 5, 2, 1)  # notes in vending machine in form of tuples


def vending(amount):
    try:
        total_notes = 0

        if amount == 0:  # if amount is 0 then it will exit the loop.
            return -1  # if amount is negative then there will be RecursionError

        else:
            for i in notes:  # read the elements from notes
                if amount >= i:  # suppose the amount is 200 which is greater than 100
                    calculate_note = amount // i  # calculate note will calculate required number of notes
                    remaining = amount % i  # remaining is remaining amount for which notes to be search
                    amount = remaining
                    total_notes += calculate_note
                    # add calculate notes to total notes to get total notes required to achieve amount
                    print(calculate_note, " of ", i)

            print("total notes: ", total_notes)
        vending(amount)

    except RecursionError:
        print("RecursionError")


# TEMPERATURE CONVERSION

def f_to_c(f):
    c = (f - 32) * (5 / 9)  # formula for calculation

    print("temperature in Celsius: ", c)


def c_to_f(c):
    f = (c * (9 / 5)) + 32  # formula for calculation

    print("temperature in fahrenheit: ", f)


# SQUARE ROOT OF NUMBER
def sqr_num(c):
    t = c
    epsilon = 1e-15
    while abs(t - c / t) > epsilon * t:
        t = (c / t + t) / 2.0
    print("Square Root : ", t)


# MONTHLY PAYMENT
def monthly_pay(p, y, r):
    total_months = 12 * y
    m_rate = r / (12 * 100)
    payment = p * m_rate / 1 - (1 + m_rate) ** (-total_months)
    print("Payment : ", payment)


# DAY OF WEEK

def day_week(day, months, year):
    year = int(year)

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

    days = {
        0: "Sunday",
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
    }

    print(day, month.get(months), year)

    year1 = year - (14 - months) // 12
    x = year1 + year1 // 4 - year1 // 100 + year1 // 400
    month1 = months + 12 * ((14 - months) // 12) - 2
    date1 = (day + x + 31 * month1 // 12) % 7
    print(date1, " : ", days.get(date1))


# CONVERT TO BINARY

def convert_binary(n):
    binary_number = " "  # consider result in string format

    for x in range(8):  # number should be of 8 digit so use range 8
        r = n % 2  # divide number by 2 and store the remainder which will be one of the digit
        n = n // 2  # from output. Now division will be the next number to process
        binary_number += str(r)  # append the value of r as a string to result.

    binary_number = binary_number[::-1]  # reverse the string
    # now if there are less digits than 8 then it will append 0's at starting because of for loop condition

    # print("binary number : ", binary_number)
    return binary_number


# BINARY TO DECIMAL

def decimal_convert(m):
    b = convert_binary(m)
    print("old binary", b)

    b = str(b)
    lef = b[0:4]
    r = b[4:8]
    print("l ", lef, "r ", r)

    temp = lef
    lef = r
    r = temp
    print("l ", lef, "r ", r)
    new_number = lef + r
    print("new binary: ", new_number)
    new_decimal = int(new_number, 2)
    print("new decimal number is : ", new_decimal)
    if num_power(new_decimal):
        print("power of 2")
    else:
        print("not power of 2")


def num_power(x):
    if x == 0:
        return False
    while x != 1:
        if x % 2 != 0:
            return False
        x = x // 2

    return True





