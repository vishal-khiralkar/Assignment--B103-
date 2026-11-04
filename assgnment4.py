# Q1 Write a Python program to check whether a number is even or odd.
# def evenOdd(x):
#     if x %2 == 0:
#         print(x,"is even number")
#     else:
#         print(x,"is odd number")    

# num = int(input("enter your number: "))
# evenOdd(num)

#Q2 Write a program to find the largest of three numbers.
# def largest(x, y, z):
#     if x >= y and x >= z:
#         print("x is largest number")

#     elif y >= x and y >= z:
#         print("y is largest number")

#     else:
#         print("z is largest number")    

# largest(80,70,90)        

#Q3 Write a program to check whether a given number is prime.
# def prime(n):
#     if n <= 1:
#         print("not a prime number")
#     else:
#         for i in range(2, n) :
#             if n % i ==  0:
#                 print("NOt Prime")
#                 break
#         else:
#          print("Prime")       
# prime(7)    

#Q4 Write a program to print the Fibonacci series up to n terms.
# def fibonacci(n):
#     a = 0
#     b = 1
#     for i in range(n):
#         print(a)
#         c = a + b
#         a = b
#         b = c
# fibonacci(10)        

#Q5 Write a program to find the factorial of a number using a loop.
# def factorial(n):
#  fact = 1
#  for i in range(1, n+1):
#      fact = fact * i
#      print(fact)
# factorial(5)

#Q6 Write a program to reverse a string without using [::-1].
# def revString(name):
#     rev = ""
#     for i in range(len(name)-1,-1,-1): 
#         rev = rev +name[i]
#     print(rev) 
# revString("vishal")        

#Q7 Write a program to check whether a string is a palindrome
# def palindrome(s):
#     rev = ""
#     for i in range(len(s)-1,-1,-1):
#         rev = rev + s[i]

#     if s == rev:
#         print("Palindrome")
#     else:
#         print("Not Palindrome")        
   
# palindrome("mom")       

# Q8 Write a program to count the number of vowels and consonants in a string.
# def count(s):
#     vowels = 0
#     consonants = 0

#     for i in s:
#         if i.lower() in "aeiou":
#             vowels += 1
#         elif i.isalpha():
#             consonants += 1

#     print("Vowels:", vowels)
#     print("Consonants:", consonants)

# count("Python Programming")

#Q9 Write a program to find the sum of all elements in a list.
# def addition(list):
#     total = 0
#     for i in list:
#         total += i
#     print("Sum", total)
# addition([10,20,30,40])        

#Q10 Write a program to find the largest and smallest element in a list without using max() or min().
# def find(list):
#     largest = list[0]
#     smallest = list[0]

#     for i in list:
#         if i > largest:
#             largest = i

#         if i < smallest:
#             smallest = i

#     print("Largest:", largest)
#     print("Smallest:", smallest)

# find([10, 50, 5, 80, 20])

#Q11 Write a program to remove duplicate elements from a list.
# def remove_duplicate(lst):
#     new = []

#     for i in lst:
#         if i not in new:
#             new.append(i)

#     print(new)

# remove_duplicate([1, 2, 2, 3, 4, 4, 5])

#Q12 Write a program to count how many times each element appears in a list using a dictionary.
# def frequency(lst):
#     count = {}

#     for i in lst:
#         if i in count:
#             count[i] += 1
#         else:
#             count[i] = 1

#     print(count)

# frequency([1, 2, 2, 3, 3, 3, 4])

#Q13 Write a program to find the second-largest number in a list.
# def second_largest(lst):
#     largest = lst[0]
#     second = None

#     for i in lst:
#         if i > largest:
#             second = largest
#             largest = i
#         elif i != largest and (second is None or i > second):
#             second = i

#     print("Second largest:", second)

# second_largest([10, 50, 30, 80, 20])

# #q14 Write a program to sort a list without using sort() or sorted().
# def sorting(lst):
#     for i in range(len(lst)):
#         for j in range(0, len(lst)-1):
#             if lst[j] > lst[j+1]:
#                 lst[j], lst[j+1] = lst[j+1], lst[j]

#     print(lst)

# sorting([5, 2, 8, 1, 3])

#q15 Write a function that accepts a list of numbers and returns a list containing only the even numbers.
# def return_even(list):
#     even = []
#     for i in list:
#         if i %2 == 0:
#             even.append(i)
#     print(even)        
# return_even([1,2,3,4,6,8,9,12,10])    

#Q16 Write a program to find the frequency of each character in a string.
# def frequency(s):
#     count = {}

#     for i in s:
#         if i in count:
#             count[i] += 1
#         else:
#             count[i] = 1

#     print(count)

# frequency("hello") 
    
#Q17 Write a program to check whether two strings are anagrams of each other.
# def anagram(s1, s2):
#     if len(s1) != len(s2):
#         print("Not Anagram")
#     else:
#         if sorted(s1) == sorted(s2):
#             print("Anagram")
#         else:
#             print("Not Anagram")

# anagram("listen", "silent")

#Q18 Write a program to find all duplicate values in a list.
# def duplicate(list):
#     duplicate_value = []
#     for i in list:
#         if list.count(i) >1 and i not in duplicate_value:
#             duplicate_value.append(i)
#     print(duplicate_value)        
# duplicate([1,1,2,3,3,4,4,5,7,8,8])    

#19 Write a program that takes a sentence and finds the longest word.
# def longest_word(s):
#     words = s.split()
#     longest = words[0]

#     for i in words:
#         if len(i) > len(longest):
#             longest = i

#     print("Longest word:", longest)

# longest_word("Python programming is very interesting")

#Q20 Create a simple student marks program that:
 #accepts marks for 5 subjects,
 #calculates the total and percentage,
 #assigns a grade,and displays whether the student passed or failed
# def student():
#     total = 0

#     for i in range(1, 6):
#         marks = int(input("Enter subject marks: "))
#         total += marks

#     percentage = total / 5

#     print("Total:", total)
#     print("Percentage:", percentage)

#     if percentage >= 90:
#         print("Grade: A")
#     elif percentage >= 75:
#         print("Grade: B")
#     elif percentage >= 60:
#         print("Grade: C")
#     elif percentage >= 40:
#         print("Grade: D")
#     else:
#         print("Grade: F")

#     if percentage >= 40:
#         print("Result: Pass")
#     else:
#         print("Result: Fail")

# student()