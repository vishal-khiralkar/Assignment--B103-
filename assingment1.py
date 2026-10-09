# Q1.Check if a number is positive, negative, or zero.
# num = int(input("enter your number: ")) 

# if(num >0):
#     print("number is positive")

# elif(num < 0):
#     print("number is negative")

# else:
#     print("value is  zero")


#Q2.Check whether a number is even or odd.
# num = int(input("Enter a number: ")) 

# if(num % 2 == 0):
#     print("number is even: ", num)

# else:
#     print("number is odd: ",num)   
 

#Q3.Find the greater of two numbers.
# num1= int(input("enter your number1: ")) 

# num2= int(input("enter your number2: "))

# if(num1 > num2):
#     print("number one is greater than n2")
# else:
#     print("number two is greater than n2")

# #Q4.Find the greatest of three numbers.
# num1 = int(input("Enter number_1: "))
# num2 = int(input("Enter number_2: "))
# num3 = int(input("Enter number_3: "))

# if(num1 > num2):
#     if(num1 > num3):
#         print("number_1 is greatest number: ", num1)

#     else:
#         print("number_3 is greatest number: ", num3) 

# else:
#     if(num2 > num3):
#         print("number_2 is greatest :", num2)   

#     else:
#         print("number_3 is greatest :", num3)      



# #Q5.Check if a person is eligible to vote (age ≥ 18).
# age = int(input("Enter your age: "))

# if(age >= 18):
#     print("you are eligible for voting...")

# else:
#     print("you are not eligible for voting...")    



# #Q6.Check whether a year is a leap year.
# year = int(input("Enter the year: "))

# if(year %4 == 0 ):
#     print("Leap year :" , year)

# else:
#     print(year, "is not leap year : ")



# #Q7.Check if a character is a vowel or consonant.
# ch = input("enter a letter: ").lower()

# if(ch == "a" or ch == "e" or ch == "i" or ch == "o" or ch == "u"):
#     print("letter" ,ch," is  vowel")
# else: 
#     print("letter",ch, "is consonant")    



# # Q8.Check whether a number is divisible by 5 and 11.
# num = int(input("Enter a number : "))

# if(num %5 == 0 and num %11 == 0):
#     print("number is divisible by 5 and 11")

# else:
#     print("number is not divisible by 5 and 11")    


#Q10.Assign grades based on marks: (1. 90-100 grade-A, 2.80–89: grad-B, 3.70–79: grade-C, 4.60–69: grade-D, 5.Below 60: F)
# marks = float(input("Enter your marks: "))

# if(marks >= 90 and marks <= 100):
#     print("Grade-A")

# elif(marks >= 80 and marks <= 89 ):
#     print("Grade-B")

# elif(marks >= 70 and marks <= 79):
#     print("Grade-C")

# elif(marks >=60 and marks <= 69):
#     print("Grade-D")  
    
# elif(marks < 60 and marks >= 40):
#     print("Grade-F")

# elif(marks > 100):
#     print("invalid marks")

# else:
#     print("Fail")

#Q11.Check if a character is uppercase or lowercase.
# ch = input("Enter a character : ")

# if(ch.isupper()):
#     print("Uppercase")

# elif(ch.islower()):
#     print("Lowercase") 

# else:
#     print("Invalid")      


# Q12.Find whether the entered alphabet is a vowel using if-elif.
# ch = input("Enter a letter : ").lower()

# if(ch == 'a'):
#     print(ch, "is a vowel")

# elif(ch == 'e'):
#     print(ch, " is a vowel")

# elif(ch == 'i'):
#     print(ch, " is a vowel")

# elif(ch == 'o'):
#     print(ch, "is a vowel")

# elif(ch == 'u'):
#     print(ch, "is a vowel")

# else:
#     print(ch, "is a consonant")            


a = float(input("Enter a value : "))
operator =input("Enter operator( +, -, *, /) : ")
b =float(input("Enter a value : "))

if(operator == "+"):
    print("Addition is : ", a+b)

elif(operator == "-"):
    print("Subtraction is : ", a-b)

elif(operator == "*"):
    print("Mulitiplication is : ", a*b) 

elif(operator == "/"):
    if(b!=0) :
        print("Division is : ", a/b)      

    else:
        print("Cannot divide by zero")

else:
    print("Invalid")
