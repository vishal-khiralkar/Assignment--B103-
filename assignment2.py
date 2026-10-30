#Q1 Even or Odd Function
#Write a function is_even(n) that returns "Even" if the number is even, otherwise "Odd".

def is_even():
    num = int(input("enter a number: "))
    if num % 2 == 0:
        print(f"{num} is even number: ")

    else:
        print(num, "is odd number")    
is_even()

#Q2 Largest of Two Numbers
#Write a function largest(a, b) that returns the larger number.

def largest(a, b):
      if a >b:
        print("a is larger number")
      else:
        print("b is larger number")    

largest(20,30)  

#Q3 Print Numbers
#Write a function print_numbers(n) that prints numbers from 1 to n using a loop.

def print_numbers(n):
    for i in range(1,n+1):
        print(i)
print_numbers(20)   


#Q4 Print Numbers
#Write a function print_numbers(n) that prints numbers from 1 to n using a loop.

def sum_n(n):
    total = 0
    for i in range(1, n+1):
        total = total + i
    return total
print(sum_n(5))


#Q5 Multiplication Table
#Write a function table(n) that prints the multiplication table of n from 1 to 10.

def table(n):
    for i in range(1, 11):
        print(f"{i} x {n} = {i*n}")
table(10)  


#Q6 Count Even Numbers
#Write a function that takes a list and returns how many even numbers it contains.

def count_even(numbers):
   
    count = 0
    for i in numbers:
     if i % 2 == 0:
        count += 1
    return count
print(count_even([1,2,3,4,5,6,7,8,9,10]))    

#Q7 Find Maximum
#Without using max(), write a function that returns the largest number in a list.

def find_max(num):
    largest = num[0]    
    for i in num:
        if i>largest:
            largest = i
    return largest
print(find_max([10,25,7,40,15]))     



#Q11 FizzBuzz
# Write a function that prints numbers from 1 to 100.
# If divisible by 3, print "Fizz".
# If divisible by 5, print "Buzz".
# If divisible by both, print "FizzBuzz".

def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

fizzbuzz()

#Q12 Palindrome Checker
#Write a function that returns True if a string is a palindrome.

def palindrome(s):
    if s == s[::-1]:
        return True
    else:
        return False

print(palindrome("madam"))

#Q13Count Vowels
#Write a function that counts the vowels in a string.

def count_vowels(s):
    count = 0
    for i in s.lower():
        if i in "aeiou":
            count += 1
    return count

print(count_vowels("hello"))

#Q14 Second Largest Number
#Write a function that returns the second largest number in a list without using sort().

def second_largest(numbers):
    largest = numbers[0]
    second = numbers[0]

    for i in numbers:
        if i > largest:
            second = largest
            largest = i
        elif i > second and i < largest:
            second = i

    return second

print(second_largest([10, 20, 5, 8, 15]))


#Q15 Guessing Game
# Generate a random number between 1 and 10.
# Keep asking the user to guess until they get it right.
# Use a loop, conditionals, and functions.

def guessing_game():
    while True:
        guess = int(input("Guess a number (1-10): "))

        if guess == 4:
            print("Correct! You win.")
            break
        else:
            print("Try again!")

guessing_game()


#Q16  Write a function grade(marks) that:
# Returns "A" for marks ≥ 90
# Returns "B" for marks ≥ 80
# Returns "C" for marks ≥ 70
# Returns "D" for marks ≥ 60
# Otherwise returns "F"

def grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    elif marks >= 60:
        return "D"
    else:
        return "F"

print(grade(95))
print(grade(82))
print(grade(45))