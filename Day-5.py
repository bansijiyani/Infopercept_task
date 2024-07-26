#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 11. Write a Python Program to accept two numbers and any arithmetic operator. According to arithmetic operator calculate the result and display it.
# (a) Using Multiple if  (b) Using if…elif if…elif  


num1 = float(input("Num 1 : "))
num2 = float(input("Num 2 : "))
operator = input("Enter any op (+,-,/,*): ")

if operator == '+':
    result = num1 + num2
    print(f"Result: {num1} + {num2} = {result}")

if operator == '-':
    result = num1 - num2
    print(f"Result: {num1} - {num2} = {result}")

if operator == '*':
    result = num1 * num2
    print(f"Result: {num1} * {num2} = {result}")

if operator == '/':
    if num2 != 0:
        result = num1 / num2
        print(f"Result: {num1} / {num2} = {result}")
    else:
        print("Invalid..")


# In[2]:


# Get input from the user
num1 = float(input("Num 1 : "))
num2 = float(input("Num 2 : "))
operator = input("Enter any op (+,-,/,*): ")

if operator == '+':
    result = num1 + num2
    print(f"Result: {num1} + {num2} = {result}")

elif operator == '-':
    result = num1 - num2
    print(f"Result: {num1} - {num2} = {result}")

elif operator == '*':
    result = num1 * num2
    print(f"Result: {num1} * {num2} = {result}")

elif operator == '/':
    if num2 != 0:
        result = num1 / num2
        print(f"Result: {num1} / {num2} = {result}")
    else:
        print("Invalid..")
else:
    print("Invalid..")


# In[ ]:





# In[ ]:





# In[3]:


# 12 . Write a program to get an alphabet from the user and display message UPPERCASE if it is uppercase alphabet or LOWERCASE if it is lowercase alphabet.

char = input("Enter alphabet char: ")

if len(char) == 1 and char.isalpha():
    if char.isupper():
        print("UPPERCASE")
    elif char.islower():
        print("LOWERCASE")
else:
    print("Not valid")
    


# In[ ]:





# In[4]:


#  13.Write a program that reads a character from keyboard and then prints it in reverse case.

char = input("Enter a character: ")

if len(char) == 1 and char.isalpha():
    if char.isupper():
        print(char.lower())
    elif char.islower():
        print(char.upper())
else:
    print("Invalid")


# In[ ]:





# In[7]:


# 14.Write a program to get the one character from user and find out this character is Vowel or Not.

c = input("Enter character :")
l = ['a','e','i','o','u','A','E','I','O','U']

if(c in l):
    print("Character is vowel")
else:
    print("Character is not vovel")


# In[ ]:





# In[ ]:





# In[11]:


# 15.Enter a character and display a message on the screen telling the user whether the character is an alphabet or digit, or any other special character.

ch = input("Enter character : ")

if(ch.isalpha()):
    print("Alphabet character ")
elif(ch.isdigit()):
    print("Digit character ")
else:
    print("Special character")


# In[ ]:





# In[ ]:





# In[12]:


# 16. Write a Python Program for the following:
# To calculate the gross salary based on the name of employee, his/her basic salary and sex entered through keyboard, consider the following rules.

# Basic Salary	Upto 4000	Beyond	4000
# but upto 8000
# Beyond	8000
# but upto 12000
# Beyond 12000

# DA (% of Basic)	14 %	12 %	10 %	8 %
# HRA	200	500	10 % of Basic	15 % of Basic

# Medical
# Male	150	250	500	2000
# Female	200	350	700	1200

# Gross Salary = Basic Salary + DA + HRA + Medical

# Input from user

name = input("Enter name: ")
basic = float(input("Enter basic salary: "))
sex = input("Enter gender (male/female): ").lower()

if basic <= 4000:
    da_perc = 14
elif basic <= 8000:
    da_perc = 12
elif basic <= 12000:
    da_perc = 10
else:
    da_perc = 8

da = (da_perc / 100) * basic

# Determine HRA
if basic <= 4000:
    hra = 200
elif basic <= 8000:
    hra = 500
elif basic <= 12000:
    hra = 0.10 * basic
else:
    hra = 0.15 * basic

if sex == 'male':
    if basic <= 4000:
        med = 150
    elif basic <= 8000:
        med = 250
    elif basic <= 12000:
        med = 500
    else:
        med = 2000
elif sex == 'female':
    if basic <= 4000:
        med = 200
    elif basic <= 8000:
        med = 350
    elif basic <= 12000:
        med = 700
    else:
        med = 1200
else:
    print("Please enter gender.")
    exit()

gross = basic + da + hra + med

print(f"Gross Salary for {name}: {gross:.2f}")


# In[ ]:





# In[ ]:





# In[14]:


# 17. Write a Python Program to calculate and print the final grade from the marks obtained in 5 different subjects. (Each of having 100 marks, equal weightage)
# Percentage Obtained (Average Marks)	Equivalent Final Grade 70 or Above		'O'
# Less than 70 but More or Equal to 60	'A'
# Less than 60 but More or Equal to 50	'B'
# Less than 50 but More or Equal to 40	'C'
# Less than 40	'F'


r_no = int(input("Enter roll no :"))
s_name = input("Enter name :")
s1 = int(input("Enter marks of subject 1 :"))
s2 = int(input("Enter marks of subject 2 :"))
s3 = int(input("Enter marks of subject 3 :"))
s4 = int(input("Enter marks of subject 4 :"))
s5 = int(input("Enter marks of subject 5 :"))

total_marks = s1 + s2 + s3 + s4 + s5
per = (total_marks / 500)*100
grade = 'a'

if per > 70:
    grade = 'O'
elif per<70 and per >60:
    grade = 'A'
elif per<60 and per >50:
    grade = 'B'
elif per<50 and per >40:
    grade = 'C'
else :
    grade = 'F'
print("==================================")
print("-------------Result---------------")
print("==================================")

print("Grade : ",grade,"grade")


# In[ ]:





# In[ ]:





# In[16]:


# 18. An electric power distribution company charges its domestic consumers as follow:
# Consumption Units	Rate of Charge
# 0
# -
# 200
# Rs. 0.40 per unit
# 201
# -
# 400
# Rs. 0.60 per unit + Rs. 100
# 401
# -
# 600
# Rs. 0.80 per unit + Rs. 250
# 601
# &
# above
# Rs. 1.00 per unit + Rs. 400



units = float(input("Enter the number of units consumed: "))

if units <= 200:
    rate = 0.40
    bill = units * rate
elif units <= 400:
    rate = 0.60
    bill = (units * rate) + 100
elif units <= 600:
    rate = 0.80
    bill = (units * rate) + 250
else:
    rate = 1.00
    bill = (units * rate) + 400

# Output the result
print("Total Bill :" ,bill )


# In[ ]:




