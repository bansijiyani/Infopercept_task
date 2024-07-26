#!/usr/bin/env python
# coding: utf-8

# #
# 1. Print Simple Welcome message like “Welcome to the world of Python Programming”.

# In[1]:


print("Welcome to the world of Python Programming")


# #
# 2. Write a Python Program to print Your Personal Details like Name, Address, City, Pincode, PhoneNo etc.
# 

# In[2]:


print("------- Personal Information ---------")
print("Name : Bansari JIyani")
print("Address : Surat , Gujarat")
print("City : Surat")
print("Pincode : 395006")
print("Mobile No : 9016407466")


# #
# 3. Write a Python Program to print Book Details like Book Id, Book Title, AuthorName, PublisherName, Price etc.
# 

# In[4]:


print("----- BOOK DETAILS -----")
print("Book Id : a20034")
print("Book Title : Atomic Habits")
print("Author Name : James Clear")
print("Publisher Name : Penguin Random House")
print("Price : 700")


# #
# 4. Write a Python Program to print any Product Information like Product ID, Product Name, Price etc.

# In[5]:


print("----- PRODUCT DETAILS -----")
print("Product Id : P12457")
print("Product Name : CPU")
print("Price : 5000")


# #
# 5. Write a Python Program to print mark sheet.
# 

# In[6]:


r_no = int(input("Enter roll no :"))
s_name = input("Enter name :")
s1 = int(input("Enter marks of subject 1 :"))
s2 = int(input("Enter marks of subject 2 :"))
s3 = int(input("Enter marks of subject 3 :"))
s4 = int(input("Enter marks of subject 4 :"))
total_marks = s1 + s2 + s3 + s4
per = (total_marks / 400)*100
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


# #
# 6. Write a Python Program to print the following string. (Use of Escape Sequence for “ ” DOUBLE QUATE) Someone Said “Nothing is Impossible in this World”.
# 

# In[9]:


s = "Someone Said \"Nothing is Impossible in this World\" "
print(s)


# #
# 8. Write a Python Program to display your visiting card.
# 

# In[13]:


shop_name = "Art Gallary"
owner = "Bansari Jiyani"
mail = "bansijiyani@gmail.com"
m_no = 9014539893
w_no = 3457652365

print("------- Visiting Card -------\nShop Name :",shop_name,"\nOwner Name : ",owner,"\nGmail : ",mail,"\nMobile No :",m_no,"\nWhatsApp No : ",w_no)



# #
# 9. Write a Python Program to display your visiting card.
# Write a Python Program to print the following string. (Use of Escape Sequence for ‘ ’ SINGLE QUATE) Someone Said ‘God is Great’.
# 

# In[11]:


s_q = "Someone said \'God is great\'"
print(s_q)


# 10.

# In[14]:


collage = input("Enter your collage name : ")
stream = input("Enter your Stream :")
y = input("Enter year :")
s = input("Enter semester : ")


print("--------- Collage information---------")
print("Collage Name : ",collage)
print("Stream : ",stream)
print("Year : ",y)
print("Semester : ",s)


# 11.

# In[18]:


n1 = int(input("Enter integer value :"))
n2 = float(input("Enter float value :"))
print("Nuber 1 :",n1)
print("Number 2: ",n2)


# 12

# In[20]:


d = int(input("Enter dollar :"))
r = d * 80
print("Rupees : ",r)


# 13.

# In[21]:


r = int(input("Enter Rupees :"))
d = r/80
print("Dollar : ",d)


# 14.

# In[22]:


l = int(input("Enter Liter :"))
m = l * 1000
print("Mililiter :",m)


# 15.

# In[23]:


f = int(input("Enter fehrenhit : "))
c = (f-32)/1.8
print("Celsius :",c)


# 16.

# In[24]:


km = int(input("Enter kilometer :"))
m = km * 1000
cm = m * 100
print("Miter : ",m)
print("Centimeter : ",cm)


# 17.

# In[26]:


p = int(input("Enter pound :"))
r = p*90
print("Rupees : ",r)


# In[ ]:





# In[27]:


dollar = int(input("Enter Dollar :"))
p = dollar/2
print("Pound :",p)


# In[ ]:





# In[28]:


kg = float(input("Enter kg: "))
g = kg * 1000
print("Grams: ", g)


# In[ ]:





# In[29]:


g = float(input("Enter grams: "))
kg = g / 1000
print("Kg: ", kg)


# In[ ]:





# In[30]:


a = float(input("Enter number 1: "))
b = float(input("Enter number 2: "))

add = a + b
sub = a - b
mul = a * b
div = a / b

print("Add: ", add)
print("Sub: ", sub)
print("Mul: ", mul)
print("Div: ", div)


# In[ ]:





# In[31]:


num = float(input("Enter number: "))
sq = num ** 2
cube = num ** 3

print("Square: ", sq)
print("Cube: ", cube)


# In[ ]:





# In[32]:


age1 = int(input("Enter age 1: "))
age2 = int(input("Enter age 2: "))
age3 = int(input("Enter age 3: "))

avg = (age1 + age2 + age3) / 3

print("Avg age: ", avg)


# In[ ]:





# In[33]:


r = float(input("Enter radius: "))
area = 3.14 * r ** 2

print("Area: ", area)


# In[ ]:





# In[34]:


r = float(input("Enter radius: "))
circumference = 2 * 3.14 * r

print("Circumference: ", circumference)


# In[ ]:





# In[35]:


P = float(input("Enter principal: "))
R = float(input("Enter rate: "))
N = int(input("Enter time: "))

SI = (P * R * N) / 100

print("SI: ", SI)


# In[ ]:





# In[36]:


P = float(input("Enter principal: "))
R = float(input("Enter rate: "))
N = int(input("Enter time: "))
CI = P * (1 + R / 100) ** N - P

print("CI: ", CI)


# In[ ]:





# In[37]:


P = float(input("Enter Amount: "))
R = float(input("Enter rate: "))
N = float(input("Enter time: "))

SI = (P * R * N) / 100
CI = P * (1 + R / 100) ** N - P
diff = CI - SI

print("SI: ", SI)
print("CI: ", CI)
print("Diff: ", diff)


# In[ ]:





# In[38]:


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

temp = a
a = b
b = temp

print("After swap a: ", a)
print("After swap b: ", b)


# In[ ]:





# In[39]:


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

a = a+b
b = a-b
a = a -b

print("After swap a: ", a)
print("After swap b: ", b)


# In[ ]:





# In[40]:


basic = int(input("Enter basic salary: "))

da = 0.40 * basic
hra = 0.20 * basic
gross = basic + da + hra

print("Gross salary: ", gross)


# In[ ]:





# In[41]:


km = int(input("Enter distance in km: "))

meters = km * 1000
feet = meters * 3.33
inches = feet * 12
cm = meters * 100

print("Meters: ", meters)
print("Feet: ", feet)
print("Inches: ", inches)
print("CM: ", cm)


# In[ ]:





# In[42]:


days = int(input("Enter days: "))

years = days // 365
days = days % 365
months = days // 30
days = days % 30

print("Years: ", years)
print("Months: ", months)
print("Days: ", days)


# In[ ]:





# In[44]:


price = int(input("Enter price: "))
d = 0.23 * price
print("Depreciation: ", d)


# In[ ]:





# In[45]:


sale = int(input("Enter sale amount: "))
disc = 0.075 * sale
print("Discount: ", disc)


# In[ ]:





# In[46]:


b_s = float(input("Enter base salary: "))
qty = float(input("Enter quantity: "))
price = float(input("Enter price: "))

total_amt = qty * price
bonus = 0.125 * total_amt
commission = 0.085 * total_amt
gross_salary = b_s + bonus + commission

print("Gross salary: ", gross_salary)


# In[ ]:





# In[47]:


n = float(input("Enter number: "))

x = int(n)
y = int((n - x) * 100)

print("x: ", x)
print("y: ", y)


# In[ ]:





# In[48]:


n = int(input("Enter number: "))
right_digit = int(n) % 10
print("Right most digit: ", right_digit)


# In[ ]:





# In[49]:


n = float(input("Enter number: "))
td = int(n) % 100
print("Right most two digits: ", td)


# In[ ]:





# In[50]:


l = float(input("Enter length: "))
b = float(input("Enter breadth: "))
h = float(input("Enter height: "))
area = l * b * h
print("Area: ", area)


# In[ ]:




