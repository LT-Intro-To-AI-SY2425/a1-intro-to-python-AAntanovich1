# Complete your individualized AI problems here

def fizbuzz(input_num):
    if(input_num%3==0):
        if(input_num%5==0):
            return 'FizzBuzz'
        return 'Fizz'
    elif(input_num%5==0):
        return 'Buzz'
    else:
        return input_num

assert fizbuzz(1) == 1, "fizzbuzz 1 test"
assert fizbuzz(3) == "Fizz", "fizzbuzz 3 test"
assert fizbuzz(4) == 4, "fizzbuzz 4 test"
assert fizbuzz(5) == "Buzz", "fizzbuzz 5 test"
assert fizbuzz(6) == "Fizz", "fizzbuzz 6 test"
assert fizbuzz(15) == "FizzBuzz", "fizzbuzz 15 test"

# Question 1: Calculate the square of a number
def square_number():
    number = float(input("Enter a number to square: "))
    return number ** 2

# Question 2: Check if a word is a palindrome
def is_palindrome():
    word = input("Enter a word: ")
    return word == word[::-1]

# Question 3: Convert Celsius to Fahrenheit
def celsius_to_fahrenheit():
    celsius = float(input("Enter temperature in Celsius: "))
    return (celsius * 9/5) + 32

# Main program
print("1. Square a number:", square_number())
print("2. Check if a word is a palindrome:", is_palindrome())
print("3. Convert Celsius to Fahrenheit:", celsius_to_fahrenheit())
