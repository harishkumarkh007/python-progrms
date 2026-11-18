
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





# def sor(numers):
#     n = len(numers)
#     for i in range(n):
#         for j in range(n-i-1):
#             if numers[j]>numers[j+1]:
#                 numers[j],numers[j+1] = numers[j+1],numers[j]

#     return numers


# numers = [9,3,4,1,7]

# resul  = sor(numers)
# print(resul)


# def sor(numers):
#    numers.sort()
#    return numers


# numers=[6,2,3,9,1,0]

# resul = sor(numers)
# print(resul)





# def merge_lis(p,q):
#     p.extend(q)
#     return p

# list_a = ["Physics", "Chemistry"]
# list_b = ["Maths", "Biology"]

# resul = merge_lis(list_a,list_b)
# print(resul)



# Given a list, extract a “slice” containing the middle three elements.

# Given Input: List: [10, 20, 30, 40, 50, 60, 70]

# Expected Output: Middle Three: [30, 40, 50]



# def lsi(num):
#     p = len(num)
#     middle_index= p//2
#     nx_chr = num[middle_index + 1]
#     midd_chr = num[middle_index]
#     pre_chr = num[middle_index - 1]
#     return pre_chr,midd_chr,nx_chr


# num =  [10, 20, 30, 40, 50, 60, 70]

# prev , middle, next = lsi(num)
# print("Middle Three:",prev , middle, next)




# Find out how many times a specific value appears in a list.

# Given Input:

# List: [10, 20, 30, 10, 40, 10, 50]
# Target: 10
# Expected Output: The number 10 appears 3 times.


# def coun_num(numer,target):
#     count=0

#     for num in numer:
#         if num==target:
#             count+=1
#     return count


# numers = [10, 20, 30, 10, 40, 10, 50]

# target=10

# resul = coun_num(numers,target)
# print(resul)





# 18. Delete every instance of a specific value from a list.

# Given Input:

# List: [5, 20, 15, 20, 25, 50, 20]
# Item to remove: 20
# Expected Output: Cleaned List: [5, 15, 25, 50]




# def dele_iem(numer,iem):
#     resul=[]
#     for num in numer:
#         if num!=iem:
#             resul.append(num)
#     return resul

# numer=[5, 20, 15, 20, 25, 50, 20]
# iem=20
# resulll=dele_iem(numer,iem)
# print(resulll)



# Take a list of strings that contains empty entries ("") and remove them to keep only the valid text.


# Given Input: List: ["Mike", "", "Emma", "Kelly", "", "Brad"]

# Expected Output: Cleaned Names: ['Mike', 'Emma', 'Kelly', 'Brad']




# def remove_iem(list1,target):
#     resul=[]
#     for i in list1:
#         if i!=target:
#             resul.append(i)
#     return resul


# list1=["Mike", "", "Emma", "Kelly", "", "Brad"]
# target=""

# resull=remove_iem(list1,target)
# print(resull)





# Remove all duplicate values from a list while keeping only one instance of each element.

# Given Input: List: [10, 20, 10, 30, 40, 40, 20, 50]

# Expected Output: Unique List: [10, 20, 30, 40, 50]




# def remove_duplic(numers):
#     result=[]
#     for num in numers:
#         if num not in result:
#             result.append(num)
#     return result


# numers = [10, 20, 10, 30, 40, 40, 20, 50]
# resul = remove_duplic(numers)
# print(resul)





# Given a list of integers, use list comprehension to create a new list that contains only the even numbers from the original list.

# Given Input: List: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Expected Output: Even Numbers: [2, 4, 6, 8, 10]



# def even_no(List):
#     result=[]
#     for num in List:
#         if num%2==0:
#             result.append(num)
#     return result

# List=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# resul =  even_no(List)
# print(resul) 










