# import  calendar
# year = int(input("ner year:  "))
# month = int(input("ener month: "))

# print(calendar.month(year,month))



# def  fcoril(num):
#     if num==1:
#         return 1
#     return num*fcoril(num-1)
# print(fcoril(5))



# def numers(n):
#     if n==0:
#      return  


#     numers(n-1)
#     print(n)
# numers(5)


# def sum(n):
#     if n==0:
#      return 0

#     return n + sum(n-1)
# print(sum(5))

# n = int(input("Enter number of terms: "))

# a, b = 0, 1

# for i in range(n):
#     print(a, end=" ")
#     a, b = b, a + b


# def fibonacci(n):
#     if n <= 1:
#         return n

#     return fibonacci(n - 1) + fibonacci(n - 2)
# num=int(input("ener he  num:"))
# for i in range(num):
#     print(fibonacci(i), end=" ")



# x = 10

# def test():
#     global x
#     x = 30

# test()
# print(x)


# x = 10

# def change():
#     global x
#     x = 50

# change()
# print(x)



# def outer():
#     x = 10
#     def inner():
#         print(x)
#     inner()

# def outer():
#     x = 1
#     def inner():
#         nonlocal x
#         x += 1
#     inner()
#     inner()
#     print(x)

# outer()


# def outer():
#     x = 10
#     def inner():
#         print(x)
#     x = 25
#     inner()

# outer()



# x = 10

# def test():
#     global x
#     x = 40
#     print(x)

# test()
# print(x)




# def delivery(price, charge=50):
#     return price + charge

# print(delivery(500, 100))



# def employee(**details):
#     print(details["department"])

# employee(name="Harish", department="IT")



sring=input("ener he sring:")

print("originl sring is:",sring)


lengh=len(sring)
index_of_middle=lengh//2

middle_chrcer=sring[index_of_middle]
firs_chrer=sring[0]
ls_chrcer=sring[-1]
new_sring=firs_chrer+middle_chrcer+ls_chrcer
print("new sring is:",new_sring)