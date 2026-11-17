# num= int(input("ener no:"))
# f=1
# i=1
# while i<=num:
#     f=f*i
#     i=i+1
# print("factorial of ",f)

----------------------------------------------------

num = int(input("enter the number:"))
if num>0:
    print("number is positive")
elif num==0:
    print("number is zero")
else:
    print("number is negative")



--------------------------------------
num = int(input("enter the number:"))
if num%2==0:
    print("number is even")
else:
    print("number is odd")


-----------------------------------------

age= int(input("enter the age:"))
if age>18:
    print("eligible to vote")
elif age==18:
    print("eligible to vote")
else:
    print("not eligible to vote")


------------------------------------------


num1=int(input("enter the first number:"))
num2=int(input("enter the second number:"))
if num1 > num2:
    print(num1,"is larger")
elif num1==num2:
    print(num1,"and",num2,"are equal values")
else:
    print(num2,"is larger")



--------------------------------------------

num1=int(input("enter the first number:"))
num2=int(input("enter the second number:"))
if num1 > num2:
    print(num2,"is smaller")
elif num1==num2:
    print(num1,"and",num2,"are equal values")
else:
    print(num1,"is smaller")


-------------------------------------------

num1=int(input("enter the first number:"))
num2=int(input("enter the second number:"))
num3=int(input("enter the third number:"))

if num1>num2 and num1>num3:
    print(num1,"is larger")
elif num2>num1 and num2>num3:
    print(num2,"is larger")
else:
    print(num3,"is larger")


------------------------------------------


num1=int(input("enter the first number:"))
num2=int(input("enter the second number:"))
num3=int(input("enter the third number:"))

if num1<num2 and num1<num3:
    print(num1,"is smaller")
elif num2<num1 and num2<num3:
    print(num2,"is smaller")
else:
    print(num3,"is smaller")


-------------------------------------

year=int(input("enter the year:"))

if year%400==0:
    print(year,"is a leap year")
elif year%4==0:
        print(year,"is a leap year")
elif year%100==0:
        print(year,"not a leap year")
else:
       print(year,"not a leap year")



------------------------------------------------



print("passing mark is:65")

mark = int(input("enter the mark::"))


print()
if mark>65:
    print(" student has passed")
elif mark==65:
        print(" student has passed")
else:
          print(" student has failed")


--------------------------------------------------



print("90 or above:A+")
print("85 to 89  :A")
print("70 -80:B+")
print("65-70:D")
print("less than 65:Failed")


sub1=int(input("enter first mark:"))

if sub1>90:
    print("A+")
elif sub1>=85 and  sub1 <=89:
    print(A)
elif sub1>=70 and sub1<=80:
    print("B+")
elif sub1 >65 and sub1 <=70:
    print("D")
else:
    print("failed")


-------------------------------------------------


age = int(input("enter the age:"))
if age>=18:
    print(" person is eligible for a driving licence")
else:
        print(" person is not eligible for a driving licence")



-----------------------------------------------------------




num=int(input("enter the number:"))
if num%5==0 and num%10==0:
    print(num,"is  divisible by both 5 and 10.")
else:
    print(num," is not divisible by both 5 and 10.")



-----------------------------------------------------------


num=int(input("enter the number:"))
if num%3==0 and num%7==0:
    print(num,"is  divisible by both 3 and 7.")
else:
    print(num," is not divisible by both 3 and 7.")



-------------------------------------------------------------

char=input("enter the character ")
vowel=['a','e','i','o','u']
if char in vowel:
    print( char,"is vowel")
else:
        print( char,"is consonant")


---------------------------------------------------------------------


num=int(input("enter the no:"))
if num>=10 and num<=99:
    print("2 digit number")

else:
    print("not a 2 digit number")





    
