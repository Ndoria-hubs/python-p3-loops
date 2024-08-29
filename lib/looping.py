#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    count = 0
    while count < 10:
        count += 1
        print(count)
        if count == 10:
            print("Happy New Year!")

def square_integers(int_list):
    # code goes here!
    squarelist = []
    for num in int_list:
        newnum = num ** 2
        squarelist.append(newnum)
    return squarelist
    

def fizzbuzz():
    # code goes here!
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)
