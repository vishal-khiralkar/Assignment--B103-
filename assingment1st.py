# Q1.Check if a number is positive, negative, or zero.
num = int(input("enter your number: ")) 

if(num >0):
    print("number is positive")

elif(num < 0):
    print("number is negative")

else:
    print("value is  zero")


#Q2.Check whether a number is even or odd.
num = int(input("Enter a number: ")) 

if(num % 2 == 0):
    print("number is even: ", num)

else:
    print("number is odd: ",num)   
 

#Q3.Find the greater of two numbers.
num1= int(input("enter your number1: ")) 

num2= int(input("enter your number2: "))

if(num1 > num2):
    print("number one is greater than n2")
else:
    print("number two is greater than n2")

#Q4.Find the greatest of three numbers.
num1 = int(input("Enter number_1: "))
num2 = int(input("Enter number_2: "))
num3 = int(input("Enter number_3: "))

if(num1 > num2):
    if(num1 > num3):
        print("number_1 is greatest number: ", num1)

    else:
        print("number_3 is greatest number: ", num3) 

else:
    if(num2 > num3):
        print("number_2 is greatest :", num2)   

    else:
        print("number_3 is greatest :", num3)      



#Q5.Check if a person is eligible to vote (age ≥ 18).
age = int(input("Enter your age: "))

if(age >= 18):
    print("you are eligible for voting...")

else:
    print("you are not eligible for voting...")    



#Q6.Check whether a year is a leap year.
year = int(input("Enter the year: "))

if(year %4 == 0 ):
    print("Leap year :" , year)

else:
    print(year, "is not leap year : ")



#Q7.Check if a character is a vowel or consonant.
ch = input("enter a letter: ").lower()

if(ch == "a" or ch == "e" or ch == "i" or ch == "o" or ch == "u"):
    print("letter" ,ch," is  vowel")
else: 
    print("letter",ch, "is consonant")    



# Q8.Check whether a number is divisible by 5 and 11.
num = int(input("Enter a number : "))

if(num %5 == 0 and num %11 == 0):
    print("number is divisible by 5 and 11")

else:
    print("number is not divisible by 5 and 11")    


#Q10.Assign grades based on marks: (1. 90-100 grade-A, 2.80–89: grad-B, 3.70–79: grade-C, 4.60–69: grade-D, 5.Below 60: F)
marks = float(input("Enter your marks: "))

if(marks >= 90 and marks <= 100):
    print("Grade-A")

elif(marks >= 80 and marks <= 89 ):
    print("Grade-B")

elif(marks >= 70 and marks <= 79):
    print("Grade-C")

elif(marks >=60 and marks <= 69):
    print("Grade-D")  
    
elif(marks < 60 and marks >= 40):
    print("Grade-F")

elif(marks > 100):
    print("invalid marks")

else:
    print("Fail")

#Q11.Check if a character is uppercase or lowercase.
ch = input("Enter a character : ")

if(ch.isupper()):
    print("Uppercase")

elif(ch.islower()):
    print("Lowercase") 

else:
    print("Invalid")      


# Q12.Find whether the entered alphabet is a vowel using if-elif.
ch = input("Enter a letter : ").lower()

if(ch == 'a'):
    print(ch, "is a vowel")

elif(ch == 'e'):
    print(ch, " is a vowel")

elif(ch == 'i'):
    print(ch, " is a vowel")

elif(ch == 'o'):
    print(ch, "is a vowel")

elif(ch == 'u'):
    print(ch, "is a vowel")

else:
    print(ch, "is a consonant") 


#Q15.Find the largest among four numbers
a = int(input("Enter first number : " ))
b = int(input("Enter second number : "))
c = int(input("Enter third number : "))
d = int(input("Enter fourth number : "))

if(a>=b and a>=c and a>=d):
    print("Largest number is : ", a)

elif(b >= a and b >= c and b >= d ):
    print("Largest number is : ", b)  

elif(c >= a and c >= b and c >= d):
    print("Lagest number is : ", c)      

else:
    print("Largest number is : ", d)

#Q16.Check whether a number is a three-digit number.
num = int(input("Enter a number : "))

if(num >= 100 and num <= 900 or num <= -100 and num >= -999):
    print("it is three digit number ")

else: 
    print("it is not a three digit number")    



#Q18Calculate income tax based on income slabs.
income = float(input("Enter  your annual income :  "))

if income <= 300000:
    tax = 0
elif income <= 600000: 
    tax = income * 0.05
elif income <= 900000:
    tax = income * 0.10
else:
    tax = income * 0.20

print("Income Tax = ", tax)


#Q19.Check if a student passes (minimum 35 marks in each subject).
maths = int(input("Enter Maths mark : "))
english = int(input("Enter english mark : "))
physics = int(input("Enter physics mark : "))

if (maths >=35 and english >=35 and physics >=35 ):
    print("Student is Pass")

else:
    print("Student is Fail")    

# Q20Find whether a number is within a given range.
num = int(input("Enter a number : "))

if(num >=10 and num <=50):
    print("Number is within the range")

else:
    print("Number is not in a range")    
           

#21.Build a simple calculator using if-elif-else (+, -, *, /).
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


#Q22.Check if a year is a century leap year.
year = int(input("Enter a year : "))

if(year %100 == 0 and year %400 == 0):
    print("Century leap year")

elif(year %100 ==0):
    print("Century year but not leap year ")    

else:
    print("Not a century year")    

#Q23.Determine the season based on the month number.
month = int(input("Enter month (1-12) : "))

if month == 10 or month == 11 or month == 12 or month == 1:
    print("Winter Season")

elif month >=2 and month <=6 :
    print("Summer Season")

elif month >= 7 and month <= 9:
    print("Rainy Season")   

else:
    print("Invalid month number")    

#Q24.Find the number of days in a month.
month = int(input("Enter month (1-12) : "))

if month == 2:
    print("28 or 29 days")

elif month == 4 or month == 6 or month == 9 or month == 11:
    print("30 days")

elif month >=1 and month <= 12 :
    print("31 days")

else:
    print("Invalid month")    

#Q25 .Check whether a password meets minimum conditions (length, digits, etc.).
password = input("Enter password : ")

if len(password) >=8:
    print("Valid password")

else:
    print("Invalid password (enter 8 digit)")

#Q26.Determine ticket price based on age category.
age = int(input("Enter you age : "))

if age < 5:
    print("Ticket price: Free")

elif age <= 12:
    print("Ticket price: Rs.50") 

elif age <=59:
    print("Ticket price: Rs. 100") 

else:
    print("Ticket price: Rs 70")          


#Q27.Calculate discount based on purchase amount.
amount = float(input("Enter purchase amount : "))

if amount >= 5000:
    discount = amount * 0.20

elif amount >= 3000:
    discount = amount * 0.10

elif amount >= 1000:
    discount = amount * 0.5

else:
    discount = 0

final_amount = amount - discount  

print("Purchase amount : ", amount)
print("Discount : ", discount)
print("Final amount : ", final_amount)



#Q28.Check if a person is eligible for a driving license (age and eyesight condition).
age = int(input("Enter your age : "))
eyesight = input("Is your eyesight is normal?(yes/no): ").lower()

if(age >=18 and eyesight == "yes"):
    print("You are eligible for licence..")

elif(age < 18):
    print("You are not eligible for driving licence") 

else:
    print("You are not eligble due to eyesight")       

#Q29.Create a login system with username and password validation.
username = input("Enter your username : ")
password = input("Enter your password : ")

if(username == "vishal" and password == "vk1234"):
    print("Login Successful...!")

elif(username != "vishal" and password != "vk1234"):
    print("Invalid username and password")

elif(username != "vishal"):
    print("Invalid username")      

else:
    print("Invalid password")    

#Q30.Create a menu-driven program using if-elif-else with options like:Addition,Subtraction,Multiplication,Division,Exit
print("--Calculation Menu--")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication" )
print("4. Division")
print("5. Exit")

operator = input("Enter operator number like(1, 2, 3, 4, 5): ")



if(operator == "1"):
        a = float(input("Enter first value : "))
        b = float(input("Enter second value : "))
        print("Addition is : ",a+b)

elif(operator == "2"):
        a = float(input("Enter first value : "))
        b = float(input("Enter second value : "))
        print("Subtraction is : ", a-b)

elif(operator == "3"):
        a = float(input("Enter first value : "))
        b = float(input("Enter second value : "))
        print("Multiplication is : ", a*b)

elif(operator == "4"):
        a = float(input("Enter first value : "))
        b = float(input("Enter second value : "))
        if b!=0:
                print("Division is: ",a/b)

        else:
                print("Cannot divide by zero")                

elif(operator == "5"):
        print("Exit")

else:
        print("Invalid")        
        
