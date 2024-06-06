#!/usr/bin/env python3

def happy_new_year():
    counter = 10
    while counter > 0:
        print(counter)
        counter -= 1
    print("Happy New Year!")
    
happy_new_year()


def square_integers(int_list):
    return [num**2 for num in int_list]

input_numbers = [4, 7, 14, 34, 78]
squared_result = square_integers(input_numbers)
print(squared_result)


def fizzbuzz():
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)

fizzbuzz()