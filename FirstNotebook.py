#!/usr/bin/env python
# coding: utf-8

# # Examples

# ## Example - 1 29-07-2020

# In[ ]:


# basic print statement
print("Hello World!")


# In[ ]:


# I am single line comment
# How to write comments in Python
# suppose there are multiple lines of text
# in python and you want to comment
# all lines in one go
# do we have any short cut ??   


# In[ ]:


# Indent is important for us
print("I am from comment section")
print("I am also from comment section")


# In[ ]:


#Multi line comments, is there any way out !
'''I am from multi line section
Me too
Me too'''


# ## Example - 2 30-07-2020

# In[ ]:


# how to use variable in python, lets talk about addition of two nums
'''
int var1, var2, summ;
var1=100;
var2=200;
summ=var1 + var2;
printf("sum is %d", summ)
'''

var1 = 100
var2 = 200
summ = 0
summ= var1 + var2
#print("Sum is" + summ) this will generate error because sum is of type string and summ is of type int
# op1
print("Sum is", summ)
#op2
print("Sum is", str(summ))


# In[ ]:


# can we check what is the type of variable
var1=100
var2="200"
var3=100.5
var4=True
var5=["a","b","c"]
var6=("a","b","c")
var7={"a","b","c"}
var8={"name": "python",
      "spec": "PL"}

print(type(var1))
print(type(var2))
print(type(var3))
print(type(var4))
print(type(var5))
print(type(var6))
print(type(var7))
print(type(var8))


# In[ ]:


# how to take multiple variables at one time
# var1=100
# var2=100
# var3=100

var1=var2=var3=100  # short notation - 1
print(var1) #100
print(var2) #100
print(var3) #100
print("========")
var1=100
var2=200
var3=300

var1, var2, var3= 100, 200, 300 #shortnotation-2
print(var1) #100
print(var2) #200
print(var3) #300


# ## Example - 3 03-08-2020

# In[ ]:


# how to change the type of data or how to set type of data

var1=100
var2="200"
var3=["a","b","c"]
var4=("a","b","c")
var5=10.7
var6=20.7
var7=True
var8=False

print("Default Types")
print(var1, type(var1))
print(var2, type(var2))
print(var3, type(var3))
print(var4, type(var4))
print(var5, type(var5))
print(var6, type(var6))
print(var7, type(var7))
print(var8, type(var8))

var1=str(var1)
var2=int(var2)
var3=tuple(var3)
var4=list(var4)
var5=int(var5)
var6=str(var6)
var7=int(var7)
var8=str(var8)

print("\nTypes After Updation")
print(var1, type(var1))
print(var2, type(var2))
print(var3, type(var3))
print(var4, type(var4))
print(var5, type(var5))
print(var6, type(var6))
print(var7, type(var7))
print(var8, type(var8))


# In[ ]:


# different ways to present the data

var1=1000.0 # traditional float representation
var2=10e2 # variation - 1


print(var1, type(var1))
print(var2, type(var2))


# In[ ]:


# complex numbers
var1=10+4j
var2=10+4j
var3=10

print(var1, type(var1))
print(var2, type(var2))
summ=var1+var2
print(summ)

print(var3, type(var3))

var3=complex(var3) # Accepted !
print(var3, type(var3))

#var1=int(var1) # TypeError: can't convert complex to int


# ## Example - 4 04-08-2020

# In[ ]:


# Strings - Introduction - Printing
var1 = "I am the first String" # printing of string with ""

var2 = 'I am the second String'  # printing of string with ''

var3="""I
        am
        multiline
        string""" # printing of string in multiple line with ""

var4='''I
        am
        multiline
        string''' # printing of string in multiple line with ''

print(var1,type(var1))
print(var2,type(var2))
print(var3,type(var3))
print(var4,type(var4))


# In[ ]:


# Strings - Introduction - Accessing as Arrays
var1 = "I am the first String" #
        #012345678910........

print(var1[0]) # Strings are represented as Arrays  - char I
print(var1[1]) # Strings are represented as Arrays  - char space
print(var1[2]) # Strings are represented as Arrays  - char a
print(var1[3]) # Strings are represented as Arrays  - char m
print(var1[4]) # Strings are represented as Arrays  - char space

print(var1[2:4]) # Strings can be printed or accessed upto specific range also am " Indexing in Strings"

print(var1[2:]) # Strings can be printed or accessed upto specific range also am 

print(var1[:4]) # Strings can be printed or accessed upto specific range also am 

print(var1[-4:-2]) # Strings can be printed or accessed upto specific range also ri "Negative Indexing in Strings"

print(var1[-6:]) # Strings can be printed or accessed upto specific range also String

print(var1[:-2]) # Strings can be printed or accessed upto specific range also "I am the first Stri"


# ## Example - 5 05-08-2020

# In[ ]:


# String manipulation methods  len, lower, upper, replace, split

varstr = "I am the new string on new day"
print("\nLength of the entered string is:",len(varstr)) # to find the length of string entered by the user

varstr="I Am SECOND oNe"
print("\nString in lowercase is: ",varstr.lower()) # to change the case of string from normal case to lower case

varstr="I Am third oNe"
print("\nString in uppercase is: ",varstr.upper()) # to change the case of string from normal case to upper case

varstr="I am fourth in a row"
chartobechanged="a"
chartobechangedto="z"
print("\nNew String is: ",varstr.replace(chartobechanged,chartobechangedto)) # to replace particular char with new one
#print("\nNew String is: ",varstr.replace("a","z")) # to replace char "a" with "z"

varstr="Here, I come as a 5th, string"
print(varstr)
print("\nSplitted string is: ",varstr.split(",")) # , space, normal char --> used to split main string into sub strings

varstr="    Here, I come as a 6th, string   "
print(varstr, len(varstr))
varstr=varstr.strip() # to remove any space in beginning and at the end of string
print(varstr,len(varstr))


# ## Example - 6 06-08-2020

# In[ ]:


# String manipulation methods - 2

varstr1 = "I am the new string"
varstr2 = "on new day"
finalstring=varstr1 + varstr2
print("\nConcatenated string is:", finalstring) # to concatenate two strings


varstr3 = "I am the new string - See you again"
varstr4="new"
check=varstr4 in varstr3  # to check whether entered word is present in the string
print(check)

varstr3 = "I am the new string - See you again"
varstr4="NEW"  # NEW is not equal to new
check=varstr4 not in varstr3  # to check whether entered word is not present in the string
print(check)


# In[ ]:


# Tuples , Introduction

firsttuple=("a","b","a") # basic tuple
print(firsttuple)

print(firsttuple[1]) # accessing tuple by its positive index ( from left to right)

print(firsttuple[-1]) # accessing tuple by its negative index ( from right to left)

print(firsttuple[0:2]) # accessing tuple by its range


findele="a" # trying to find element b in the Tuple
srch=firsttuple.index(findele) # Search is based on its index
print(srch) # print results - index


findele="da" # trying to find element da in the Tuple which is not present
#srch=firsttuple.index(findele) # Search is based on its index
#print(srch) # print results - value error

findele="a" # trying to find element a in the Tuple which is present at 2 locations
srch=firsttuple.index(findele) # Search is based on its index
print(srch) # print results - index


# ## Example - 7 10-08-2020

# In[ ]:


## Operators - Arithmetic

#way 1

# v1=input('enter first no.')
# v2=input('enter second no.')
# print(int(v1)+int(v2))

#way 2
a= int(input("Enter First Number "))
b= int(input("Enter Second Number "))

# arithmetic operations
c= a+b
d= a*b
e= b-a
f= a/b
g= a%b
h= a**b
i= a//b

#print("Sum of",a,"and",b,"is",c) 

print("Sum of {} and {} is {}".format(a,b,c))
print("Multiplication of {} and {} is {}".format(a,b,d))
print("Subtraction of {} and {} is {}".format(a,b,e))
print("Division of {} and {} is {}".format(a,b,f))
print("Modulus of {} and {} is {}".format(a,b,g))
print("Exponentiation of {} and {} is {}".format(a,b,h))
print("Floor division of {} and {} is {}".format(a,b,i))


# In[ ]:


# Operators - Assignment

var1=int(input("enter any number"))

#var1=var1+10
var1+=10 #var1=var1 + 10 short notation to perform calculations
print(var1)

var1-=10 #var1=var1 - 10 short notation to perform calculations
print(var1)

var1*=10 #var1=var1 * 10 short notation to perform calculations
print(var1)

var1/=10 #var1=var1 / 10 short notation to perform calculations
print(var1)

var1%=10 #var1=var1 % 10 short notation to perform calculations
print(var1)

var1//=10 #var1=var1 // 10 short notation to perform calculations
print(var1)


# ## Example - 8 11-08-2020

# In[ ]:


# Operators - Assignment Comparison

a= int(input("Enter First Number: "))
b= int(input("Enter Second Number: "))

# ==, >, <, >=, <=, !=

print("\nStatus of a==b is",a==b) # TRUE or FALSE
print("\nStatus of a>b is",a>b) # TRUE or FALSE
print("\nStatus of a<b is",a<b) # TRUE or FALSE
print("\nStatus of a>=b is",a>=b) # TRUE or FALSE
print("\nStatus of a<=b is",a<=b) # TRUE or FALSE
print("\nStatus of a!=b is",a!=b) # TRUE or FALSE



# In[ ]:


# Operators - Logical Comparison

a= int(input("Enter value of a: "))
b= int(input("Enter value of b: "))

# and, or, not

print("\nStatus of and is ",a > b and a < 100 ) # TRUE or FALSE

print("\nStatus of or is",a > b or a < 100) # TRUE or FALSE

print("\nStatus of not is",not(a > b and a < 100)) # TRUE or FALSE


# In[ ]:


# Operators - Identity specification

var_list_1=["a","b","c"]

var_list_3=["a","b"]

print(var_list_1)
#print(var_list_2) this line will generate error 
print(var_list_3)

var_list_2=var_list_1 # var list 2 here is exactly same as list 1 because it is created from list 1 only

var_list_3=var_list_2 # var list 2 here is exactly same as list 1 because it is created from list 1 only

# is, is not

print(var_list_1 is var_list_2) #True

print(var_list_2 is not var_list_3) #False # var list 3 is not created from list 1

print(var_list_1)
print(var_list_2)
print(var_list_3)


# In[ ]:


# Operators - Membership specification

var_list_1=["a","b","c"]

var_list_3=["a","b"]

print("a" in var_list_1) # we can check whether particular element exists in the list or not

print("ab" in var_list_1)  # we can check whether particular element exists in the list or not

print("a" not in var_list_1)  # we can check whether particular element does not exist in the list or not


# ## Example - 9 12-08-2020

# In[ ]:


# Program Flow Control using if, if else

a= int(input("Enter First Number: "))
b= int(input("Enter Second Number: "))

if a > b:
    print("a is greater than b") # we are checking if a > b
    
elif a==b: # short form to write if else ( else if)
    print("a and b are equal")
    
else: # else statement must match with indentation of if statement
    print("b is greater than a") # we are not checking anything, if first is not true, this will execute
    
    
#3 combinations
#1. a=10, b=20
#2. a=20, b=10
#3. a=10, b=10


# In[ ]:


# Program Flow Control using if, if else - short hand notation - 1

a= int(input("Enter First Number: "))
b= int(input("Enter Second Number: "))

if a > b: print("a is greater than b") # we are checking if a > b


# In[ ]:


# Program Flow Control using if, if else - short hand notation - 2

a= int(input("Enter First Number: "))
b= int(input("Enter Second Number: "))

print("a is greater than b") if a > b else print("b is greater than a") # we are checking if a > b


# In[ ]:


# Program Flow Control using if, if else - short hand notation - 3

a= int(input("Enter First Number: "))
b= int(input("Enter Second Number: "))

print("a is greater than b") if a > b else print("a and b are equal")  if a == b else print("b is greater than a") 


# In[ ]:


# Program Flow Control using if, if else - more examples ( for all three numbers as separate inputs)

a= int(input("Enter First Number: "))
b= int(input("Enter Second Number: "))
c= int(input("Enter Third Number: "))

# some if statement we can add here to check whether input of a,b and c are equal or not

if a >= b and a >= c:
    print("a is greater than b and c") # we are checking if a > b
    
elif b >= a and b >= c: # short form to write if else ( else if)
    print("b is greater than a and c")
    
else: # else statement must match with indentation of if statement
    print("c is greater than a and b") # we are not checking 


# In[ ]:


#code provided by Cheki 
a=int(input("Enter the First Number:"))
b=int(input("Enter the Second Number:"))
c=int(input("Enter the Third Number:"))

if a>b and a>c:
    print("a is greater than b and c")

elif a==b and a==c:
    print("a is equal to b and c")

elif a==b and a>c:
    print("a and b is equal but greater than c")

elif b>c:
    print("b is greater than a and c")

elif b==c:
    print("b and c is equal but greater than a")

else:
    print("c is greater than a and b")


# ## Example - 10 13-08-2020

# In[ ]:


# Program Flow Control using if, if else - cont.. pass

a= int(input("Enter First Number: "))
b= int(input("Enter Second Number: "))
if a > b:
    # how to skip the execution of this section i.e. True case
    pass
else:
    print("b is greater than a")
    


# In[ ]:


# Program Flow Control using if, if else - cont.. nested if 

a= int(input("Enter a: "))
b= int(input("Enter b: "))

if a > b:
    print("a is greater than b") # we are checking if a > b
    
    if a > 100: #example of nested if else
        print("yes, a is greater than 100") 
        
    else: # else statement must match with indentation of if statement
        print("no, a is not greater than 100")
        
else:
    print("b is greater than a")
    


# In[ ]:


#even or odd by jayant

a = int(input("Enter any number"))
if a % 2 == 0:
    print("Even")
else:
    print("Odd")
 


# In[ ]:


#code by bharat

# no. of classes held
# no. of classes attended
# percentage of classess attended
cls_held=int(input('enter classes held'))
cls_attended=int(input('enter classes attended'))
if cls_attended <= cls_held:
    
    p=int((cls_attended/cls_held)*100)
    print('percentage is:',p)
    if p >=75:
        print('u r eligible to write exames')
    else:
         print('u r not eligible to write exames')
            
else:
    print('attended classes should be less then classes held')


# ## Example - 11 17-08-2020

# In[ ]:


# Loops - while - 3 condition, increment/decrement, initial value of loop

initial = 1 # initial value
while initial < 10: # termination condition
    print(initial) # printing of results
    initial=initial+1 # increment factor


# In[ ]:


# Loops - while - 3 condition, increment/decrement, initial value of loop

initial = 10 # initial value
while initial > 0: # termination condition
    print(initial) # printing of results
    initial=initial-1 # decrement factor


# In[ ]:


# Loops - while - 3 condition, increment/decrement, initial value of loop

initial = 10 # initial value
while initial > 0: # termination condition
    print(initial) # printing of results - indefinite times


# In[ ]:


# Loops - while - 3 , break

initial = 1 # initial value
while initial <= 10: # termination condition
    print(initial) # printing of results
    if initial == 5:
        break
    initial=initial+1 # increment factor


# In[ ]:


# Loops - while - 3 , continue

initial = 0 # initial value
while initial <10: # termination condition
    initial=initial+1 # increment factor
    if initial == 5:
        continue
    print(initial)
    


# In[ ]:


# Loops - while, else

initial = 1 # initial value
while initial <= 10: # termination condition
    print(initial) # printing of results
    initial=initial+1 # increment factor
else:
    print("Loop execution completed!!")


# ## Example - 12 18-08-2020

# In[ ]:


# Loops - for  - 3 -> condition, increment/decrement, initial value of loop - v1

for initial in range(10):
    print("initial") # printing of results


# In[ ]:


# Loops - for  - 3 -> condition, increment/decrement, initial value of loop - v2

for initial in range(1,10):
    print(initial) # printing of results


# In[ ]:


# Loops - for  - 3 -> condition, increment/decrement, initial value of loop - v3

for initial in range(1,10,2):
    print(initial) # printing of results


# In[ ]:


# Loops - for  - else
for initial in range(1,10,2):
    print(initial) # printing of results
else:
    print("execution terminates!!")


# In[ ]:


# Loops - for  - pass

for initial in range(1,10,2):
    if initial == 7:
        pass # skip the printing of 7
    else:
        print(initial)


# In[ ]:


# Loops - for  - break

for initial in range(1,10,2):
    if initial == 7:
        break # stops the execution of loop
    else:
        print(initial)


# In[ ]:


# Loops - for  - collections - ex 1

country = ["IND", "USA", "PAK"]

for initial in country:
    print(initial)


# In[ ]:


# Loops - for  - strings - ex 2

for initial in "country":
    print(initial)


# In[ ]:


# Loops - for  - using multiple for loops

states = ["PB", "KL"]
caps= ["CHD", "TRV"]

for i in states:
    for j in caps:
        print(i,j)


# ## Example - 13 19-08-2020

# In[ ]:


# Revisiting Strings - method - format, v1
marksObt=98
marksMax=100
var1 = "Great, I have scored {} marks out of {}!"

print(var1.format(marksObt,marksMax)) 


# In[ ]:


# Revisiting Strings - method - format, v2

var1 = "Great, I have scored {} marks out of {}!"

print(var1.format(98,100)) 


# In[ ]:


# Revisiting Strings - method - format, v3

marksObt=99
marksMax=100
percen=99.0
var1 = "Great, I have scored {1} marks out of {0} with {2}%"

print(var1.format(marksMax,marksObt,percen)) 


# In[ ]:


# Revisiting Strings - Escape Sequences \ backslash \n \t \\ \" \'

marksObt=99
marksMax=100
percen=99.0
var1 = '"Great Effort", You have scored {1} marks out of {0} with {2}%\n' # with single quote

var2 = "\"Great \nEffort\", \tYou have scored {1} marks out of {0} with {2}%" # with escape sequences

print(var1.format(marksMax,marksObt,percen)) 
print(var2.format(marksMax,marksObt,percen)) 


# ## Example - 14 20-08-2020

# In[ ]:


# String manipulation methods - find

varstr=input("Enter the string of your choice: ") # take string input from the user

keyword=input("Enter the keyword: ") # enter search keyword

result=varstr.find(keyword) # use find method to perform search

if result==-1: # if keyword is not found, it will return -1 else index of the keyword will be returned
    print("Keyword not found!!")
else:
    print("Keyword found at index",result)


# In[ ]:


# String manipulation methods - digit

varstr=input("Enter the string of your choice: ") # take string input from the user

ans=varstr.isdigit()

if ans==True: # if keyword is not found, it will return -1 else index of the keyword will be returned
    print("It's digit based!!")
else:
    print("It's not a digit based!!")


# In[ ]:


# String manipulation methods - alpha

varstr=input("Enter the string of your choice: ") # take string input from the user

ans=varstr.isalpha()

if ans==True: # if keyword is not found, it will return -1 else index of the keyword will be returned
    print("It's alpha based!!")
else:
    print("It's not alpha based!!")


# In[ ]:


# String manipulation methods - alpha

varstr=input("Enter the string of your choice: ") # take string input from the user

ans=varstr.isalnum() # a...z or 0...9

if ans==True: 
    print("It's alpha numeric based!!")
else:
    print("It's not alpha numeric based!!") # if we are going to enter special chars except a..z and 0..9


# In[ ]:


# String manipulation methods - startswith

varstr=input("Enter the string of your choice: ") # take string input from the user
key=input("Enter the key word:")
ans=varstr.startswith(key) # its going to check the first char of string
#ans=varstr.startswith(key,6) # its going to check the string from char available at mentioned index "6"

if ans==True: 
    print("It's starting with the mentioned key!!")
else:
    print("It's not starting with the mentioned key!!") # if we are going to enter special chars except a..z and 0..9


# In[ ]:


# String manipulation methods - title

varstr=input("Enter the string of your choice: ") # take string input from the user

ans=varstr.title() #Each word will be changed to its capital form

print(ans)


# ## Example - 15 24-08-2020

# In[ ]:


# Practice programs - 1
# Write a python script to find area of circle

from math import pi # namespace in python which helps to use in built methods/functions in the code

radius=float(input("Enter the value of radius: ")) # input to accept radius from user

area=pi * radius**2 # short notation for calculation

#print("Area of circle is",area) # printing of area on screen

print("Area of circle is {:.2f}".format(area)) # printing of area on screen upto 2 decimal places


# In[ ]:


# Practice programs - 2
# Write a python script to print current date time

import datetime # namespace containing date time functions
current = datetime.datetime.now() # to fetch current date and time
print(current) # to print date and time

print(current.strftime("%Y-%m-%d %H:%M:%S")) # splitting current date and time into variables


# In[ ]:


# Practice programs - 3
# Write a python script to print repeated entities ( n + nn + nnn + nnnn )

# User will input only single digit = 7
# 7
# 77
# 777
# 7777

# ANS=7+77+777+7777  
n=int(input("Enter the value of n: "))

n1= int("%s" %n) # first n
n2= int("%s%s" %(n,n)) # first nn
n3= int("%s%s%s" %(n,n,n)) # first nnn
n4= int("%s%s%s%s" %(n,n,n,n)) # first nnnn

ans=n1+n2+n3+n4

print(ans)



# ## Example - 16 25-08-2020

# In[ ]:


# # 
# ask user to input some number
# whatever that number is, suppose if user enters 10, we will find the difference of entered number with 50.
# if difference is more than 30, we will return the square or double of exact difference of two numbers

n=int(input("Enter the number of your choice: "))
max=50
diff=max-n

if diff > 30:
    print("Difference is ",diff)
    print("Square of difference is ",diff**2)
else:
    print("Difference is less than 30!, it is {}".format(diff))
    


# In[ ]:


# let us try to add three numbers ( user input based), 
# if all three numbers are not equal, calculate their sum
# if all three numbers are equal, then let us return thrice of calculated sum


# Example -1, 10, 20, 30 = 60
# Example -2, 10, 10, 10 = 30 * 3 = 90

a=int(input("Enter the number of your choice: "))
b=int(input("Enter the number of your choice: "))
c=int(input("Enter the number of your choice: "))

summ=a+b+c

if a==b==c:
    summ=summ * 3
    
print("Ans is {}".format(summ))
    


# In[ ]:


# take the string input from user, and try to find if it contains any vowel (a,e,i,o,u)

# Example -1, correct, yes it contains vowel
all_vows='aeiouAEIOU'
a=input("Enter the string of your choice: ")

# m1 if you are going to enter string or single char
c=False
for ch in a:
    if ch in all_vows:
        c=True

if c == True:
    print("M1-String contains vowel(s)")
else:
    print("M1-String does not contain any vowel(s)")

#-------------------------------------------------------
    
# m2 If you are going to check for single char only
if a in all_vows:
    print("M2-String contains vowel(s)")
else:
    print("M2-String does not contain any vowel(s)")


# ## Example - 17 26-08-2020

# In[ ]:


# Whether a number is even or odd, depending upon whether it is even or odd, suitable message to the user will be displayed

# take input of n from user
# apply the formula even or odd
# print the results

#By Jayant
# Program To Find Whether The Number is Even or Odd: 
n = int(input("Enter any number: ")) # Enter valid integer number
if n>0:
    if n % 2 == 0: # Here it is checking the remainder. If it is 0 it will print Even else Odd
        print(n,"is Even")
    else:
        print(n,"is Odd")
else:
    print("Not a valid input!!")


# In[ ]:


# Write a python script to print calendar

import calendar # namespace containing calendar functions

y = int(input("Enter year: ")) # Enter valid year
m = int(input("Enter month: ")) # Enter valid month

print(calendar.month(y,m)) #print calendar


# ## Example - 18 27-08-2020

# In[ ]:


# How to calculate area of triangle
# prime params are base of tr, height of tr.
# area = base * height/2

base=int(input("Enter the value of base: ")) # input for base - int
height=int(input("Enter the value of height: ")) # input for height - int
area = base * height/2 # calculate area
print("Area is ",area) # print area


# In[ ]:


# How to calculate (X+Y) * (X+Y)

X=int(input("Enter the value of X: ")) # input x - int
Y=int(input("Enter the value of Y: ")) # input y - int
print('ans = ''x\u00b2','+','y\u00b2','+','2xy')
ans = X * X + 2 * X * Y + Y * Y # x sup2
print("Ans is ",ans)


# In[ ]:


# First Number by def = 1
# Upto what limit you want to find sum = 5
# 1+2+3+4+5
# print sum of 1.....5
sm=0
limit=int(input("Enter the value of limit: ")) # input for limit - int
for i in range(1,limit+1):
    sm=sm+i
print("Sum is ",sm)


# ## Assignments- 1 31-08-2020

# ## Example - 19 01-09-2020

# In[ ]:


# Program To Take Multiple Inputs in Single Line By Cheki
x, y = input("Enter any two numbers: ").split()
z = int(x) + int(y)
print("Addition of two numbers is: ",z)


# In[ ]:


# Program To Take Multiple Inputs in Single Line By Banuka
# x, y = input("Enter a two value: ").split()
x, y = map(int,input("Enter two numbers seperated by space: ").split() )
z = x + y
print("Addition of two numbers is: ",z)


# ## Example - 20 03-09-2020

# In[ ]:


# Accept multiple integers and count the numbers also & print the sum by Banuka:
num = map(int,input("Enter numbers seperated by space: ").split(','))
total = 0
count = 0
for i in num:
count = count + 1 # counting the total numbers entered by user
total += i # total = total + i
print("Total numbers entered",count)
print("Sum = ",total)


# In[ ]:


# Program To Calculate BMI(Body Mass Index)
height = float(input("Enter the height "))
weight = float(input("Enter the weight "))
bmi = round(weight/height**2,2)
print("BMI:",bmi)


# In[ ]:


# Accept multiple strings and concat the strings by Banuka:
num = input("Enter numbers seperated by space: ").split(',')
total = ""
for i in num:
total = total +" "+ i # total = total + i
print("Sum = ",total)


# ## Example - 21 07-09-2020

# In[ ]:


#Intro to Lists
simplelist=["ele1","ele2","ele3"] # list to create with 3 elements
print(simplelist) # printing of list elements


# In[ ]:


#Intro to Lists
simplelist=["ele1","ele2","ele3","ele1","ele2","ele3"] # duplicate elements in the list can exits
print(simplelist) # printing of list elements


# In[ ]:


#Intro to Lists - how to access like arrays
simplelist=["ele1","ele2","ele3","ele1","ele2","ele3"] # duplicate elements in the list can exits
print(simplelist[0]) # printing of first element in list
print(simplelist[5]) # printing of last element in list


# In[ ]:


#Intro to Lists - list can contain multiple types of data
simplelist=["ele1",2,"ele3","ele1","ele2","ele3"] # duplicate elements in the list can exits
print(type(simplelist[0])) # printing of type of first element in list
print(type(simplelist[1])) # printing of type of second element in list


# In[ ]:


#Intro to Lists - list can contain multiple types of data
simplelist=["ele1","ele2","ele3","ele1","ele2","ele3"] # duplicate elements in the list can exits
print(simplelist[-1]) # printing of element from last in list


# In[ ]:


#Intro to Lists - list can contain multiple types of data
# print elements from 3rd till 5th in list
simplelist=["ele1","ele2","ele3","ele1","ele2","ele3"] 
print(simplelist[2:5]) # printing of elements as mentioned above


# In[ ]:


#Intro to Lists - list can contain multiple types of data
#print elements from first till 5th in list
simplelist=["ele1","ele2","ele3","ele4","ele5","ele6"] 
print(simplelist[:5]) # printing of elements as mentioned above


# In[ ]:


#Intro to Lists - list can contain multiple types of data
# print elements from 3rd till last in list
simplelist=["ele1","ele2","ele3","ele4","ele5","ele6"] 
print(simplelist[2:]) # printing of elements as mentioned above


# In[ ]:


# Intro to Lists - list can contain multiple types of data
# print elements from 3rd till last in list
# for(i=0;i<10;i++) or or for(;;)
# list[start:end:step] or list[::]

simplelist=["ele1","ele2","ele3","ele4","ele5","ele6","ele7"] 
print(simplelist[::]) # as simple as print(simplelist)
print(simplelist) # as simple as print(simplelist)
print(simplelist[::2]) # printing of elements at alternative 2nd location # this is unique
print(simplelist[2::]) # as simple as [2:]


# ## Example - 22 08-09-2020

# In[ ]:


# Intro to Lists - lists are changeable - through index

simplelist=["ele1",5,"ele2","ele3","ele4","ele5","ele6","ele7"] 
print(simplelist) # existing list

ind=int(input("Enter the index value for updation: ")) # value at index 0 or so
val=input("Enter the value: ") # actual value

# some code to replace
simplelist[ind]=val

# printing of new list - on the basis of input from the user
print(simplelist)



# In[ ]:


# Intro to Lists - lists are changeable - through value

simplelist=["ele1","ele2","ele3","ele4","ele5","ele6","ele7"] 
            #0 1 2 3 4 5 6 
print(simplelist) # existing list

exisval=input("Enter the existing value for updation: ") # must be a existing value 
# old input - ele2

newval=input("Enter the new value for updation: ") # any new value
# new input - element2

# some code to replace
if exisval in simplelist: # check whether existing val is in the list or not
    ind = simplelist.index(exisval) # it will check the index of existing value in list
#    print(ind)
    simplelist[ind]=newval # it is going to relace existing value with new one

# printing of new list - on the basis of input from the user
print(simplelist) # printing of new list



# ## Example - 23 09-09-2020

# In[ ]:


# Intro to Lists - lists are changeable - through value

simplelist=["ele1","ele2","ele3","ele4","ele5","ele6","ele7"] 

print(simplelist) # printing - way out -1

#print elements with the help of loop

for ele in simplelist:
    print(ele)  # printing - way out -2



# In[ ]:


# Intro to Lists - adding list elements - cheki

num=[10,20,30,40,50,60,70,80,90,100] 

#summ= 10+20+30+40+50+60+70+80+90+100
print("List elements are: " ,num) # printing - way out -1

#print elements with the help of loop
add=0
for i in num:
    add=add+i
    print(i,add)
print("Sum of elements is ",add)



# In[ ]:


# Intro to Lists - adding list elements - at alternative position only by cheki

simplelist=[10,20,30,40,50,60,70,80,90,100] 
            #0, 1, 2, 3, 4, 5, 6, 7, 8, 9
    
# 10+30+50+70+90 

print("List elements are: " ,simplelist[::2])  # print elements at alternative location with gap of 2,
#starting from 0th element

#print elements with the help of loop
add=0
for ele in simplelist[::2]:
    add=add+ele
    
print("Sum of elements is ",add)


# In[ ]:


# Intro to Lists - adding list elements - at alternative position only by cheki

simplelist=[10,20,30,40,50,60,70,80,90,100] 
            #0, 1, 2, 3, 4, 5, 6, 7, 8, 9
    
#   20+40+60+80+100

print("List elements are: ",simplelist[1::2]) # print elements at alternative location with gap of 2,
#starting from element at location 1

#print elements with the help of loop
add=0
for ele in simplelist[1::2]:
    add=add+ele
    
print("Sum of elements is ",add)


# In[ ]:


# Intro to Lists - length of list

simplelist=[10,20,30,40,50,60,70,80,90,100] 

print("No. of elements in list are ",len(simplelist))


# In[ ]:


# Intro to Lists - counting no. of occurrences of element in list

simplelist=[10,10,10,40,50,60,70,80,90,100] 

cnt=simplelist.count(10) # to count how many times particular element exits in the list

print("Element is repeated",cnt, "time(s)")


# ## Example - 24 10-09-2020

# In[ ]:


# Intro to Lists - add elements in the list  - last position by default

simplelist=[10,20,30,40,50,60,70,80,90,100] # default list
newval=int(input("Enter the element to add in the list: ")) # input statement to take new ele

print("existing list ",simplelist)
# add new ele in the list
simplelist.append(newval)

print("updated list ",simplelist)


# In[ ]:


# Intro to Lists - add elements in the list  - user defined position

simplelist=[10,20,30,40,50,60,70,80,90,100] # default list

idx=int(input("Enter the location: ")) # input statement to take location
newval=int(input("Enter the element: ")) # input statement to take new ele

print("existing list ",simplelist)

# add new ele in the list at user defined position
simplelist.insert(idx,newval)

print("updated list ",simplelist)


# In[ ]:


# Intro to Lists - remove elements in the list

simplelist=[10,20,30,40,50,60,70,80,90,100] # default list

delval=int(input("Enter the element to remove from the list: ")) # input statement to del existing ele

print("existing list ",simplelist)

# remove ele from the list, if it exists
simplelist.remove(delval)

print("updated list ",simplelist)


# In[ ]:


# Intro to Lists - remove last element from the list - by default

simplelist=[10,20,30,40,50,60,70,80,90,100] # default list

#delval=int(input("Enter the element to remove from the list: ")) # input statement to del existing ele

print("existing list ",simplelist)

# remove ele from the list, if it exists
simplelist.pop()

print("updated list ",simplelist)


# In[ ]:


# Intro to Lists - remove last element from the list - by default

simplelist=[10,20,30,40,50,60,70,80,90,100] # default list

idx=int(input("Enter the location to remove element from the list: ")) # input statement to del existing ele

print("existing list ",simplelist)

# remove ele from the list, if it exists
simplelist.pop(idx)

print("updated list ",simplelist)


# In[ ]:


# Intro to Lists - remove all elements from the list

simplelist=[10,20,30,40,50,60,70,80,90,100] # default list

print("existing list ",simplelist)

# remove all elements from the list and list itself too
del(simplelist)

#print(simplelist)


# In[ ]:


# Intro to Lists - remove all elements from the list by cheki

simplelist=[10,20,30,40,50,60,70,80,90,100] # default list

print("existing list ",simplelist)

# remove all elements from the list and retain EMPTY list
simplelist.clear()

print("Empty list ",simplelist)


# In[ ]:


simpleList=[10,20,30,40,50,60,70,80,90,100] #by abhishek
print("exiting list :",simpleList)
del simpleList[::] # to delete all elements only
print("updated list :",simpleList)


# In[ ]:


# Deleting all elements using for loop by jayant
list1 = [10,20,30,40,50,60,70,80]
for i in list1[:]:
    list1.remove(i)
print(list1)
print("All elements are deleted and list is empty now")


# ## Example - 25 14-09-2020

# In[ ]:


# Copying all elements from one list to another - first way to do it
exislist = [10,20,30,40,50,60,70,80] # to create list
print("Existing list", exislist) # to print list

listnew=exislist.copy() #copy method of python to copy one list into another

print("Copied list",listnew) # printing new list


# In[ ]:


# Copying all elements from one list to another - one way to do it, another one - 2nd way to do it
exislist = [10,20,30,40,50,60,70,80] # to create list
print("Existing list", exislist) # to print list
listnew=list(exislist) #copy method of python to copy one list into another
print("Copied list",listnew) # printing new list


# In[ ]:


# Creating a reference of one list to another - cheki
exislist = [10,20,30,40,50,60,70,80] # to create list
print("Existing list", exislist) # to print list

listnew=exislist #reference method of python from one list to another

print("Copied list",listnew) # printing new list


# In[ ]:


# Joining of lists - method -1
list1 = [10,20,30,40,50,60,70,80] # to create list
list2 = [90,100] # to create list

print("List-1:", list1) # to print list-1
print("List-2:", list2) # to print list-2

mergedlist = list1 + list2 # to join two lists, adding all elements together

print("Merged list:",mergedlist) # printing of joined list


# In[ ]:


# Joining of lists - method -2
list1 = [10,20,30,40,50,60,70,80] # to create list
list2 = [90,100] # to create list

print("List-1:", list1) # to print list-1
print("List-2:", list2) # to print list-2

for i in list2: # adding elements one by one
    list1.append(i) # with the use of append method

print("Merged list:",list1) # printing of joined list


# In[ ]:


# Joining of lists - method -3
list1 = [10,20,30,40,50,60,70,80] # to create list
list2 = [90,100] # to create list

print("List-1:", list1) # to print list-1
print("List-2:", list2) # to print list-2

list1.extend(list2) # with the use of append method

print("Merged list:",list1) # printing of joined list


# ## Example - 26 22-09-2020

# In[ ]:


# To reverese a list in python - by banuka
list1 = [10,20,30,40,50,60,70,80] # default list
print("Original list ",list1) # printing of list contents
list1=list1[::-1] # using the concept of indexing to reverse the list
print("Reversed list ",list1) # printing of list contents


# In[ ]:


# To reverese a list in python - by jayant
list1 = [10,20,30,40,50,60,70,80]
print("Original list ",list1) # printing of list contents
list1.reverse() # using the concept of inbult method reverse to reverse the list
print("Reversed list ",list1) # printing of list contents


# In[ ]:


# To slice a list, slicing means to divide the list into small segments

list1 = [10,20,30,40,50,60,70,80]
#index           0,1,2,3,4,5,6,7
print("Original list ",list1) # printing of list contents

# slicing syntax
print(list1[0:8:1]) # o/p [10, 20, 30, 40, 50, 60, 70, 80]

#slicing will take three arguments [0:8:1]
#0 = starting point  would be the starting index of list from where slicing will start
#8 = stopping point  would be the last element of list at where slicing will end
#1 = stepping point  would be the increment factor of slicing



# ## Example - 27 23-09-2020

# In[ ]:


# To slice a list, slicing means to divide the list into small segments - example -1

list1 = [1,2,3,4,5,6,7,8,9,10]
# 1, 3, 5, 7, 9,.... steps = 2
# 1, 2, 3, 4, 5,.... steps = 1
# 1, 4, 7, .... steps = 3

#index   0,1,2,3,4,5,6,7,8,9
print("Original list is",list1) # printing of list contents


# syntax is [ start : stop : steps]

#start is starting point of slicing
# stop is slicing of list from start till stop point
# steps is slicing by increment or decrement factor


# slicing syntax
print("Sliced list is",list1[0:8:1]) # o/p [1, 2, 3, 4, 5, 6, 7, 8]
print("Sliced list is",list1[1:8:2]) # o/p [2,4,6,8]
# 1,3,5,7 by bharat
# 2,4,6,8 by jayant, cheki


#slicing will take three arguments [0:8:1]
#0 = starting point  would be the starting index of list from where slicing will start
#8 = stopping point  would be the last element of list at where slicing will end
#1 = stepping point  would be the increment factor of slicing



# In[ ]:


###### To slice a list, slicing means to divide the list into small segments - example -2

# take one list and ask user to enter elements of the list of runtime
# add all those into list
# print the list
# sllice the list from element 3rd till last, if it contains elements more than 3

list1 = [] # empty list

lm=int(input("How many elements? ")) # take length of list as input

for i in range(0,lm):
    var=int(input("Enter element: ")) # take input of list elements upto length
    list1.append(var) # add elements in list
    
print("Original list is",list1) # printing of list contents
print("Length of list is",lm) # printing of list length

if (lm > 3): # if size of list is greater than 3
    print("Sliced list is",list1[2:lm:1]) # o/p printing of sliced list
else:
    print("List must have length greater than 3!")


# ## Example - 28 24-09-2020

# In[ ]:


#Introduction of Tuples, it is also a collection like lists - ex-1

#simplelist = [1,2,3,4,5,6,7,8,9,10] # list

simpletuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10) # Tuple - static with integer data

print("Tuple is", simpletuple) # printing of tuple elements

print("Type of data is ",type(simpletuple)) # printing of type


# In[ ]:


#Introduction of Tuples, it is also a collection like lists - ex-2

#simplelist = [1,2,3,4,5,6,7,8,9,10] # list

simpletuple = ("LPU","PUNJAB") # Tuple - static with string data

print("Tuple is", simpletuple) # printing of tuple elements

print("Type of data is ",type(simpletuple)) # printing of type


# In[ ]:


#Introduction of Tuples, it is also a collection like lists - ex-3

#simplelist = [1,2,3,4,5,6,7,8,9,10] # list

simpletuple = ("LPU","PUNJAB", 144001) # Tuple - static with different type of data

print("Tuple is", simpletuple) # printing of tuple elements

print("Type of data is ",type(simpletuple)) # printing of type


# In[ ]:


#Introduction of Tuples, it is also a collection like lists - ex-4 - how to access elements from first position

#simplelist = [1,2,3,4,5,6,7,8,9,10] # list

simpletuple = (10, 20, 30, 4, 5, 65, 7, 88, 9, 100) # Tuple - static with integer data

#print("Tuple is", simpletuple) # printing of tuple elements

print(simpletuple) # accessing all elements of tuple
print(simpletuple[0]) # accessing one element at a time with index position


# In[ ]:


#Introduction of Tuples, it is also a collection like lists - ex-4 - how to access elements from last position

#simplelist = [1,2,3,4,5,6,7,8,9,10] # list

simpletuple = (10, 20, 30, 4, 5, 65, 7, 88, 9, 100) # Tuple - static with integer data

print(simpletuple[-1]) # accessing one element at a time with index position

print(simpletuple[-2]) # accessing one element at a time with index position


# In[ ]:


#Introduction of Tuples, it is also a collection like lists - ex-5 - how to access elements with range of indexes

#simplelist = [1,2,3,4,5,6,7,8,9,10] # list

simpletuple = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100) # Tuple - static with integer data

print(simpletuple[0:5]) # accessing bunch of elements with start and end position

print("Starting from first element",simpletuple[:5]) # accessing bunch of elements with start and end position

#End parameter is 5 ( from first to last)

print("Starting from last element",simpletuple[-5:]) # accessing bunch of elements with start and end position

#start parameter is -5 ( from last to first)


# In[ ]:


#Introduction of Tuples, it is also a collection like lists - ex-6 - how to access elements with range of indexes

simpletuple = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100) # Tuple - static with integer data

# print the sum of all the elements of tuple ( 10+20+30....+100)
# print the sum of all the elements at even index (30+50+70...+100) or
# print the sum of all the elements at even index (10+30+50...+100) or
summ=0
for i in simpletuple:
    print(i)
    summ=summ+i
print("Sum of all elements is",summ)

summ=0
for i in simpletuple[0:10:2]:
    print(i)
    summ=summ+i
print("Sum of all elements at even index is",summ)

#or
summ=0
for i in simpletuple[2:10:2]:
    print(i)
    summ=summ+i
print("Sum of all elements at even index is",summ)


# ## Example - 29 28-09-2020

# In[ ]:


#Introduction of Tuples, it is also a collection like lists - ex-7 - how to update elements of tuple

simpletuple = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100) # Tuple - static with integer data

print("Tuple is",simpletuple)

simpletuple[0]=1000 # this line will generate an error because you cannot change tuple once its is defined.

print("Tuple is",simpletuple)

# diff -1, lists vs tuples
#1. list - it is changeable, if its tuple, it is unchangeable


# In[ ]:


#Introduction of Tuples, it is also a collection like lists - ex-8 - how to update elements of tuple

simpletuple = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100) # Tuple - static with integer data

print("Tuple is",simpletuple)

temp_list=list(simpletuple)

temp_list[0]=1000 # this line will not generate an error because you can change list elements.

print("Temporary list is",temp_list)

simpletuple=tuple(temp_list)

print("New Tuple is",simpletuple)

print("Type of data is",type(simpletuple))



# In[ ]:


#Introduction of Tuples, it is also a collection like lists -  how to access tuple elements one by one

simpletuple = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100) # Tuple - static with integer data

for item in simpletuple:
    print(item)




# In[ ]:


#Introduction of Tuples, it is also a collection like lists -  how to find length of tuple

simpletuple = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100) # Tuple - static with integer data

print("Length is",len(simpletuple))


# In[ ]:


#Introduction of Tuples, it is also a collection like lists -  how to check element in tuple

simpletuple = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100) # Tuple - static with integer data

if 50 in simpletuple:
    print("Yes, Exits!")
else:
    print("Missing!!")


# In[ ]:


#Introduction of Tuples, it is also a collection like lists -  how to delete tuple as you cannot remove elements from a tuple

simpletuple = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100) # Tuple - static with integer data

del simpletuple # tuple will be deleted

#print(simpletuple) # generate an error because tuple is already deleted by line 5.


# In[ ]:


#Introduction of Tuples, it is also a collection like lists -  how to join tuples

simpletuple1 = (10, 20, 30, 40, 50) # Tuple - static with integer data
simpletuple2 = (60, 70, 80, 90, 100) # Tuple - static with integer data

simpletuple= simpletuple1+simpletuple2 # + operator can be used to join n tuples

print(simpletuple) # printing of joined tuple


# ## Example - 30 29-09-2020

# In[ ]:


#Introduction of Tuples - with different methods

simpletuple = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100) # Tuple - static with integer data

print(simpletuple) # printing of tuple

ele=int(input("Enter the search element:")) # enter the element to be searched
ans=simpletuple.index(ele) # search and return the index of element

print("Element found at index: ",ans)


# In[ ]:


#Introduction of Tuples - with different methods

simpletuple = (10, 20, 30, 40, 50, 60, 70, 80, 50, 100) # Tuple - static with integer data

print(simpletuple) # printing of tuple

ele=int(input("Enter the search element:")) # enter the element to be searched
ans=simpletuple.count(ele) # search and return the no. of occureneces of element

print("Element is repeated",ans,"time(s)")


# In[ ]:


#Introduction of dictionaries  - how to define
# info can be represented in the form of KEY-VALUE pairs
examdict = {
    "name": "LENOVO",
    "year": 2020,
    "config": "I7"
            }
print(examdict)
print(type(examdict))


# In[ ]:


#Introduction of dictionaries - how to access
# info can be represented in the form of KEY-VALUE pairs
examdict = {
    "name": "LENOVO",
    "year": 2020,
    "config": "I7"
            }
print("Name is",examdict["name"]) # to print dict elements - key wise
print("Year is",examdict["year"]) # to print dict elements - key wise
print("Configuration is",examdict["config"]) # to print dict elements - key wise


# In[ ]:


#Introduction of dictionaries - how to access
# info can be represented in the form of KEY-VALUE pairs
examdict = {
    "name": "LENOVO",
    "year": 2020,
    "config": "I7"
            }

examdict["year"]=2021 # to update year value with the help of KEY
print(examdict) # printing of updated dictionary


# In[ ]:


#Introduction of dictionaries - how to update
# info can be represented in the form of KEY-VALUE pairs
examdict = {
    "name": "LENOVO",
    "year": 2020,
    "config": "I7"
            }

whichkey=input("Enter the key you want to change") # take input of key to be updated
newval=input("Enter the value you want to change") # take input of value to be updated

examdict[whichkey]=newval # to update value with the help of KEY
print(examdict) # printing of updated dictionary


# In[ ]:


#Introduction of dictionaries - how to update
# info can be represented in the form of KEY-VALUE pairs
examdict = { # base dictionary
    "name": "LENOVO",
    "year": 2020,
    "config": "I7"
            }

whichkey=input("Enter the key you want to change") # take input of key to be updated

if whichkey in examdict: #in keyword we can check whether key is present in dictionary or not
    newval=input("Enter the value you want to change") # take input of value to be updated
    examdict[whichkey]=newval # to update value with the help of KEY
else:
    print("KEY NOT FOUND!!") # will execute if key is not present 
    
    
print(examdict) # printing of updated dictionary


# ## Example - 31 30-09-2020

# In[ ]:


#Introduction of dictionaries - how to access all keys
# info can be represented in the form of KEY-VALUE pairs
examdict = {
    "name": "LENOVO",
    "year": 2020,
    "config": "I7"
            }

for key in examdict: # printing of all keys in dictionary
    print(key)


# In[ ]:


#Introduction of dictionaries - how to access all values
# info can be represented in the form of KEY-VALUE pairs
examdict = {
    "name": "LENOVO",
    "year": 2020,
    "config": "I7"
            }

for key in examdict: # printing of all values in dictionary
    print(examdict[key])


# In[ ]:


#Introduction of dictionaries - how to access all keys - values pairs
# info can be represented in the form of KEY-VALUE pairs
examdict = {
    "Name:": "LENOVO",
    "Year:": 2020,
    "Config:": "I7"
            }

print("Method - 1")
for key in examdict: # printing of all key value pairs in dictionary - ex1
    print(key,examdict[key])

print("\nMethod - 2")
for key,value in examdict.items(): # printing of all key value pairs in dictionary - ex2
    print(key,value)
    


# In[ ]:


#Introduction of dictionaries - how to find length of dictionary
# info can be represented in the form of KEY-VALUE pairs
examdict = {
    "Name:": "LENOVO",
    "Year:": 2020,
    "Config:": "I7"
            }

print("Length is",len(examdict))


# In[ ]:


#Introduction of dictionaries - how to add items in dictionary
# info can be represented in the form of KEY-VALUE pairs
studdict = {
    "Name:": "ABC",
    "Reg:": 123456
            }
# name, reg, email, phone no, country, gender info, programme, school
print(studdict)


# ## Example - 32 01-10-2020

# In[ ]:


#Introduction of dictionaries - how to add items in dictionary
# info can be represented in the form of KEY-VALUE pairs
studdict = {} #blank dictionary

# we can create no. of keys as per our requirements
studdict["name"]="ABC" # key-1 is name to take the input of student name
studdict["reg"]=12345
studdict["phoneno"]=67890
studdict["country"]="IND"
studdict["genderinfo"]="M"

print(studdict) # printing of student dictionary 


# In[ ]:


#Introduction of dictionaries - how to remove items fron dictionary
# info can be represented in the form of KEY-VALUE pairs
studdict = {
    "Name": "ABC",
    "Reg": 123456,
    "Phoneno":67890,
    "Country":"IND",
    "Genderinfo":"M"
            }

print(studdict) # printing of student dictionary 

dele=input("Enter the key which you want to delete?") # ask for user input of key to be deleted

if dele in studdict: # will check if key exists in dictionary or not
    studdict.pop(dele) # pop to delete key
    print("key is deleted!")
    print("\nupdated dictionary",studdict) # printing of updated student dictionary 
else:
    print("invalid key!")



# In[ ]:


#Introduction of dictionaries - how to remove all items fron dictionary
# info can be represented in the form of KEY-VALUE pairs
studdict = {
    "Name": "ABC",
    "Reg": 123456,
    "Phoneno":67890,
    "Country":"IND",
    "Genderinfo":"M"
            }

print(studdict) # printing of student dictionary 

del studdict # to delete complete dictionary

print(studdict) # will generate an error if dictionary is deleted by line no. 13


# In[ ]:


#Introduction of dictionaries - how to empty dictionary
# info can be represented in the form of KEY-VALUE pairs
studdict = {
    "Name": "ABC",
    "Reg": 123456,
    "Phoneno":67890,
    "Country":"IND",
    "Genderinfo":"M"
            }

print("Default dictionary",studdict) # printing of student dictionary 

studdict.clear() # to empty complete dictionary

print("Empty dictionary",studdict) # will generate an error if dictionary is deleted by line no. 13


# In[ ]:


#Introduction of dictionaries - how to add items in dictionary - dynamic way
# info can be represented in the form of KEY-VALUE pairs
cityinfo = {} #blank dictionary

# name of city, state of city, tourist attraction of city,
#travel mode, climate conditions, food choice

#Flow of program
# how may cities you want to enter? 1 or more
# what are the parameters you want to take for city? cityname, state, tourist attractions and so on
#user must enter the name of city with parameter - cityname
# enter the values of selected parameters
# print the record of city
# ask user again, do you want to enter any new city? if yes, reneter all details, if no, print results and quit



# ## Example - 33 05-10-2020

# In[ ]:


#Introduction of dictionaries - how to copy one dictionary into another - method -1
# info can be represented in the form of KEY-VALUE pairs
studdict = {
    "Name": "ABC",
    "Reg": 123456,
    "Phoneno":67890,
    "Country":"IND",
    "Genderinfo":"M"
            }

print("Default dictionary",studdict) # printing of student dictionary 

newstuddict=studdict.copy() # copy method allows us to copy the contents of one dict into another

print("Copied dictionary",newstuddict) # to print the copied contents of dict


# In[ ]:


#Introduction of dictionaries - how to copy one dictionary into another - method -2
# info can be represented in the form of KEY-VALUE pairs
studdict = {
    "Name": "ABC",
    "Reg": 123456,
    "Phoneno":67890,
    "Country":"IND",
    "Genderinfo":"M"
            }

print("Default dictionary",studdict) # printing of student dictionary 

newstuddict=dict(studdict) # dict() function allows us to copy the contents of one dict into another

print("Copied dictionary",newstuddict) # to print the copied contents of dict


# In[ ]:


#Introduction of dictionaries - how to use nested dictionaries
# info can be represented in the form of KEY-VALUE pairs
studdict = {
        
    "student1":{
    "Name": "ABC",
    "Reg": 123456,
    "Phoneno":67890,
    "Country":"IND",
    "Genderinfo":"M"
            },
    
    
    "student2":{
    "Name": "DEF",
    "Country":"US",
    "Genderinfo":"F"
            },
    
    "student3":{
    "Name": "GHI",
    "Reg": 99999,
    "Phoneno":55555,
    "Country":"CN"
            }
    
}
    

print("Default Nested dictionary",studdict) # printing of nested dictionary 



# In[ ]:


# Introduction of Functions - creating a function in Python

#1. Definition of function - line no. 8
#2. Body part of function  - line no. 9
#3. Calling of function - line no. 11


def myfunction(): # to define a function in the program, empty paranthesis means, this function will not take any arguments
    print("This is my first fun") # statement to be execute - while the function is called

myfunction() # to call a user defined function at line no. 3


# In[ ]:


# Introduction of Functions - creating a function in Python with arguments

#1. Definition of function with one argument - line no. 8
#2. Body part of function  - line no. 9
#3. Calling of function with one argument - line no. 11


def myfunction(var): # to define a function in the program, var in paranthesis means, this function will take one argument
    print("This is my first fun,",var) # statement to be execute - while the function is called

var=input("Please enter your name!") # input for function argument
myfunction(var) # to call a user defined function at line no. 3


# In[ ]:


# Introduction of Functions - calling statement of function must match with function definition Python

#1. Definition of function with one argument - line no. 8
#2. Body part of function  - line no. 9
#3. Calling of function with one argument - line no. 11


def myfunction(var): # to define a function in the program, var in paranthesis means, this function will take one argument
    print("This is my first fun,",var) # statement to be execute - while the function is called

var=input("Please enter your name!") # input for function argument
myfunction(var) #this should generate error, call of user defined function must match with function definition

myfunction() #this should generate error, call of user defined function must match with function definition


# ## Example - 34 06-10-2020

# In[ ]:


# Introduction of Functions - to add two numbers and print the result

# program to add two numbers with the help of function

def myfunction(var1, var2): # function to add two numbs, var1 and var2
    print("Sum of two numbers is",var1+var2) # addition of two numbers

var1=int(input("Enter number1:")) # input for function argument-1
var2=int(input("Enter number2:")) # input for function argument-2

myfunction(var1,var2) #call of user defined function to add two numbers


# In[ ]:


# Introduction of Functions - to add two numbers and print the result with RETURN

# program to add two numbers with the help of function

def myfunction(var1, var2): # function to add two numbs, var1 and var2
    return var1+var2 # addition of two numbers

var1=int(input("Enter number1:")) # input for function argument-1
var2=int(input("Enter number2:")) # input for function argument-2

print("Sum of two numbers is",myfunction(var1,var2)) #call of user defined function to add two numbers


# In[ ]:


# Introduction of Functions - to add n numbers and print the result with RETURN

# program to add two numbers with the help of function

# * is used to define arbitary arguments

def myfunction(*MasterVariable): # function to add n numbers with the help of arbitary variables
    ## perform addition
    summ=0
    for i in range(0,len(MasterVariable)):
        summ=summ+MasterVariable[i]
    return summ
    
var1=int(input("Enter number1:")) # input for function argument-1
var2=int(input("Enter number2:")) # input for function argument-2
var3=int(input("Enter number3:")) # input for function argument-3
var4=int(input("Enter number4:")) # input for function argument-4
var5=int(input("Enter number5:")) # input for function argument-5


print("Sum of five numbers is",myfunction(var1,var2,var3,var4,var5)) #call of user defined function to add two numbers


# In[ ]:


# code by jayant to add n numbers
def addNumber(*masterVariable): 
    result = 0
    for number in masterVariable:
        result = result + number
    return result
limit = int(input("Enter the limit: "))
summ = 0
for i in range(limit):
    num = int(input("Enter numbers: "))
    summ = summ + num
print("Sum = ",addNumber(summ))


# ## Example - 35 07-10-2020

# In[ ]:


# Introduction of Functions - to pass collection kind of data, for e.g. lists, tuples etc.

def myfunction(ListVariable): # function to add list elements
    ## perform addition
    summ=0
    for i in ListVariable:
        summ=summ+i
    return summ # result will be returned
    
varList=[10,20,30,40,50] # static list to be passed

print("Sum of list elements is",myfunction(varList)) #call of user defined function to add list elements


# In[ ]:


# Introduction of Functions - to skip the execution

def myfunction(): # function to print
    pass # to skip execution, we can write pass
    
myfunction() #call of user defined function


# In[ ]:


### Introduction of Functions - to pass arguments in different way

def myfunction(Var1,Var2,Var3): # function to add list elements
    print("Var1",Var1)
    print("Var2",Var2)
    print("Var3",Var3)
    print("\n")
    ## perform addition
    
var1=int(input("Enter number1:")) # input for function argument-1
var2=int(input("Enter number2:")) # input for function argument-2
var3=int(input("Enter number3:")) # input for function argument-3

#default call and value assignment
myfunction(var1,var2,var3) #call of user defined function -default

#modified call and value assignment
myfunction(Var3=var1,Var2=var2,Var1=var3) #call of user defined function -modified


# In[ ]:


### Introduction of Functions - to pass arguments in different way with default

def myfunction(myname= "no name"): # function to set default value of arguments
    print("Entered name is",myname)
        
var1=input("Enter your name:") # input for function argument-1

if len(var1) >0:
    myfunction(var1) #call of user defined function with 1 argument
else:
    myfunction() #call of user defined function with 0 argument
    


# ## Example - 36 08-10-2020

# In[ ]:


# introduction of recursion - draft-1 logic to be used in function
# enter the number 5, #5 * 4 * 3 * 2 * 1 = 120

#1. enter the num : 5 ( user input)
#2. Do processing ( take the advantage of for loop)
#3. display o/p

num=int(input("Enter the number:")) # user input for number
if num<0: # condition if it is negative number
    print("Invalid Input!")
elif num==0: # condition if it is equivalent to 0
    print("Factorial is 1")
else:
    fact=1
    for i in range(1,num+1): # loop to process 
        fact=fact*i
    print("Factorial is",fact) # to print the result


# In[ ]:


# introduction of recursion - draft-2 normal function call
# enter the number 5, #5 * 4 * 3 * 2 * 1 = 120

#1. enter the num : 5 ( user input)
#2. Do processing ( take the advantage of for loop)
#3. display o/p

def facto(num): # function to find factorial of a number
    if num<0: # condition if it is negative number
        print("Invalid Input!")
    elif num==0: # condition if it is equivalent to 0
        print("Factorial is 1")
    else:
        fact=1
        for i in range(1,num+1): # loop to process 
            fact=fact*i
        print("Factorial is",fact) # to print the result

num=int(input("Enter the number:")) # user input for number
facto(num) # call to a facto function


# In[ ]:


# introduction of recursion - draft-3 function with return value
# enter the number 5, #5 * 4 * 3 * 2 * 1 = 120

#1. enter the num : 5 ( user input)
#2. Do processing ( take the advantage of for loop)
#3. display o/p

def facto(num): # function to find factorial of a number
    if num<0: # condition if it is negative number
        ans="Invalid Input!"
    elif num==0: # condition if it is equivalent to 0
        ans="Factorial is 1"
    else:
        fact=1
        for i in range(1,num+1): # loop to process 
            fact=fact*i
        ans=fact
    return ans

num=int(input("Enter the number:")) # user input for number
 
print("Factorial is",facto(num)) # call to a facto function and to print the result


# In[ ]:


# introduction of recursion - draft-4 function with return value - recursive mode
# enter the number 5, #5 * 4 * 3 * 2 * 1 = 120

#1. enter the num : 5 ( user input)
#2. Do processing ( take the advantage of recursion)
#3. display o/p

def facto(num): # function to find factorial of a number
    if num==1: # condition if it is equivalent to 1
        return 1
    else:
        return num * facto(num-1) # recursive call to a function and returning of the results

num=int(input("Enter the number:")) # user input for number

print("Factorial is",facto(num)) # call to a facto function and to print the result


# In[ ]:


# introduction of function - main
# enter the number 5, #5 * 4 * 3 * 2 * 1 = 120

#1. enter the num : 5 ( user input)
#2. Do processing ( take the advantage of for loop)
#3. display o/p

def facto(num): # function to find factorial of a number
    if num<0: # condition if it is negative number
        ans="Invalid Input!"
    elif num==0: # condition if it is equivalent to 0
        ans="1"
    else:
        fact=1
        for i in range(1,num+1): # loop to process 
            fact=fact*i
        ans=fact
    return ans


# In[ ]:


def main(): # main function to call other functions 
    num=int(input("Enter the number:")) # user input for number
    results=facto(num) # call to a facto function
    print("Ans is",results)

if __name__ =='__main__': # used to execute main function
    main() # call to main function


# ## Example - 37 12-10-2020

# In[ ]:


#Introduction to file handling - 1. How to open a file - default location

#open  #function to open a file
# #Modes on which a file can be opened
# 1. READ r
# 2. APPEND a
# 3. WRITE w

# two types of files can be worked out
#1. Text file t
#2. Binary file b


f= open("myfile.txt") # file to be opened from default location where notebook file is saved.

f= open("myfile.txt","rt") # file to be opened from default location where notebook file is saved.

# line no. 14 and line no. 16 are same because r for read and t for text are default values

print(f.read()) # we can use read method for reading the contents of the file



# In[ ]:


#Introduction to file handling - 1. How to open a file - different location - way1 

#open  #function to open a file
# #Modes on which a file can be opened
# 1. READ r
# 2. APPEND a
# 3. WRITE w

# two types of files can be worked out
#1. Text file t
#2. Binary file b


f= open("Myfolder/myfile.txt") # file to be opened from different then default location where notebook file is saved.

print(f.read()) # we can use read method for reading the contents of the file



# In[ ]:


#Introduction to file handling - 1. How to open a file - different location - way2

#open  #function to open a file
# #Modes on which a file can be opened
# 1. READ r
# 2. APPEND a
# 3. WRITE w

# two types of files can be worked out
#1. Text file t
#2. Binary file b


f= open("Myfolder\\myfile.txt") # file to be opened from different then default location where notebook file is saved.

print(f.read()) # we can use read method for reading the contents of the file



# In[ ]:


#Introduction to file handling - 1. How to open a file - different location

#open  #function to open a file
# #Modes on which a file can be opened
# 1. READ r
# 2. APPEND a
# 3. WRITE w

# two types of files can be worked out
#1. Text file t
#2. Binary file b


f= open("Myfolder/myfile.txt") # file to be opened from different then default location where notebook file is saved.

print(f.read(6)) # we can use read method for reading the contents of the file upto particlar length



# In[ ]:


#Introduction to file handling - 1. How to open a file - File must exist!


f= open("Myfolder1/myfile.txt") # file to be opened from different then default location where notebook file is saved.

print(f.read()) # we can use read method for reading the contents of the file



# ## Example - 38 13-10-2020

# In[ ]:


#Introduction to file handling - 1. How to open a file - different location

f= open("MyFolder/myfile.txt") # file to be opened from different then default location where notebook file is saved.

print(f.read()) # we can use read method for reading the contents of the file upto particlar length



# In[ ]:


#Introduction to file handling - 1. How to close a file 

f= open("MyFolder/myfile.txt") # file to be opened from different then default location where notebook file is saved.

print(f.read()) # we can use read method for reading the contents of the file upto particlar length

f.close() # to close file object


# In[ ]:


#Introduction to file handling - 1. How to close a file , check if file is actually closed or not!!

f= open("MyFolder/myfile.txt") # file to be opened from different then default location where notebook file is saved.

print(f.read()) # we can use read method for reading the contents of the file upto particlar length

f.close() # to close file object

print(f.read()) # this willl generate an error as we have already closed file object in line no. 7


# In[ ]:


#Introduction to file handling - 1. write mode

f= open("MyFolder/myfile2.txt","w") # write to a new file always
temp=input("Enter file content:") # to enter the contents for the file
f.write(temp) # to write contents into a file
f.close()

f= open("MyFolder/myfile2.txt","rt") # file to be opened from different then default location where notebook file is saved.
print(f.read()) # we can use read method for reading the contents of the file

f.close() # to close file object


# In[ ]:


#Introduction to file handling - 1. Append Mode

f= open("MyFolder/myfile2.txt","a") # append mode to add contents in file
temp=input("Enter file content:")
f.write(temp)
f.close()

f= open("MyFolder/myfile2.txt","rt") # file to be opened from different then default location where notebook file is saved.
print(f.read()) # we can use read method for reading the contents of the file upto particlar length

f.close() # to close file object


# ## Example - 39 14-10-2020

# In[ ]:


#Introduction to file handling - 1. Empty file creation with x mode

f= open("MyFolder/myfile3.txt","x") # to create empty file

f.close() # to close file object


# In[ ]:


#Introduction to file handling - 1. Reading Empty file 

f= open("MyFolder/myfile3.txt","x") # to create empty file

print(f.read()) # read method is not executable on empty file, this will generate an error

f.close() # to close file object


# In[ ]:


#Introduction to file handling - 1. Property of x mode

f= open("MyFolder/myfile3.txt","x") # to create empty file but file already exists
# above code will generate an error

# x mode will display error if file is already exist on the system

f.close() # to close file object


# In[ ]:


#Introduction to file handling - 1. Delete mode to delete a file
import os # OS module carrying various features related to operations concerned with operating system

os.remove("MyFolder/myfile2.txt") # to delete an existing file from system


# In[ ]:


#Introduction to file handling - 1. Delete mode to delete a file which does not exist
import os # OS module carrying various features related to operations concerned with operating system

os.remove("MyFolder/myfile2.txt") # to delete an existign file from system

# if file does not exist, code will generate an error "The system cannot find the file specified: 'MyFolder/myfile2.txt"


# In[ ]:


#Introduction to file handling - 1. Delete mode to delete a folder
import os # OS module carrying various features related to operations concerned with operating system

# folder to be deleted - MyFolder
os.rmdir("MyFolder2") # to delete an existign folder from system

# you can delete only EMPTY folder


# In[ ]:


#Introduction to file handling - 1. Delete mode to delete a folder
import os # OS module carrying various features related to operations concerned with operating system

# folder to be deleted - MyFolder
os.rmdir("MyFolder") # to delete an existign folder from system

# this will generate an error because MyFoledr is carrying files "The directory is not empty: 'MyFolder'"


# In[ ]:


#Introduction to file handling - 1. How to check if file already exists
import os # OS module carrying various features related to operations concerned with operating system

if os.path.exists("MyFolder/myfile3.txt"): # to check the existence of file
    print("File exists!")
else:
    print("File does not exist!")


# ## Example - 40 15-10-2020

# In[ ]:


#Introduction to file handling - 1. How to open a file - different location - way2

#opt 1 to open a file

# f= open("Myfolder/myfile3.txt","rt") # file to be opened from different then default location where notebook file is saved.
# print(f.read()) # we can use read method for reading the contents of the file

#opt 2 to open a file with() function

with open("Myfolder/myfile.txt","rt") as f:# file to be opened from different then default location where notebook file is saved.
    print(f.read()) # we can use read method for reading the contents of the file
    f.close()



# In[ ]:


#Introduction to file handling - 1. How to write a file - different location - way2

#opt 1 to write a file

# f= open("Myfolder/myfile3.txt","w") # file to be opened from different then default location where notebook file is saved.
#f.write("Sample text we are writing in file") # we can use read method for reading the contents of the file
# f.close()

#opt 2 to write a file with() function

with open("Myfolder/myfile.txt","w") as f:# file to be opened from different then default location where notebook file is saved.
    f.write("Sample text we are writing in file") # we can use read method for reading the contents of the file
    f.close()



# In[ ]:


#Introduction to file handling - 1. How to rename a file 

# first ask user to enter the name of file - myfile.txt
# check whether file exists in systems or not
# enter new name of file
#rename otherwise we will inform user that file is not there

#"MyFolder/myfile3.txt"
import os # OS module carrying various features related to operations concerned with operating system

oldname=input("Enter the current name of file") # existing file in system

if os.path.exists(oldname): # to check the existence of file with old name
    print("File exists!")
    newname=input("Enter the new name of file:")
    
    os.rename(oldname,newname) #rename file with new name
    print("Name updated!")
    
    if os.path.exists(newname): # to check the existence of file with new name
        print("New File exists!")
    else:
        print("New File does not exist!")
else:
    print("File does not exist!") # if file does not exist in the system


# ## Example - 41 19-10-2020

# In[ ]:


# installation of NB EXTENSIONS implemented


# ## Example - 42 20-10-2020

# In[ ]:


#Introduction to file handling - 1. How to set the current file pointer (seek)
import os # OS module carrying various features related to operations concerned with operating system

if os.path.exists("MyFolder/myfile.txt"): # to check the existence of file
    print("File exists!")
    
    with open("Myfolder/myfile.txt","rt") as f:# file to be opened from different then default location where notebook file is saved.
        print("default:", f.read()) # we can use read method for reading the complete contents of the file
        
        f.seek(5) # to change the current position of file pointer to 5
        print("modified:", f.read()) # to read the contents from new location of file pointer
        f.close() # to close file
    
else:
    print("File does not exist!")


# In[ ]:


#Introduction to file handling - 1. How to get the current file pointer (tell)
import os # OS module carrying various features related to operations concerned with operating system

if os.path.exists("MyFolder/myfile.txt"): # to check the existence of file
    print("File exists!")
    
    with open("Myfolder/myfile.txt","rt") as f:# file to be opened from different then default location where notebook file is saved.
        print("Default Pointer location",f.tell()) # to fetch current location of pointer, default one
        print("default:", f.read()) # we can use read method for reading the complete contents of the file
        
        f.seek(5) # to change the current position of file pointer to 5
        print("Modified Pointer location",f.tell()) # to fetch current location of pointer, modified one
        print("modified:", f.read()) # to read the contents from new location of file pointer
        f.close() # to close file
    
else:
    print("File does not exist!")


# In[ ]:


#Introduction to file handling - 1. How to set the current file pointer (seek)
import os # OS module carrying various features related to operations concerned with operating system

if os.path.exists("MyFolder/myfile.txt"): # to check the existence of file
    print("File exists!")
    
    with open("Myfolder/myfile.txt","rt") as f:# file to be opened from different then default location where notebook file is saved.
        f.seek(-5) # must be a positve number , this will generate an error
        print(f.read()) # to read the contents from new location of file pointer
        f.close() # to close file
    
else:
    print("File does not exist!")


# In[ ]:


#Introduction to file handling - 1. How to fetch the list of files in directory/folder
import os # OS module carrying various features related to operations concerned with operating system

temp= os.listdir("MyFolder") # to list all the files in directory
print("No. of files in folder are", len(temp)) # count of files in folder
print("Details of files are",temp) # print the name of files
#print(type(temp))
   


# In[ ]:


#Introduction to file handling - 1. How to fetch only text files in directory/folder
import os # OS module carrying various features related to operations concerned with operating system

temp= os.listdir("MyFolder") # to list all the files in directory
print("No. of files in folder are", len(temp)) # count of files in folder
print("Details of files are",temp) # print the name of files
#print(type(temp))
   


# ## Example - 43 21-10-2020

# In[ ]:


#Introduction to file handling - 1. How to fetch only text files in directory/folder
import os # OS module carrying various features related to operations concerned with operating system

temp= os.listdir("MyFolder") # to list all the files in directory
print("No. of files in folder are", len(temp)) # count of files in folder
print("Details of files are",temp) # print the name of files
#print(type(temp))
print("===============================================================================")
count=0
for f in os.listdir("MyFolder"): # fetch the contents of folder , file by file
    if(f[-4:]=='.txt'):  # f is used to access file names,by using negative indexing here, we can print last 4 chars i.e. extension of file
        count=count+1 # count the no. of txt files found
        print(f) # this will print only names of text files
if (count>0): 
    print("Total files found!",count) # print the count of files found
else:
    print("0 file found!") # 0 files found
   


# In[ ]:


#Introduction to file handling - 1. How to DELETE only text files in directory/folder
import os # OS module carrying various features related to operations concerned with operating system

print("===============================================================================")

for f in os.listdir("MyFolder"): # fetch the contents of folder , file by file
    if(f[-4:]=='.txt'):  # f is used to access file names,by using negative indexing here, we can print last 4 chars i.e. extension of file
        print(f) # this will print only names of text files
        f="MyFolder/"+f # to generate complete path of file
        os.remove(f) # to remove text files


# ## Example - 44 22-10-2020

# In[ ]:


#Introduction to file handling - 1. How to read a file in different way ( reverse order )

import os # namespace which carries all os related methods

filename=raw_input("Enter the complete path of file:") # to take complete path as an input from user in Python 2

#filename=input("Enter the complete path of file:") # to take complete path as an input from user in Python 3

if os.path.exists(filename): # to check the existence of file
    print("File exists!")
    with open(filename,"rt") as f:# file to be opened from different then default location where notebook file is saved.
        subset=f.read() # to temporary store file contents
        #print(type(subset)) #to check the type of data which is returned by file object
        print(subset) # we can use read method for reading the contents of the file
        print(subset[::-1]) # we can use [start:end:step] to reverse the contents of the file
        f.close()

else:
    print("File does not exist!!")


# In[ ]:


#Introduction to file handling - 1. How to create a folder/directory

import os # namespace which carries all os related methods

filename=raw_input("Enter the name of new folder:") # to take complete path as an input from user in Python 2

#filename=input("Enter the name of new folder:") # to take complete path as an input from user in Python 3

os.mkdir(filename)
print("Directory created!")


# In[ ]:


#Introduction to file handling - 1. How to check existence of a folder/directory

import os # namespace which carries all os related methods

filename=raw_input("Enter the complete path of folder to search:") # to take complete path as an input from user in Python 2

#filename=input("Enter the complete path of folder to search:") # to take complete path as an input from user in Python 3

# if os.path.exists(filename): # to check the existence of directory way 1
#     print("Directory exists!")
# else:
#     print("Directory does not exist!")

if os.path.isdir(filename): # to check the existence of directory way 2
    print("Directory exists!")
else:
    print("Directory does not exist!")


# ## Example - 45 26-10-2020

# In[ ]:


#Introduction to Exception handling - 1. basic block

# Try block used to test a block for any kind of awkard inputs

# Except block used to handle any kind of awkard inputs

# Finally block used to handle a normal execution during any kind of awkard inputs

try: # try this code for execution
    a= int(input("Enter First Number "))
    b= int(input("Enter Second Number "))

    c= a+b # to add two numbers

    print("Sum of {} and {} is {}".format(a,b,c)) # to print o/p
    
except: # if exception occurs
    print("Exceptional input!!")


# In[ ]:


#Introduction to Exception handling - 2.  variants

# Try block used to test a block for any kind of awkard inputs

# Except block used to handle any kind of awkard inputs

# Finally block used to handle a normal execution during any kind of awkard inputs

try: # try this code for execution
    a= int(input("Enter First Number "))
    b= int(input("Enter Second Number "))

    c= a+b # to add two numbers

    print("Sum of {} and {} is {}".format(a,b,c)) # to print o/p
    
except: # if exception occurs
    print("Exceptional input!!")

finally: # it will be executed , does not matter if try execpt will generate any kind of exception
    print("Code executed !!")


# In[ ]:


# # enhance the functionality by using exception handling in this program
# ask user to input some number
# whatever that number is, suppose if user enters 10, we will find the difference of entered number with 50.
# if difference is more than 30, we will return the square or double of exact difference of two numbers

try:
    n=int(input("Enter the number of your choice: "))
    max=50
    diff=max-n

    if diff > 30:
        print("Difference is ",diff)
        print("Square of difference is ",diff**2)
    else:
        print("Difference is less than 30!, it is {}".format(diff))
except:
    print("Something went wrong!!")
    
finally:
    print("Code is executed!!")


# ## Example - 46 27-10-2020

# In[ ]:


#Introduction to Exception handling - How to raise a error specific message "Name Error"

# Try block used to test a block for any kind of awkard inputs
# Except block used to handle any kind of awkard inputs
# Finally block used to handle a normal execution during any kind of awkard inputs

try: # try this code for execution
    a= int(input("Enter First Number "))
    b= int(input("Enter Second Number "))

    c= a+b # to add two numbers

    print("Sum of {} and {} is {}".format(a,b,c)) # to print o/p

except NameError: # It will be raised when Name Error will occur.
    print("Number input is expected!")

except: # if some other exception occurs, except Name Error.
    print("Some other exception occurred!!")

finally: # it will be executed , does not matter if try execpt will generate any kind of exception
    print("Code executed !!")
    
# One try block can carry multiple except statements
# name specific exception can be mentioned in the code


# In[ ]:


#Introduction to Exception handling - How to raise a error specific message ""

#Introduction to file handling - 1. How to close a file , check if file is actually closed or not!!

try: # to implement exception handling
    
    f= open("MyFolder/myfile.txt") # file to be opened from different then default location where notebook file is saved.

    print(f.read()) # we can use read method for reading the contents of the file upto particlar length

    f.close() # to close file object

    print(f.read()) # this willl generate an error as we have already closed file object in line no. 7

except ValueError: # to take care value Error
    print("You are trying to access closed file!")

except: # to take care all other kind of errors
    print("Invalid I/O Operation!")


# ## Example - 47 28-10-2020

# In[ ]:


# different kind of errors in python, try to execute line by line

#print(5+'5') # TypeError
#--------------------------------------------------------------------------------------------
#ans=100/0 #ZeroDivisionError
#--------------------------------------------------------------------------------------------
#val=input("Enter val:"  #KeyboardInterrupt, stop the execution during input statement
#--------------------------------------------------------------------------------------------
#print "hello world! # python 2, but its not accepted in Python 3, # SyntaxError
#--------------------------------------------------------------------------------------------
# list1=[1,5,7,9]
# print(list1[4]) #IndexError  as max possible value is 3
#--------------------------------------------------------------------------------------------
#import randomname #ImportError
#--------------------------------------------------------------------------------------------
# studdict = {
#     "Name": "ABC"
#             }

# print("Default dictionary",studdict['Namee']) # KeyError
#--------------------------------------------------------------------------------------------
# m='Twenty'
# print(int(m)) # ValueError
#--------------------------------------------------------------------------------------------
# m='1'
# print(n) # NameError
#--------------------------------------------------------------------------------------------
# m=1
#     if m>1: #IndentationError
#         print("Random Text")
#     else:
#         print("1")
#--------------------------------------------------------------------------------------------


# In[ ]:


## Exception handling - on Operators - Arithmetic

try:
    
    a= int(input("Enter First Number "))
    b= int(input("Enter Second Number "))

    # arithmetic operations
    c= a+b;    d= a*b;    e= b-a;    f= a/b;    g= a%b;    h= a**b;    i= a//b; # use ; to add multiple statements in one line

    print("Sum of {} and {} is {}".format(a,b,c))
    print("Multiplication of {} and {} is {}".format(a,b,d))
    print("Subtraction of {} and {} is {}".format(a,b,e))
    print("Division of {} and {} is {}".format(a,b,f))
    print("Modulus of {} and {} is {}".format(a,b,g))
    print("Exponentiation of {} and {} is {}".format(a,b,h))
    print("Floor division of {} and {} is {}".format(a,b,i))
    
except NameError:
    print("Name Error")

except ZeroDivisionError:
    print("Zero Division Error")
    
except ValueError:
    print("Value Error")

except SyntaxError:
    print("Syntax Error")

except:
    print("Something went wrong!") 


# ## Example - 48 29-10-2020

# In[ ]:


#Introduction to Exception handling - How to display a system defined error message

try: 
    a= int(input("Enter First Number "))
    b= int(input("Enter Second Number "))

    c= a+b

    print("Sum of {} and {} is {}".format(a,b,c)) # to print o/p

except NameError as nm: # used to display system defined exception messages to the user
    print(nm)

except: # if some other exception occurs, except Name Error.
    print("Some other exception occurred!!")

finally: # it will be executed , does not matter if try execpt will generate any kind of exception
    print("Code executed !!")
    
# One try block can carry multiple except statements
# name specific exception can be mentioned in the code


# In[ ]:


## Exception handling - on Operators - Arithmetic to display custom and system defined messages to the user

try:
    
    a= int(input("Enter First Number "))
    b= int(input("Enter Second Number "))

    # arithmetic operations
    c= a+b;    d= a*b;    e= b-a;    f= a/b;    g= a%b;    h= a**b;    i= a//b; # use ; to add multiple statements in one line

    print("Sum of {} and {} is {}".format(a,b,c))
    print("Multiplication of {} and {} is {}".format(a,b,d))
    print("Subtraction of {} and {} is {}".format(a,b,e))
    print("Division of {} and {} is {}".format(a,b,f))
    print("Modulus of {} and {} is {}".format(a,b,g))
    print("Exponentiation of {} and {} is {}".format(a,b,h))
    print("Floor division of {} and {} is {}".format(a,b,i))
    
except NameError as nm:
    print("Name Error",nm)

except ZeroDivisionError as ze:
    print("Zero Division Error",ze)
    
except ValueError as ve:
    print("Value Error",ve)

except SyntaxError as se:
    print("Syntax Error",se)

except:
    print("Something went wrong!") 


# In[ ]:


## Exception handling - on Operators - Arithmetic by jayant
# single exception block to display system defined messages to the user

try:
    
    a= int(input("Enter First Number "))
    b= int(input("Enter Second Number "))

    # arithmetic operations
    c= a+b;    d= a*b;    e= b-a;    f= a/b;    g= a%b;    h= a**b;    i= a//b; # use ; to add multiple statements in one line

    print("Sum of {} and {} is {}".format(a,b,c))
    print("Multiplication of {} and {} is {}".format(a,b,d))
    print("Subtraction of {} and {} is {}".format(a,b,e))
    print("Division of {} and {} is {}".format(a,b,f))
    print("Modulus of {} and {} is {}".format(a,b,g))
    print("Exponentiation of {} and {} is {}".format(a,b,h))
    print("Floor division of {} and {} is {}".format(a,b,i))
    
except Exception as mess: # to handle all kin dof exceptions which can occur in the program
    print(mess) #to print system defined messages on the screen for the user


# In[ ]:


## Exception handling - on Operators - Arithmetic - how to write try code and normal code separately
# single exception block to display system defined messages to the user

try:
    a= int(input("Enter First Number "))
    b= int(input("Enter Second Number "))

    # arithmetic operations
    c= a+b;    d= a*b;    e= b-a;    f= a/b;    g= a%b;    h= a**b;    i= a//b; # use ; to add multiple statements in one line

except Exception as mess: # to handle all kin dof exceptions which can occur in the program
    print(mess) #to print system defined messages on the screen for the user

else: # it will execute if exception is not occurred in the code
    print("Sum of {} and {} is {}".format(a,b,c))
    print("Multiplication of {} and {} is {}".format(a,b,d))
    print("Subtraction of {} and {} is {}".format(a,b,e))
    print("Division of {} and {} is {}".format(a,b,f))
    print("Modulus of {} and {} is {}".format(a,b,g))
    print("Exponentiation of {} and {} is {}".format(a,b,h))
    print("Floor division of {} and {} is {}".format(a,b,i))


# ## Example - 49 02-11-2020

# In[ ]:


#Introduction to Exception handling - with Raise keyword - raising exceptions on the basis of particular conditions - 1

a= int(input("Enter First Number "))
b= int(input("Enter Second Number "))
c= a+b

# if sum of 2 numbers is less than 0, we can raise exception
if c < 0:
    raise Exception("Below 0, its invalid!") # with raise keyword, we can specify any case as an exceptional case
else:
    print("Sum of {} and {} is {}".format(a,b,c)) # to print o/p


# In[ ]:


#Introduction to Exception handling - with Raise keyword - raising exceptions on the basis of particular conditions - 2
# custom exception -1

a= int(input("Enter First Number "))
b= int(input("Enter Second Number "))
c= a-b

# if difference of 2 numbers is less than 0 or equal to 0, we can also raise exception
if c < 0:
    raise Exception("Below 0, its invalid!") # with raise keyword, we can specify any case as an exceptional case
elif c==0:
    raise ValueError("Equal to 0, it should be greater than 0!") # with raise keyword, we can raise a particular exception also
else:
    print("Sum of {} and {} is {}".format(a,b,c)) # to print o/p


# In[ ]:


# Introduction to Exception handling - with Raise keyword - raising exceptions on the basis of particular conditions
# custom or multiple user defined exceptions -1

class Error(Exception): # base class for exception
    pass
    
class Exception1(Error): # derived one for raising exceptions
    pass
    
class Exception2(Error): # derived one for raising exceptions
    pass
        

try:
    a= int(input("Enter First Number ")) # take input of first number
    b= int(input("Enter Second Number "))  # take input of second number
    c= a-b # subtract number 2 from number 1

    # if difference of 2 numbers is less than 0 or equal to 0, we can also raise exception

    if c < 0:
        raise Exception1 #raised if ans is less than 0
    elif c==0: 
        raise Exception2 #raised if ans is equal to 0
    else:
        print("Difference of {} and {} is {}".format(a,b,c)) # to print o/p
        
except Exception1: # user defined exception -1
    print("Below 0, its invalid!") # with raise keyword, we can specify any case as an exceptional case
    
except Exception2: # user defined exception -2
    print("Equal to 0, it should be greater than 0!") # with raise keyword, we can raise a particular exception also
    


# ## Example - 50 03-11-2020

# In[ ]:


# Introduction to Exception handling - with Raise keyword - raising exceptions on the basis of particular conditions
# custom or user defined exception -1

class ExceptionalError(Exception): # base one for raising exceptions
    pass

try:
    a= int(input("Enter First Number ")) # take input of first number
    b= int(input("Enter Second Number "))  # take input of second number
    c= a-b # subtract number 2 from number 1

    # if difference of 2 numbers is less than 0 or equal to 0, we can also raise exception

    if c < 0:
        raise ExceptionalError("Below 0, its invalid!") #raised if ans is less than 0
    else:
        print("Difference of {} and {} is {}".format(a,b,c)) # to print o/p
        
except ExceptionalError as Exception1: # user defined exception -1
    print(Exception1) # with raise keyword, we can specify any case as an exceptional case
    
except: # for all other exceptions except ExceptionalError
    print("For all other wrong inputs!")
    


# In[ ]:


## Exception handling - handling multiple exceptions at one go
try:
    
    a= int(input("Enter First Number "))
    b= int(input("Enter Second Number "))

    # arithmetic operations
    c= a+b;    d= a*b;    e= b-a;    f= a/b;    g= a%b;    h= a**b;    i= a//b; # use ; to add multiple statements in one line

    print("Sum of {} and {} is {}".format(a,b,c))
    print("Multiplication of {} and {} is {}".format(a,b,d))
    print("Subtraction of {} and {} is {}".format(a,b,e))
    print("Division of {} and {} is {}".format(a,b,f))
    print("Modulus of {} and {} is {}".format(a,b,g))
    print("Exponentiation of {} and {} is {}".format(a,b,h))
    print("Floor division of {} and {} is {}".format(a,b,i))
    
except (NameError, ZeroDivisionError, ValueError, SyntaxError): #you can club different errors into 1 to display a common message to the user
    print("Exception occured from { Name Error, Zero Division Error,Value Error,Syntax Error }")

except:# to take care rest of the exceptions
    print("Something went wrong!") 

