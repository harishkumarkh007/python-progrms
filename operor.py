#  Shopping Bill — Addition

# shirt=800
# shoes=1200
# total=shirt+shoes
# print("The Total sum is: ",total)

# -------------------------------
# Bank Balance — Subtraction

# person=10000
# drw=2500
# balance=person-drw
# print("The remaining balance is :", balance)

# ----------------------------
# Movie Tickets

# ticket_costs=250
# no_of_members=4
# total_cost=ticket_costs*no_of_members
# print(" total amount of ticket:  ",total_cost)

# ------------------------------
# Sharing a Restaurant Bill

# bill=1500
# no_of_frnds=4
# ech_cut=bill/no_of_frnds
# print("ech should pay:",ech_cut)

# -------------------------------
# Packing Chocolates

# No_of_choclte = 53
# a_box= 10
# complete_box=No_of_choclte//a_box
# remaining_choclate=No_of_choclte%a_box
# print("complete no  of boxes:",complete_box)
# print("remaining no of choleae",remaining_choclate)

# ------------------------------------------
# Convert Minutes into Hours and Minutes


# complee_hour=145//60
# reminig_minies=145%60
# print(complee_hour)
# print(reminig_minies)


# ------------------------------------------
#  Even or Odd —

# num=int(input("ener  numer"))
# if  num%2 == 0:
#     print("num is even")
# else:
#     print("num is odd")


# ------------------------------------------
# Area of a Square

# s=5
# A=s**2
# print("area of the square is",A)


# ------------------------------------------
# Adding Money to a Wallet

# wallet=500
# wallet = wallet+200
# print("new balance is",wallet)


# ------------------------------------------
# Exam Pass Check

# passmark=40
# stdscore=65
# if stdscore > 40:
#     print(" student's mark is greater thanthe passing mark.")
# elif stdscore == 40:
#         print(" student's mark is  equal to the passing mark.")
# else:
#       print("less thn pass mark")


# -------------------------------------------------
# Password Matching

# name = input("enter the password:")
# stored_password = "hello"
# if stored_password == name:
#     print("password mached")
# else:
#     print("password not maching")
      

# -------------------------------
# Stock Availability

# Stock_count=int(input("enter the count"))
# if Stock_count!=0:
#     print("stock is present")
# else:
#     print("stock is not present")


# -------------------------------
# Driving Licence Eligibility


# age = int(input("ener the age"))
# test_pass=int(input("enter the pass status( test_pass=0{fail},,test_pass=1{pass})"))

# if (age>=18)and(test_pass==1):
#     print("eligile for lisence")


# elif age >= 18 and (test_pass==0):
#     print("not eligile foe lisece")
# else:
#     print("not eligile foe lisece")


# ------------------------------
# Weekend Check — or


# day = input('enter the day ::')
# if day=="saturday"or day=="sunday":
#     print("its a weekened")
# else:
#     print("its not a weekened")


# --------------------------------------
# Online Shopping Free Delivery — or


# price=int(input("enter the price:"))
# membership=input("enter the membership:")
# if price >=1000 or membership== "premium":
#     print("customer get free delevry")
# else:
#     print("customer doesn't get free delevry")
      

# -----------------------------------------
# Account Access — not


# blocked = input("is the accound blocked {yes/no}:")
# if not (blocked=='yes'):
#     print('access granted')
# else:
#     print("not granted")


# -----------------------------
# Job Eligibility


# age=24
# graduated=input("are you graduated {yes/no}:")
# banned=input("are you banned{yes/no}: ")

# if age>=21 and graduated=="yes" and not(banned=="yes"):
#     print("eligile for job")
# else:
#      print("not eligile for job")\


# -------------------------------------------------
# Restricted Username — not in


# # Restricted Username — not in
# user_name=input("enter the user name::")
# blocked_names = ["admin", "root", "system"]
# if user_name is not  blocked_names:
#     print("Restricted Username")
# else:
#     print(" it's unRestricted Username")


# ------------------------------------
# Check Product Availability — in


# Name="laptop"
# products = ["Laptop", "Mobile", "Tablet", "Headphones"]
# if Name  in products:
#     print("product is availale")
# else:
#     print("Product Availabile")


# ----------------------------
# Membership with Strings


# sym="@"
# email = "student@gmail.com"
# if sym in email:
#     print("@ in email")
# else:
#     print("@ not in email")

# ---------------------------------
# Online Shopping Checkout

# Product_price = 1200
# list=["Laptop", "Mobile", "Tablet", "Headphones"]
# Quantity = 3
# Discount = 500
# amount = Product_price *Quantity
# f_amount = amount-Discount

# if f_amount>=2000 or  "Laptop" in list:
#     print("eligile for free delivery")
# else:
#         print("not eligile for free delivery")


# #---------------------------------------------
# Write a program to create a new string made of an input string’s first, middle, and last characters.

# Given Input: str1 = "James"
# Expected Output: Jms


# str1=input("ener he sring:")
# length=len(str1)
# firs_chr=str1[0]
# ls_chr=str1[-1]
# middle_index=length//2
# middle_chr=str1[middle_index]
# nw_sr=firs_chr+middle_chr+ls_chr
# print()
# print("originl string:",str1)
# print("new string:",nw_sr)


# ----------------------------------------------------------------------

# Write a program to create a new string made of the middle three characters of an input string of odd length
# Given Input: 
# str1 = "JhonDipPeta"
# Expected Output: Dip


# str1=input("ener he sring:")
# length=len(str1)
# middle_index = length//2
# middle_char=str1[middle_index]
# nxt_char=str1[middle_index+1]
# prevoius_char=str1[middle_index-1]
# new_sring=prevoius_char+middle_char+nxt_char
# print("originl sring:",str1)
# print("new sring:",new_sring)


# ----------------------------------------------------------------------------------------

# Given two strings, s1 and s2, create a new string by appending s2 in the middle of s1.
# Given Input:
#  s1 = "Ault" s2 = "Kelly"
# Expected Output: AuKellylt


# s1=input("ener he sring 1:")
# s2=input("ener he sring 2:")
# mid=len(s1)//2
# print()
# print(s1)
# print(s2)
# print()
# print(s1[:mid]+s2+s1[mid:])



# -------------------------------------------------------------
# Given two strings, s1 and s2, create a new string from the first, middle, and last characters of each input string.

# Given Input:
# s1 = "America" s2 = "Japan"

# Expected Output: AJrpan



# s1 = "America"
# s2 = "Japan"

# result = s1[0] + s2[0] + s1[len(s1)//2] + s2[len(s2)//2] + s1[-1] + s2[-1]

# print(result)

# --------------------------------------------------------------


# Write a program to reverse a given string.

# Given Input:
# str1 = "PYnative"

# Expected Output: evitanYP



# str1=input("ener hesring")
# # reverse=str1[::-1]
# # print("originl sing is:",str1)
# # print()
# # print("reversed sring:",reverse)


# without slicing

# sore=""


# for i in str1:
#     sore=i+sore
# print(sore)

# ----------------------------------------------------------------------------------------
    

# Write a program to find the last index of the substring “Emma” in a given string.

# Given Input:
#  str1 = "Emma is a data scientist who knows Python. Emma works at google."
# Expected Output:
#  Last occurrence of Emma starts at index 43

# str1 = "Emma is a data scientist who knows Python.Emma works at google."
# index = str1.rfind("Emma")
# print(f"Last occurrence of Emma starts at index {index}")



# -------------------------------------------------------------------------
# Write a program to split a given string on hyphens and display each substring.

# Given Input: str1 = "Emma-is-a-data-scientist"

# Expected Output:

# Displaying each substring: 
# Emma
# is
# a
# data
# scientist

# str1 = "Emma-is-a-data-scientist"
# words = str1.split("-")

# #[Emma,is,a,data,scientist]
# print("Displaying each substring:")
# for word in words:
#     print(word)



# ---------------------------------------------
# Write a program to find the total count of the substring “USA” in a given string, ignoring the case (i.e., both “usa” and “USA” should be counted).

# Given Input: str1 = "Welcome to USA. usa awesome, isn't it?"

# Expected Output: The USA count is: 2



# str1 = "Welcome to USA. usa awesome, isn't it?"
# str1 = str1.lower()
# coun=str1.count("usa")
# print("The USA count is:",coun)



# ------------------------------------------------

#  Write a program to count the total number of vowels (a, e, i, o, u) in a given string.

# Given Input: str1 = "Hello World"

# Expected Output: Vowel Count: 3


# str1 = "Hello World"
# str1=str1.lower()
# coun = 0
# for ch in str1:
#     if ch=="a" or  ch=="e" or  ch=="a" or  ch=="i" or  ch=="o" or  ch=="u":
#         coun = coun+1


# if coun>0:
#     print("Vowel Count:",coun)
# else:
#     print(" no Vowel ")



#-----------------------------------------------------------------------


# Write a program to check if two strings are balanced. For example, strings s1 and s2 are balanced if all the characters in s1 are present in s2. The character’s position doesn’t matter.

# Given Input:

# Case 1: s1 = "yn", s2 = "PyNative"
# Case 2: s1 = "ynf", s2 = "PyNative"

# Expected Output:

# Case 1: True
# Case 2: False

# s1 = "yn"
# s2 = "PyNative"

# result = True

# for char in s1:
#     if char not in s2:
#         result = False
#         break

# print(result)

#---------------------------------------------------

# 11)Check if a given URL starts with “https” and ends with “.com”.

# Given Input: str1 = "https://google.com"

# Expected Output:

# Is valid URL: True

# str1 = "https://google.com"

# if str1.startswith("https") and str1.endswith(".com"):
#     print("Is valid URL: True")
# else:
#     print("Is valid URL: False")

#----------------------------------------------

# Write a program to toggle the case of all characters in a string (uppercase becomes lowercase and vice versa).

# Given Input: str1 = "PyThOn"

# Expected Output: pYtHoN


# str1 = "PyThOn"

# result = str1.swapcase()

# print(result)


# def even_odd(n):
#     if n & 1==0:
#         return "even"
#     else:
#         return"odd"
# Res=even_odd(5)
# print(Res)



# def mul(n,i=1):
#     if n>10:
#         return 0
#     if i>10:
#         return 0
    
#     print("5 *",i,"=",n*i)
#     return mul(n,i+1)

    
# Res=mul(5)
# print(Res)

