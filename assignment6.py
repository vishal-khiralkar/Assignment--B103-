#Q1. Write a Python program to reverse a number without converting it into a string.
# n = 12345
# rev = 0

# while n > 0:
#     digit = n % 10
#     rev = rev * 10 + digit
#     n = n // 10

# print("Reverse:", rev)

#Q2. Write a program to check whether a number is a palindrome.
# n = 121
# temp = n
# rev = 0

# while n > 0:
#     digit = n % 10
#     rev = rev * 10 + digit
#     n = n // 10

# if temp == rev:
#     print("Palindrome")
# else:
#     print("Not Palindrome")

#Q3. Write a program to check whether a number is an Armstrong number.
# n = 153
# temp = n
# total = 0
# power = len(str(n))

# while n > 0:
#     digit = n % 10
#     total = total + digit ** power
#     n = n // 10

# if temp == total:
#     print("Armstrong Number")
# else:
#     print("Not Armstrong Number")

#Q4  Write a program to find the factorial of a number using a loop.
# n = 5
# fact = 1

# for i in range(1, n + 1):
#     fact = fact * i

# print("Factorial:", fact)

#Q5. Write a program to generate the Fibonacci series up to N terms.
# n = 7
# a = 0
# b = 1

# for i in range(n):
#     print(a, end=" ")
#     a, b = b, a + b

#Q6. Write a program to check whether a number is prime.
# n = 7
# count = 0

# for i in range(1, n + 1):
#     if n % i == 0:
#         count += 1

# if count == 2:
#     print("Prime Number")
# else:
#     print("Not Prime")

#Q7. Write a program to print all prime numbers between 1 and 100.
# for n in range(2, 101):
#     count = 0

#     for i in range(1, n + 1):
#         if n % i == 0:
#             count += 1

#     if count == 2:
#         print(n, end=" ")

#Q8. Write a program to find the GCD and LCM of two numbers.
# a = 12
# b = 18

# x = a
# y = b

# while y != 0:
#     x, y = y, x % y

# gcd = x
# lcm = (a * b) // gcd

# print("GCD:", gcd)
# print("LCM:", lcm)

#Q9. Write a program to reverse a string without using slicing.
# s = "Python"
# rev = ""

# for i in s:
#     rev = i + rev

# print("Reverse:", rev)

#Q10. Write a program to check whether a string is a palindrome.
# s = "madam"
# rev = ""

# for i in s:
#     rev = i + rev

# if s == rev:
#     print("Palindrome")
# else:
#     print("Not Palindrome")

#Q11. Write a program to count vowels, consonants, digits and special characters in a string.
# s = "Hello123@"

# vowels = 0
# consonants = 0
# digits = 0
# special = 0

# for i in s:
#     if i.isalpha():
#         if i.lower() in "aeiou":
#             vowels += 1
#         else:
#             consonants += 1
#     elif i.isdigit():
#         digits += 1
#     else:
#         special += 1

# print("Vowels:", vowels)
# print("Consonants:", consonants)
# print("Digits:", digits)
# print("Special Characters:", special)

#Q12. Write a program to find the frequency of each character in a string.
# s = "hello"
# freq = {}

# for i in s:
#     if i in freq:
#         freq[i] += 1
#     else:
#         freq[i] = 1

# print(freq)

#Q13. Write a program to find the first non-repeating character in a string.
# s = "aabbcde"

# for i in s:
#     if s.count(i) == 1:
#         print("First non-repeating:", i)
#         break

#Q14. Write a program to remove duplicate characters from a string.
# s = "programming"
# result = ""

# for i in s:
#     if i not in result:
#         result += i

# print(result)

#Q15. Write a program to check whether two strings are anagrams.
# s1 = "listen"
# s2 = "silent"

# if sorted(s1) == sorted(s2):
#     print("Anagram")
# else:
#     print("Not Anagram")

#Q16. Write a program to find the longest word in a sentence.
# s = "Python is a programming language"
# words = s.split()

# longest = ""

# for i in words:
#     if len(i) > len(longest):
#         longest = i

# print("Longest word:", longest)

#Q17. Find the second-largest element in a list without using sort().
# a = [10, 20, 40, 30, 50]

# largest = second = float('-inf')

# for i in a:
#     if i > largest:
#         second = largest
#         largest = i
#     elif largest > i > second:
#         second = i

# print("Second Largest:", second)

#Q18. Remove duplicate elements from a list without using set().
# a = [1, 2, 2, 3, 4, 4, 5]
# result = []

# for i in a:
#     if i not in result:
#         result.append(i)

# print(result)

#Q19. Find the common elements between two lists.
# a = [1, 2, 3, 4]
# b = [3, 4, 5, 6]

# result = []

# for i in a:
#     if i in b and i not in result:
#         result.append(i)

# print("Common Elements:", result)

#Q20. Move all zeros to the end of a list without changing the order of other elements.
# a = [0, 1, 0, 3, 12]
# result = []

# for i in a:
#     if i != 0:
#         result.append(i)

# for i in a:
#     if i == 0:
#         result.append(i)

# print(result)

#Q21. Find the missing number in a list containing numbers from 1 to N.

# a = [1, 2, 3, 5, 6]
# n = 6

# total = n * (n + 1) // 2
# missing = total - sum(a)

# print("Missing Number:", missing)

#Q22. Find the maximum difference between two elements where the larger element appears after the smaller element.
# a = [2, 3, 10, 6, 4, 8, 1]

# min_num = a[0]
# max_diff = 0

# for i in a:
#     if i - min_num > max_diff:
#         max_diff = i - min_num

#     if i < min_num:
#         min_num = i

# print("Maximum Difference:", max_diff)

#Q23. Rotate a list to the right by K positions.
# a = [1, 2, 3, 4, 5]
# k = 2

# k = k % len(a)
# result = a[-k:] + a[:-k]

# print(result)

#Q24. Find all pairs in a list whose sum equals a given target.
# a = [2, 4, 3, 5, 7, 8]
# target = 7

# for i in range(len(a)):
#     for j in range(i + 1, len(a)):
#         if a[i] + a[j] == target:
#             print(a[i], a[j])

#Q25. Write a program to count the frequency of each word in a paragraph.
# s = "python is easy python is powerful"

# words = s.split()
# freq = {}

# for i in words:
#     if i in freq:
#         freq[i] += 1
#     else:
#         freq[i] = 1

# print(freq)

#Q26. Write a program to merge two dictionaries. If a key exists in both, add their values.
# d1 = {'a': 10, 'b': 20}
# d2 = {'b': 30, 'c': 40}

# result = d1.copy()

# for key, value in d2.items():
#     if key in result:
#         result[key] += value
#     else:
#         result[key] = value

# print(result)

#Q27. Write a program to sort a dictionary based on its values.
# d = {'a': 40, 'b': 10, 'c': 30, 'd': 20}

# result = dict(sorted(d.items(), key=lambda x: x[1]))

# print(result)

#Q28. Given a list of student dictionaries containing name and marks, find the student with the highest marks.
# students = [
#     {'name': 'Rahul', 'marks': 80},
#     {'name': 'Amit', 'marks': 90},
#     {'name': 'Sneha', 'marks': 85}
# ]

# highest = students[0]

# for i in students:
#     if i['marks'] > highest['marks']:
#         highest = i

# print("Name:", highest['name'])
# print("Marks:", highest['marks'])

#Q29. Group words from a list based on their first character using a dictionary.
# words = ['apple', 'ant', 'ball', 'bat', 'cat']

# result = {}

# for i in words:
#     key = i[0]

#     if key in result:
#         result[key].append(i)
#     else:
#         result[key] = [i]

# print(result)

#Q30. Convert two lists into a dictionary, where the first list contains keys and the second contains values.
# keys = ['name', 'age', 'city']
# values = ['Rahul', 21, 'Pune']

# result = dict(zip(keys, values))

# print(result)

#Q31. Write a recursive function to calculate the factorial of a number.
# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)

# print(factorial(5))

#Q32. Write a recursive function to find the sum of digits of a number.
# def sum_digits(n):
#     if n == 0:
#         return 0
#     else:
#         return n % 10 + sum_digits(n // 10)

# print(sum_digits(1234))

#Q33. Implement your own map() function without using Python's built-in map().
# def my_map(func, lst):
#     result = []

#     for i in lst:
#         result.append(func(i))

#     return result

# def square(n):
#     return n * n

# a = [1, 2, 3, 4, 5]

# print(my_map(square, a))

# #Q34. Implement a function that accepts a list and returns a new list containing only even numbers.
# def even_numbers(lst):
#     result = []

#     for i in lst:
#         if i % 2 == 0:
#             result.append(i)

#     return result

# a = [1, 2, 3, 4, 5, 6, 7, 8]

# print(even_numbers(a))

#Q35. Write a function to flatten a nested list.
# a = [[1, 2], [3, 4], [5, 6]]
# result = []

# for i in a:
#     for j in i:
#         result.append(j)

# print(result)

#Q36. Student Management System
# Create a console-based application with the following operations:
#  Add student
#  Display all students
#  Search student by ID
#  Update student details
#  Delete student
# students = {}

# while True:
#     print("\n1. Add Student")
#     print("2. Display Students")
#     print("3. Search Student")
#     print("4. Update Student")
#     print("5. Delete Student")
#     print("6. Exit")

#     choice = int(input("Enter choice: "))

#     if choice == 1:
#         sid = input("Enter ID: ")
#         name = input("Enter Name: ")
#         marks = input("Enter Marks: ")

#         students[sid] = {
#             'name': name,
#             'marks': marks
#         }
#         print("Student Added")

#     elif choice == 2:
#         for sid, details in students.items():
#             print(sid, details)

#     elif choice == 3:
#         sid = input("Enter ID: ")

#         if sid in students:
#             print(students[sid])
#         else:
#             print("Student Not Found")

#     elif choice == 4:
#         sid = input("Enter ID: ")

#         if sid in students:
#             students[sid]['name'] = input("New Name: ")
#             students[sid]['marks'] = input("New Marks: ")
#             print("Student Updated")
#         else:
#             print("Student Not Found")

#     elif choice == 5:
#         sid = input("Enter ID: ")

#         if sid in students:
#             del students[sid]
#             print("Student Deleted")
#         else:
#             print("Student Not Found")

#     elif choice == 6:
#         break

#     else:
#         print("Invalid Choice")

#Q37 Bank Account Management
# Create a bank account program with:
#  Create account
#  Deposit money
#  Withdraw money
#  Check balance
#  Display account details
# balance = 0
# name = ""

# while True:
#     print("\n1. Create Account")
#     print("2. Deposit")
#     print("3. Withdraw")
#     print("4. Check Balance")
#     print("5. Display Details")
#     print("6. Exit")

#     choice = int(input("Enter choice: "))

#     if choice == 1:
#         name = input("Enter Name: ")
#         print("Account Created")

#     elif choice == 2:
#         amount = float(input("Enter Amount: "))
#         if name:
#             if amount > 0:
#                 balance += amount
#                 print("Money Deposited")
#             else:
#                 print("Invalid Amount")
#         else:
#             print("Create Account First")

#     elif choice == 3:
#         amount = float(input("Enter Amount: "))

#         if amount > 0 and amount <= balance:
#             balance -= amount
#             print("Money Withdrawn")
#         else:
#             print("Insufficient Balance or Invalid Amount")

#     elif choice == 4:
#         print("Balance:", balance)

#     elif choice == 5:
#         print("Account Holder:", name)
#         print("Balance:", balance)

#     elif choice == 6:
#         break

#     else:
#         print("Invalid Choice")

#Q38. Employee Salary Management
# Create a program to:
#  Add employee details
#  Calculate gross salary
#  Calculate deductions
#  Calculate net salary
#  Display employee salary details
# name = input("Enter Employee Name: ")
# basic = float(input("Enter Basic Salary: "))

# hra = basic * 0.20
# da = basic * 0.10

# gross = basic + hra + da

# deduction = gross * 0.05

# net = gross - deduction

# print("Employee Name:", name)
# print("Basic Salary:", basic)
# print("HRA:", hra)
# print("DA:", da)
# print("Gross Salary:", gross)
# print("Deduction:", deduction)
# print("Net Salary:", net)

#Q39. Library Management System
# Create a program to:
#  Add books
#  Display available books
#  Issue a book
#  Return a book
#  Search books by title
# books = {}

# while True:
#     print("\n1. Add Book")
#     print("2. Display Books")
#     print("3. Issue Book")
#     print("4. Return Book")
#     print("5. Search Book")
#     print("6. Exit")

#     choice = int(input("Enter choice: "))

#     if choice == 1:
#         book_id = input("Enter Book ID: ")
#         title = input("Enter Book Title: ")

#         books[book_id] = {
#             'title': title,
#             'available': True
#         }
#         print("Book Added")

#     elif choice == 2:
#         for bid, details in books.items():
#             print(bid, details)

#     elif choice == 3:
#         bid = input("Enter Book ID: ")

#         if bid in books and books[bid]['available']:
#             books[bid]['available'] = False
#             print("Book Issued")
#         else:
#             print("Book Not Available")

#     elif choice == 4:
#         bid = input("Enter Book ID: ")

#         if bid in books and not books[bid]['available']:
#             books[bid]['available'] = True
#             print("Book Returned")
#         else:
#             print("Invalid Book ID or Book Already Available")

#     elif choice == 5:
#         title = input("Enter Book Title: ")

#         found = False

#         for bid, details in books.items():
#             if details['title'].lower() == title.lower():
#                 print(bid, details)
#                 found = True

#         if not found:
#             print("Book Not Found")

#     elif choice == 6:
#         break

#     else:
#         print("Invalid Choice")

#Q40. Task Management Application
# Create a console-based task manager with:
#  Add task
#  View all tasks
#  Update task
#  Delete task
#  Mark task as completed
#  Filter completed and pending tasks
tasks = []

while True:
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Mark Completed")
    print("6. Filter Tasks")
    print("7. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        task = input("Enter Task: ")
        tasks.append({
            'task': task,
            'status': 'Pending'
        })
        print("Task Added")

    elif choice == 2:
        for i, t in enumerate(tasks):
            print(i, t)

    elif choice == 3:
        index = int(input("Enter Task Number: "))

        if 0 <= index < len(tasks):
            tasks[index]['task'] = input("New Task: ")
            print("Task Updated")
        else:
            print("Invalid Task Number")

    elif choice == 4:
        index = int(input("Enter Task Number: "))

        if 0 <= index < len(tasks):
            tasks.pop(index)
            print("Task Deleted")
        else:
            print("Invalid Task Number")

    elif choice == 5:
        index = int(input("Enter Task Number: "))

        if 0 <= index < len(tasks):
            tasks[index]['status'] = 'Completed'
            print("Task Completed")
        else:
            print("Invalid Task Number")

    elif choice == 6:
        status = input("Enter Completed or Pending: ").title()

        for t in tasks:
            if t['status'] == status:
                print(t)

    elif choice == 7:
        break

    else:
        print("Invalid Choice")
