#Q! Find the data type of every value in a mixed list.

# def data_type(list):
#  for i in list:
#     print(i, "=", type(i))
# data_type( ["Vishal",21,87.00,"Shivansh", True]) 


#Q2 Convert a nested list into a tuple of tuples.

# def convert(student):
#  result = tuple(tuple(i) for i in student)
#  print(result)

# convert( [["Viransh",18,"Data Sceience"],["Pune",88.05,]])     

#Q3 Remove all duplicate values from a mixed list while preserving the original order.
# def mix_list(list):
#     original = []
#     for i in list:
#         if  i not in original:
#               original.append(i)
#     print(original)        
# mix_list([1,2,3,3,"hello",5,6,"hello",6])

#Q4 Check whether a number is a power of 2 using operators.
# n = 16

# if n > 0 and (n & (n - 1)) == 0:
#     print("Power of 2")
# else:
#     print("Not a power of 2")

#Q5 Swap two numbers using bitwise XOR.
# a = 10
# b = 20

# a = a ^ b
# b = a ^ b
# a = a ^ b

# print("a =", a)
# print("b =", b)

#Q6 Find whether a number is divisible by both 4 and 6 using logical operators.
# def divisible(a):
#     if a %4 == 0 and a %6 == 0:
#         print(a, "is divisible by both(4 & 6)")
#     else:
#         print("not divisible by both")    
# divisible(12) 

#Q7 Calculate the total electricity bill using different unit rates
# units = int(input("Enter electricity units: "))

# if units <= 100:
#     bill = units * 3

# elif units <= 200:
#     bill = (100 * 3) + (units - 100) * 5

# elif units <= 300:
#     bill = (100 * 3) + (100 * 5) + (units - 200) * 7

# else:
#     bill = (100 * 3) + (100 * 5) + (100 * 7) + (units - 300) * 10

# print("Total Electricity Bill:", bill)

#Q8 Check whether three sides can form a triangle
# a = int(input("Enter first side: "))
# b = int(input("Enter second side: "))
# c = int(input("Enter third side: "))

# if a + b > c and a + c > b and b + c > a:
#     print("Triangle can be formed")
# else:
#     print("Triangle cannot be formed")

#Q9 Determine the type of triangle (Equilateral, Isosceles, Scalene).
# a = int(input("Enter first side: "))
# b = int(input("Enter second side: "))
# c = int(input("Enter third side: "))

# if a + b > c and a + c > b and b + c > a:

#     if a == b == c:
#         print("Equilateral Triangle")

#     elif a == b or b == c or a == c:
#         print("Isosceles Triangle")

#     else:
#         print("Scalene Triangle")

# else:
#     print("Invalid Triangle")

#Q10 Create a simple ATM menu (Withdraw, Deposit, Balance).
# balance = 20000

# withdraw = int(input("Enter the Debited amount: "))
# balance -= withdraw
# print(withdraw, "debited successfully\navailabe balance is",balance)

# diposite = int(input("Enter the Credited amount:"))
# balance += diposite
# print(diposite,"in your account successfully...\navailable balance is",balance)


#Q11 Calculate income tax based on different tax slabs.
# income = int(input("enter your income: "))
# if income <= 25000:
#     tax = 0

# elif income >= 100000:
#    tax = income * 0.5

# elif income >=500000:
#     tax = income * 0.10   

# else:
#   tax = income * 0.30

# print("Income Tax :",tax)

#Q12 Create a menu-driven calculator using if-elif.
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))

# print("1. Addition")
# print("2. Subtraction")
# print("3. Multiplication")
# print("4. Division")

# choice = int(input("Enter your choice like(1,2,3,4): "))

# if choice == 1:
#     print("Addition:", a + b)
# elif choice == 2:
#     print("Subtraction:", a - b)
# elif choice == 3:
#     print("Multiplication:", a * b)
# elif choice == 4:
#     print("Division:", a / b)
# else:
#     print("Invalid choice")                 

#Q13 Print all prime numbers between 1 and n.
# n = 10
# for i in range(2, n+1):
#     count = 0 
#     for j in range(1, i+1):
#         if i % j == 0:
#             count += 1

#     if count == 2:
#         print(i)        

#Q14 Find the factorial of a number using a loop.
# n = 5
# fact = 1
# for i in range(1, n+1):
#     fact = fact * i
#     print("Factorial",fact)    

#Q15 Find the factorial of a number using a loop.
# n = 7
# a = 0
# b = 1

# for i in range(n):
#     print(a, end=" ")
#     c = a + b
#     a = b
#     b = c

#Q16. Check whether a number is an Armstrong number.
# n = 153
# temp = n
# total = 0

# while temp > 0:
#     digit = temp % 10
#     total = total + digit ** 3
#     temp = temp // 10

# if total == n:
#     print("Armstrong number")
# else:
#     print("Not Armstrong number")

#Q17 Reverse a number and check if it is a palindrome.
# no = 121
# rev = 0
# temp = no
# while no > 0:
#     rev = rev*10+no%10
#     no = no//10
#     print(rev)
# if temp == rev:
#     print("Number is palindrome")
# else:
#     print("Number is not palindrome")        

#Q19. Write a function to check if a string is a palindrome.
# def palindrome(s):
#     if s == s[::-1]:
#         print("Palindrome")
#     else:
#         print("Not Palindrome")

# palindrome("madam")

#Q20. Count vowels and consonants in a string
# def count_letters(s):
#     vowels = 0
#     consonants = 0

#     for i in s:
#         if i.isalpha():
#             if i.lower() in "aeiou":
#                 vowels += 1
#             else:
#                 consonants += 1

#     print("Vowels:", vowels)
#     print("Consonants:", consonants)

# count_letters("hello")

#Q23. Find the second-largest number in a list.
# def second_largest(my_list):
#     unique = list(set(my_list))
#     unique.sort()

#     print("Second largest:", unique[-2])

# second_largest([10, 20, 30, 40, 50])

# Q24. Merge two lists without duplicates.
# list1 = [1, 2, 3, 4]
# list2 = [3, 4, 5, 6]

# result = []

# for i in list1 + list2:
#     if i not in result:
#         result.append(i)

# print(result)

#Q25. Find the second-largest and second-smallest elements
# my_list = [10, 20, 30, 40, 50]

# my_list = list(set(my_list))
# my_list.sort()

# print("Second smallest:", my_list[1])
# print("Second largest:", my_list[-2])

#Q26. Rotate a list to the left by k positions
# my_list = [1, 2, 3, 4, 5]
# k = 2

# result = my_list[k:] + my_list[:k]

# print(result)

#.Q27 Separate even and odd numbers into two lists.
# my_list = [1, 2, 3, 4, 5, 6]

# even = []
# odd = []

# for i in my_list:
#     if i % 2 == 0:
#         even.append(i)
#     else:
#         odd.append(i)

# print("Even:", even)
# print("Odd:", odd)

#Q28. Find the common elements between two lists
# list1 = [1, 2, 3, 4, 5]
# list2 = [3, 4, 5, 6, 7]

# common = []

# for i in list1:
#     if i in list2 and i not in common:
#         common.append(i)

# print(common)

#Q29. Count the frequency of each element in a tuple
# my_tuple = (1, 2, 2, 3, 3, 3, 4)

# for i in set(my_tuple):
#     print(i, ":", my_tuple.count(i))

#Q30. Find the union, intersection, and difference of two sets.
# a = {1, 2, 3, 4}
# b = {3, 4, 5, 6}

# print("Union:", a.union(b))
# print("Intersection:", a.intersection(b))
# print("Difference:", a.difference(b))

#Q31. Check whether one set is a subset of another.
# a = {1, 2}
# b = {1, 2, 3, 4}

# if a.issubset(b):
#     print("A is a subset of B")
# else:
#     print("A is not a subset of B")

#Q32. Count the frequency of words in a sentence.
# sentence = "python is easy python is powerful"

# words = sentence.split()
# count = {}

# for i in words:
#     if i in count:
#         count[i] += 1
#     else:
#         count[i] = 1

# print(count)

#Q33. Create a dictionary from two lists (keys and values).
# keys = ["name", "age", "city"]
# values = ["Rahul", 22, "Pune"]

# my_dict = dict(zip(keys, values))

# print(my_dict)

#Q34. Sort a dictionary by its values.
# my_dict = {"A": 50, "B": 20, "C": 40, "D": 10}

# result = dict(sorted(my_dict.items(), key=lambda x: x[1]))

# print(result)

#Q35. Read a text file and count lines, words, and characters
# file = open("demo.txt","r")
# data = file.read()

# lines = data.splitlines()
# words = data.split()
# characters = len(data)

# print("Lines:", len(lines))
# print("Words:", len(words))
# print("Characters:", characters)

# file.close()

#Q36. Copy only the even-numbered lines from one file to another.
# file = open("input.txt", "r")
# data = file.readlines()
# file.close()

# output = open("output.txt", "w")

# for i in range(len(data)):
#     if (i + 1) % 2 == 0:
#         output.write(data[i])

# output.close()

# print("Even lines copied successfully")

#Q37. Handle invalid integer input using try-except.
# try:
#     n = int(input("Enter a number: "))
#     print("NUmber",n)

# except ValueError:
#     print("Invalid input! Please enter an integer")

#Q38. Handle file-not-found errors while reading a file.
# try:
#     file = open("demo.txt", "r")
#     print(file.read())
#     file.close()

# except FileNotFoundError:
#     print("File not found!")

#Q39. Create a random password generator using random and string modules.

# import random
# import string

# characters = string.ascii_letters + string.digits

# password = ""

# for i in range(8):
#     password += random.choice(characters)

# print("Password:", password)

#Q40. Use datetime module to calculate the number of days between two dates.
# from datetime import date

# date1 = date(2026, 1, 1)
# date2 = date(2026, 1, 10)

# difference = date2 - date1

# print("Total days:", difference.days)