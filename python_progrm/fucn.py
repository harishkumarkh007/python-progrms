# def welcome():
#     print("welcome...!")

# welcome()
# welcome()

# Find the square of a number

# num = int(input(" ener henumer:"))
# def squre(num):
#     return num*num

# resul = squre(num)
# print(resul)


# Check even or odd


# num= int(input("enter the number:"))

# def odd_or_even(num):
#     if num%2==0:
#         return "no is even"
#     else:
#         return "no is odd"

# resul = odd_or_even(num)
# print(resul)


# 4. Find the largest of two numbers


# a= int(input("enter the number1:"))
# b = int(input("enter the number2:"))

# def  largest(a,b):
#     if a>b:
#         return a,"igger"
#     elif a==b:
#         return  "both are same"
#     else:
#         return b

# reslt=largest(a,b)
# print(reslt)


# num=int(input("enter the number:"))
# def factorial(num):
#     fact=1
#     for i in range(1,num+1):
#         fact=fact*i
#     return fact
# result = factorial(num)
# print(result)


# num1=int(input("enter the number:"))
# count = 0
# while num1>0:
#     digit = num1%10
#     count = count+1
#     num1 = num1//10

# print("no of digit",count)

# num1=int(input("enter the number:"))
# def count_no_digit(num1):
#     count = 0
#     while num1>0:
#      digit = num1%10
#      count = count+1
#      num1 = num1//10
#     return count
# resul =  count_no_digit(num1)
# print(resul)


# num1=int(input("enter the number:"))
# count = 0
# while num1>0:
#     digit= num1%10
#     count=count+digit
#     num1=num1//10
# print(count)


# num1=int(input("enter the number:"))
# def sum_digit(num1):
#     count = 0
#     while num1>0:
#         digit = num1%10
#         count = count+digit
#         num1 = num1//10
#     return count
# result = sum_digit(num1)
# print(result)



# num1=int(input("enter the number:"))
# rev = 0
# while num1>0:
#     digit = num1%10
#     rev = rev*10 + digit
#     num1 = num1//10
# print(rev)


# num1=int(input("enter the number:"))
# def reverse_num(num1):
#     rev = 0
#     while num1>0:
#         digit = num1%10
#         rev = rev*10+digit
#         num1 = num1//10
#     return rev
# result = reverse_num(num1)
# print(result) 


# num1=int(input("enter the number:"))
# original =  num1
# rev= 0
# while num1>0:
#     digit = num1%10
#     rev = rev*10+digit
#     num1 = num1//10

# if original==rev:
#     print("palindrome")
# else:
#     print("not palindrome ")





# x = 10

# def change():
#     global x
#     x = 20
#     print(x)
# change()

# print(x)



# def outer():
#     x = 10
#     def inner():
#         x = 50
#     inner()
#     print(x)
# outer()


def test():
    nonlocal x
    x = 20