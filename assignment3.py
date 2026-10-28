#Q1 Print numbers from 1 to 50.
def num(n):
    for i in range(1, n+1):
        print(i)
num(50) 

#Q2 Print numbers from 50 to 1.
def num50to1(ch):
    while ch>1:
        ch -= 1
        print(ch)    
num50to1(50)        

#Q3 Print all even numbers from 1 to 100.
def even(num):
    for i in range(num+1):
        
        if i %2 == 0  :
            print(i)
    print("even number is print")            

even(100)  

# #Q4 Print all odd numbers from 1 to 100
def oddnum():
 for i in range(1, 101):
    if i %2 !=0:
        print(i)
oddnum()

#Q5 Print all numbers that are divisible by 5 from 1 to 100.
def dvisibleby5(n):
    for i in range(1,n + 1 ):
        if i %5 == 0:
            print(i)
    print("These number is divisible by 5") 
dvisibleby5(100)  

#Q6 Print the sum of numbers from 1 to 50.
def addition(n):
    total= 0
    for i in range(1, n+1):
        total += i
    print(total)
addition(50)               

#Q7 Print the sum of all even numbers from 1 to 20.
def evenNaddi(n):
    total = 0
    for i in range(1, n+1):
        if i %2 == 0:
            total += i
    print(total)
        
evenNaddi(20)

#Q8 Print the sum of all odd numbers from 1 to 20.
def oddaddition(n):
    total = 0
    for i in range(1, n + 1):
        if i% 2 !=0:
            total += i
    print(total)  

oddaddition(20)    

#Q9 Print the first 20 natural numbers.
def natual(n):
    for i in range(1, n+1):
        print(i)
natual(20)        

#Q10 Print the multiplication table of a number entered by the user.
def table():
    num = int(input("Enter a number: "))
    for i in range(1, 11):
        print(f"{num} x {i} = {num*i}")
table()        

#Q11 Count how many numbers are there from 1 to N.
def count(n):
    count_no = 0
    for i in range(1, n + 1):
        count_no += 1
    return count_no
print(count(10))       

#Q12 Print the square of numbers from 1 to 10.
def square():
   for i in range(1, 11):
      print(f"{i} square is {i*i}")
square()

#Q13 Print the cube of numbers from 1 to 10.
def cube(n):
   for i in range(1,n+1):
      print(f"{i} Cube is {i*i*i}")
cube(10)   

#Q14 Print numbers from 100 to 1, decreasing by 5 each time.
def decreasing(n):
   for i in range(100, n, -5):
      print(i)
decreasing(1)

#Q15 Print all numbers between 1 and 100 that are divisible by 3 and 4.
def dvisible(n):
   for i in range(1, n+1):
      if i % 3 == 0 and i % 4 == 0:
         print(i)
   print("This number is divisible by 3 and 4")  
dvisible(100)         

#Q16 Print the first 10 multiples of a given number.
def multiplies(n):
   for i in range(1, 11):
      print(i * n)
a = int(input("Enter the value : ") )        
multiplies(a) 

#Q17 Print all numbers between 1 and N that are divisible by 2.
def divisiblebytwo(n):
    for i in range(1, n+1):
        if i % 2 == 0:
            print(i)
        
    print("This number is divisble by 2")
divisiblebytwo(50)

#Q18 Print numbers from 1 to N, skipping numbers divisible by 3.
def skip(N):
   for i in range(1, N+1):
      if i % 3 == 0:
         continue
      print(i)
skip(50)      

#Q19 Print numbers from 1 to N and stop when the number reaches 20.
def reaches(n):
   for i in range(1, n+1):
      print(i)
      if i == 20:
         break
reaches(30) 

#Q20 Print the following pattern:
def pattern(n):
   for i in range(1, n+1):
      print(str(i) * i)
pattern(5)      