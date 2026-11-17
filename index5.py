# def square(num):
#     return num ** 2

# print(square(2))
# print(square(5))




# def square(n):
#     """Returns  the square of a number."""
#     return n * n

# # help(square)
# print(square.__doc__)



# def show():
#     x=10
#     print(x)
# show()



# x=10
# def show():
#     x=20
#     print(x)
# show()
# print(x)




# x=10
# def show():
#     global x
#     x=20
#     print(x)
# show()
# print(x)




# def outer():
#     x = "outer"

#     def inner():
#         nonlocal x
#         x = "inner"
#     inner()
#     print("x after  inner():",x)
# outer() 


# def outer():
#     x = 10

#     def inner():
#         nonlocal x
#         x = 20

#     inner()
#     print(x)

# outer()



# L-local
# E-enclosing
# G-global
# B-built-in

# x = "global"
# def outer():
#     x = "enclosing"
#     def inner():
#         # x =  'local'
#         print("inner x:",x)
#     inner()
#     print("outer x:",x)
# outer()
# # print("global x:",x)


# n=int(input("ener no:"))
# def factorial(n):
#     if n==1:
#         return 1
#     else:
#         return n * factorial(n-1)

# resul=factorial(n)
# print(resul)



# n= int(input("ner he no:"))
# def sum_of_num(n):
#     if n==1:
#         return 1
#     else:
#         return n+sum_of_num(n-1)

# resul=sum_of_num(n)
# print(resul)
