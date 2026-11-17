# 1)Print all elements of an array.

# num=[10,20,30,40]
# print(num)

# ----------------------------------

# 2)Find the sum of all elements.

# num=[10,20,30,40,50]

# resul=sum(num)
# print(resul)

#-------------------------------------

# 3)Find the average of array elements.

# num=[10,20,30,40,50]

# average=sum(num)/len(num)
# print(average)

#---------------------------------

# 4)Find the largest element


# num=[50,10,90,20,30]
# # largest=max(num)
# # print(largest)
# largest = num[0]
# for i in num:
#     if i>largest:
#         largest=i
# print("largest:",largest)


# 5)Find the smallest element.

# num=[50,10,90,20,30]
# # smallest=min(num)
# # print(smallest)
# smallest=num[0]
# for i in num:
#     if i<smallest:
#         smallest=i
# print(smallest)


# 6)Count even and odd numbers.

# num=[10,2,5,6,88,9]
# even_coun=0
# odd_coun=0
# for i in num:
#     if i%2==0:
#         even_coun=even_coun+1
#     else:
#         odd_coun=odd_coun+1
# print("even coun",even_coun)
# print("odd coun",odd_coun)


# 7)Count positive and negative numbers.

# num=[1,6,-1,6,-4,4,9,-2]
# coun_posi=0
# coun_neg=0
# for i in num:
#     if i>=0:
#         coun_posi+=1
#     else:
#         coun_neg+=1
# print("posiive  no",coun_posi)
# print("negive no",coun_neg)

#8)Search for an element

num=[10,23,45,87,34]
elemn=23
# for i in num:
#     if i==elemn:
#      print("elemn presen")
#      break
# else:
#    print("no found")

# for i in range(len(num)):
#     if num[i]==elemn:
#      print(f"elemn presen index {i}")
#      break

# else:
#      print("no prensen")



#9)Count how many times an element occurs.
# num=[1,23,1,6,1,3,1,2,3]
# elemn=1
# coun=0
# for i in num:
#     if i==elemn:
#         coun+=1

# if coun>0:
#     print("elemen found")
# else:
#     print("no found")
 
# print(f"occurence {coun} imes")



# 10)second lrges elemen


# num=[10,2,67,58,345]

# lrges=float('-inf')
# second_lrges=float('-inf')

# for i in num:

#     if i>lrges:
#         second_lrges=lrges
#         lrges=i
#     elif i>second_lrges and i<lrges:
#         second_lrges=i
# print("second lrges:",second_lrges)



# 11)Print All Factors of a Given Number

# num=int(input("ener he numer:"))

# # resul=[]

# # for i in range(1,num+1):
# #     if num%i==0:
# #         resul.append(i)
# # print("fcorsis",resul)


# for i in range(1,num+1):
#     if num%i==0:
#         print(i)





# nums = [5, 6, 7, 7, 1, 9, 11, 1, 1, 5, 1, 1]

# freq_map = {}

# for i in range(len(nums)):

#     if nums[i] in freq_map:
#         freq_map[nums[i]] += 1

#     else:
#         freq_map[nums[i]] = 1

# print(freq_map)






# num=[10,20,10,30,20,20,40,50]

# freq={}

# for i in num:
#     if i in freq:
#         freq[i]+=1

#     else:
#         freq[i]=1

# print(freq)


# num =[10,20,30,48,10,10,40]

# target=10

# count=0

# for  i in num:
#     if i==target:
#         count+=1


# if count>0:
#     print("target found")

# else:
#     print('no found')
# print(f"occurnce of {target} is {count}")
















