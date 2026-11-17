
# def no(n):
#     print(n[2])
#     coun = len(n)
#     print(coun)
#     if coun  !=0:
#         print("False")
#     else:
#         print("True")  

        
         
# numbers = no([10, 20, 30, 40, 50])



# numbers = [100, 200, 300, 400, 500]

# numbers[2]=200
# print("Updated (Change):",numbers)

# # append(), insert(), and remove() modify the original list directly.

# numbers.append(600)
# print("Updated (Append): ",numbers)

# numbers.insert(2,300)
# print("Updated (Insert):",numbers)

# numbers.remove(600)
# print("Updated (Remove 600):",numbers)

# remove_index = numbers.pop(0)
# print("pdated (Remove Index 0):",numbers)


# def sum(num):
#     total = 0
#     for n in num:
#         total +=n
#         avg  = total//len(num)

#     return  total,avg
  

# summ,vre= sum([10, 20, 30, 40, 50])
# print("Sum:",summ)
# print("Average",vre)

# num = [10, 20, 30, 40, 50]

# summ,aver = sum(num)
# print("Sum:",summ)
# print("Average:",aver)


# def max_min(num):
#     lrge = num[0]
#     for i in range(len(num)):
#       if  num[i]>lrge:
#          lrge =  num[i]
#     return lrge


# def min(num):
#     smll = num[0]
#     for i in range(len(num)):
#       if  num[i]<smll:
#          smll =  num[i]
#     return smll




# num=[45, 12, 89, 2, 67]
# maxximum = max_min(num)
# print(maxximum)


# minimum = min(num)
# print(minimum)





# def produc(numbers):
#     prod = 1
#     for i in numbers:
#         prod  *= i
#     return prod 


# numbers = [2, 3, 5, 7]
# product= produc(numbers)
# print("Product: ",product)



# def  odd_even(numbers):
#     odd_coun  = 0
#     even_coun  = 0
#     for i in range(len(numbers)):
#         if i%2==0:
#             even_coun +=1
#         else:
#             odd_coun +=1
#     return even_coun,odd_coun






# numbers = [10, 21, 4, 45, 66, 93, 11]

# odd_count,even_count = odd_even(numbers)
# print("Even numbers:",even_count)
# print("odd numbers:",odd_count)



# def reverse_lis(numbers):
#     rev=[]
#     for i in  numbers:
#         rev.insert(0,i)

#     return rev

# numbers = [100, 200, 300, 400, 500]

# reverse = reverse_lis(numbers)
# print(reverse)







def Sorted_List(numbers):
    a=numbers[0]
    m=numbers[1]
    for i  in numbers:
        if a>numbers[i]:
            p=a
            a=m
            m=p
        return a,m




numbers = [56, 12, 89, 3, 22]

sorted_rr = 














