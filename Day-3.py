#!/usr/bin/env python
# coding: utf-8

# 1.

# In[3]:


# Write a Python Program to accept any number and check whether it is divisible by 9 or not

n = int(input("Enter any number :"))
if(n%9 == 0):
    print("Number is divisible by 9")
else:
    print("Number not divisible by 9")


# 2.

# In[5]:


# Write a Python Program to accept any number and check whether it is positive or negative
# (a) Using if…elif	(b) Using Multiple if (c) Using Ternary Operator


n1 = int(input("Enter the number :"))

if(n1>0):
    print("Positive number")
else:
    print("Negative Number")


# In[7]:


n2 = int(input("Enter the number :"))

if(n2 > 0):
    print("Positive Number")
if(n2 < 0):
    print("NEgative number")


# In[10]:


n3 = int(input("Enter num :"))

print("Positive number") if(n3 > 0) else print("Negative number")


# In[ ]:





# 3.

# In[11]:


# Write a program to read any number and determine whether a number is “ODD” or “EVEN” and print the message NUMBER IS ODD or NUMBER IS EVEN.
# (a) Using if…elif	(b) Using Multiple if (c) Using Ternary Operator


num1 = int(input("Enter the number :"))

if(num1 % 2 == 0):
    print("Even number")
else:
    print("Odd Number")


# In[12]:


num2 = int(input("Enter the number :"))

if(num2 % 2 == 0):
    print("Even Number")
if(num2 % 2 != 0):
    print("Odd number")


# In[13]:


num3 = int(input("Enter the number :"))

print("Even Number") if(num3 % 2==0) else print("Odd number")


# In[ ]:





# 4.

# In[21]:


# Write a Python Program to accept any year in four digits and check whether it is Leap Year or not.
# (a) Using if…elif	(b) Using Multiple if (c) Using Ternary Operator


y = int(input("Enter year in 4 digit :"))

if(y%400 == 0) or (y%4==0 and y%100!=0):
    print("Leap year")
else:
    print("Not leap year")


# In[31]:


y1 = int(input("Enter year in 4 digit :"))
    

if y1 % 4 == 0 and y1 % 100 != 0:
    print("Leap year")
    
if y1 % 400 != 0 and (y1 % 4 != 0 or y1 % 100 == 0):
    print("Not a leap year")

if y1 % 400 == 0:
    print("Leap year")



# In[32]:


y2 = int(input("Enter a year in 4 digits: "))

print("Leap year") if (y2 % 400 == 0 or (y2 % 4 == 0 and y2 % 100 != 0)) else print("Not a leap year")


# In[ ]:





# 5.

# In[34]:


# Write a Python Program to get two numbers from keyboard and print the maximum number among them.
# (a) Using if…elif	(b) Using Multiple if (c) Using Ternary Operator


n1 = input("Enter number 1 :")
n2 = input("Enter number 2 :")

if(n1>n2):
    print("Greatest number is : ",n1)
else:
    print("Greatest number is : ",n2)


# In[35]:


n1 = input("Enter number 1 :")
n2 = input("Enter number 2 :")

if(n1>n2):
    print("Greatest number is : ",n1)
    

if(n1 < n2):
    print("Greatest number is : ",n2)


# In[37]:


n1 = input("Enter number 1 :")
n2 = input("Enter number 2 :")

print("Greatest number is : ",n1) if (n1 > n2) else print("Greatest number is : ",n2)


# In[ ]:





# In[ ]:





# #
# 6

# In[40]:


# Write a program, which reads two integer values. If the first is less than the second, print the message UP. If the second is less than first, print the message DOWN If the numbers are equal, print the message EQUAL.
# (a) Using if…elif if…elif	(b) Using Multiple if (c) Using Nested Ternary

nm1 = input("Enter number 1 :")
nm2 = input("Enter number 2 :")

if(nm1 < nm2):
    print("UP")
elif(nm1 < nm2):
    print("DOWN")
else:
    print("EQUAL")
    
    


# In[41]:


nm1 = input("Enter number 1 :")
nm2 = input("Enter number 2 :")

if(nm1 < nm2):
    print("UP")
    
if(nm1 > nm2):
    print("DOWN")

if(nm1 == nm2):
    print("EQUAL")


# In[44]:


nm1 = input("Enter number 1 :")
nm2 = input("Enter number 2 :")

print("UP") if (nm1 < nm2) else print("DOWN") if(nm1 > nm2) else print("EQUAL")


# In[ ]:





# In[ ]:





# In[45]:


# 7. Write a Python Program to get any number from the console and check whether it is positive, negative or zero.
# (a) Using Multiple if	(b) Using if…elif if…elif if…elif (c) Using Nested Ternary




# In[47]:


num = float(input("Enter a number: "))

if num > 0:
    print("Positive")

if num < 0:
    print("Negative")

if num == 0:
    print("Zero")


# In[48]:


num = int(input("Enter a number: "))

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
elif num == 0:
    print("Zero")


# In[49]:


num = float(input("Enter a number: "))

print("Positive") if num > 0 else print("Negative") if num < 0 else print("Zero")


# In[ ]:





# In[ ]:





# In[50]:


# 8. Write a program that will read three numeric values from the user and find out and display the larger one.
# (a) Using Multiple if	(b) Using Nested if  (c) Using if…elif if…elif	(d) Using Nested Ternary


# In[52]:


n1 = input("Enter the first number: ")
n2 = input("Enter the second number: ")
n3 = input("Enter the third number: ")

if(n1 > n2 and n1 > n3):
    print("Greatest num is : ",n1)
elif(n2 > n3):
    print("Greatest num is : ",n2)
else:
    print("Greatest num is : ",n3)


# In[56]:


n1 = input("Enter the first number: ")
n2 = input("Enter the second number: ")
n3 = input("Enter the third number: ")

if(n1 > (n2 and n3)):
     print("Greatest num is : ",n1)
        
if(n2 > (n1 and n3)):
     print("Greatest num is : ",n2)

if(n3 > (n1 and n2)):
     print("Greatest num is : ",n3)


# In[58]:


n1 = input("Enter the first number: ")
n2 = input("Enter the second number: ")
n3 = input("Enter the third number: ")

if n1 >= n2:
    if n1 >= n3:
        l = n1
    else:
        l = n3
else:
    if n2 >= n3:
        l = n2
    else:
        l = n3

print("gratest number is:", l)


# In[60]:


n1 = input("Enter the first number: ")
n2 = input("Enter the second number: ")
n3 = input("Enter the third number: ")



if n1 >= n2 and n1 >= n3:
    l = n1
elif n2 >= n1 and n2 >= n3:
    l = n2
else:
    l = n3

print("greatest number is:", l)


# In[ ]:





# In[ ]:





# In[62]:


# 9. Write a Python Program to input marks of 3 subjects and calculate total, percentage, result and grade.
# (a) Using Multiple if	(b) Using Nested if  (c) Using if…elif if…elif


r_no = int(input("Enter roll no :"))
s1 = int(input("Enter marks of subject 1 :"))
s2 = int(input("Enter marks of subject 2 :"))
s3 = int(input("Enter marks of subject 3 :"))
total_marks = s1 + s2 + s3
per = (total_marks / 300)*100
grade = 'a'

if per>90:
    grade = 'A'
elif per>80 and per < 90:
    grade = 'B'
elif per>60 and per < 80:
    grade = 'C'
elif per>40 and per < 60:
    grade = 'D'
else :
    grade = 'E'
print("==================================")
print("-------------Result---------------")
print("==================================")
print("Total marks : ",total_marks)
print("percentage :",per,"%")
print("Grade : ",grade,"grade")


# In[63]:


# Input: Read roll number and marks for three subjects from the user
r_no = int(input("Enter roll number: "))
s1 = int(input("Enter marks of subject 1: "))
s2 = int(input("Enter marks of subject 2: "))
s3 = int(input("Enter marks of subject 3: "))

# Calculate total marks and percentage
total_marks = s1 + s2 + s3
per = (total_marks / 300) * 100

# Initialize grade
grade = 'E'  # Default grade

# Determine the grade using multiple if statements
if per > 90:
    grade = 'A'
if 80 < per <= 90:
    grade = 'B'
if 60 < per <= 80:
    grade = 'C'
if 40 < per <= 60:
    grade = 'D'
if per <= 40:
    grade = 'E'

# Print the results
print("==================================")
print("-------------Result---------------")
print("==================================")
print("Total marks:", total_marks)
print("Percentage:", per, "%")
print("Grade:", grade, "grade")


# In[ ]:





# In[ ]:





# In[ ]:





# In[64]:


# 10. Write a Python Program to accept any day number between 1 to 7 and print the message as Monday if day number is 1, Tuesday if day number is 2, Wednesday if day number is 3 and so on. Also display appropriate message if the day number is less than 1 or greater than 7.
# Using Multiple if  (b) Using if…elif if…elif  


day_num = int(input("Enter a day (1-7): "))

if day_num == 1:
    print("Monday")
if day_num == 2:
    print("Tuesday")
if day_num == 3:
    print("Wednesday")
if day_num == 4:
    print("Thursday")
if day_num == 5:
    print("Friday")
if day_num == 6:
    print("Saturday")
if day_num == 7:
    print("Sunday")
if day_num < 1 or day_num > 7:
    print("Invalid day number.")


# In[65]:


day_num = int(input("Enter a day number (1-7): "))

if day_num == 1:
    print("Monday")
elif day_num == 2:
    print("Tuesday")
elif day_num == 3:
    print("Wednesday")
elif day_num == 4:
    print("Thursday")
elif day_num == 5:
    print("Friday")
elif day_num == 6:
    print("Saturday")
elif day_num == 7:
    print("Sunday")
else:
    print("Invalid day number.")


# In[ ]:





# In[ ]:





# In[67]:


# Write a Python Program to accept any number between 0 to 9 and print the message as Zero if number is 0, One if number is 1, Two if number is 2 and so on. Also display "Number must be positive and in one digit only" if the number is less than 0 or greater than 9.
# Using Multiple if  (b) Using if…elif if…elif  

num = int(input("Enter a number (0-9): "))

if num == 0:
    print("Zero")
if num == 1:
    print("One")
if num == 2:
    print("Two")
if num == 3:
    print("Three")
if num == 4:
    print("Four")
if num == 5:
    print("Five")
if num == 6:
    print("Six")
if num == 7:
    print("Seven")
if num == 8:
    print("Eight")
if num == 9:
    print("Nine")
if num < 0 or num > 9:
    print("Invalid")


# In[68]:


num = int(input("Enter a number (0-9): "))

if num == 0:
    print("Zero")
elif num == 1:
    print("One")
elif num == 2:
    print("Two")
elif num == 3:
    print("Three")
elif num == 4:
    print("Four")
elif num == 5:
    print("Five")
elif num == 6:
    print("Six")
elif num == 7:
    print("Seven")
elif num == 8:
    print("Eight")
elif num == 9:
    print("Nine")
else:
    print("Invalid")


# In[69]:


# Write a Python Program to accept any month number between 1 to 12 and print the message as January if month number is 1, February if month number is 2, March if month number is 3 and so on. Also print the number of days for that month and display appropriate message if the month number is less than 1 or greater than 12.
# (a) Using Multiple if  (b) Using if…elif if…elif  


mn = int(input("Enter a month number (1-12): "))

if mn == 1:
    print("January, 31 days")
if mn == 2:
    print("February, 28 or 29 days")
if mn == 3:
    print("March, 31 days")
if mn == 4:
    print("April, 30 days")
if mn == 5:
    print("May, 31 days")
if mn == 6:
    print("June, 30 days")
if mn == 7:
    print("July, 31 days")
if mn == 8:
    print("August, 31 days")
if mn == 9:
    print("September, 30 days")
if mn == 10:
    print("October, 31 days")
if mn == 11:
    print("November, 30 days")
if mn == 12:
    print("December, 31 days")
if mn < 1 or mn > 12:
    print("Invalid month number.")


# In[70]:


mn = int(input("Enter a month number (1-12): "))

if mn == 1:
    print("January, 31 days")
elif mn == 2:
    print("February, 28 or 29 days")
elif mn == 3:
    print("March, 31 days")
elif mn == 4:
    print("April, 30 days")
elif mn == 5:
    print("May, 31 days")
elif mn == 6:
    print("June, 30 days")
elif mn == 7:
    print("July, 31 days")
elif mn == 8:
    print("August, 31 days")
elif mn == 9:
    print("September, 30 days")
elif mn == 10:
    print("October, 31 days")
elif mn == 11:
    print("November, 30 days")
elif mn == 12:
    print("December, 31 days")
else:
    print("Invalid month number.")


# In[ ]:




