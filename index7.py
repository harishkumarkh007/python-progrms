# roll_no=[101,102,103,104,105]
# print(roll_no)
# print(roll_no[0])
# print(roll_no[-1])

# print(len(roll_no))
# print(roll_no==[])
# print(not roll_no)
# print()



# print(roll_no==[])
# # empty lis is considerd as False
# so not False is True

# roll_no[0]=200
# print(roll_no)



# roll_no.append(106)
# print(roll_no)


# roll_no.insert(3,500)
# print(roll_no)


# x=roll_no.remove(101)
# # print(x)//remove fucnion returns no value
# print(roll_no)



# x1=roll_no.pop()
# # print(x1)//pop funcio eurn vlues
# print(roll_no)

# roll_no.pop()
# print(roll_no)



# roll_no.clear()
# print(roll_no)



# ---------------------------------------------


# marks=[10,20,30,40,50]

# x1=sum(marks)
# print(x1)


# vg=x1/len(marks)
# print(vg)


# lrgs=marks[0]
# smmles=marks[0]

# for mrk in marks:
#     if mrk>lrgs:
#         lrgs=mrk
#     if mrk<smmles:
#         smmles=mrk
# print(lrgs)
# print(smmles)

# numers=[1,2,3,4,5]
# prod=1

# for i in numers:
#     prod=prod*i
# print(prod)



# odd_cou=0
# even_coun=0
# for i in numers:
#     if i%2==0:
#         even_coun +=1
#     else:
#         odd_cou +=1
# print(even_coun)
# print(odd_cou)


# numers=[1,2,3,4,5]
# numers.reverse()
# print(numers)



# numers1=[1,2,3,4,5]
# reversed=numers1[::-1]
# print(numers1)
# print(reversed)


# numers=[1,2,6,4,3,7,5]
# numers.sort()
# print(numers)
# numers.sort(reverse=True)
# print(numers)
# new_lis=sorted(numers)
# print(numers)
# print(new_lis)


# fruis_originl=['apple','mango','orange']
# fruis_copy= fruis_originl.copy()
# fruis_copy.append('kiwi')
# print("originl:",fruis_originl)
# print("copy :",fruis_copy)

# num=[1,2,3]

# fruits=["kiwi","mango","coconut"]

# combined_batch = num + fruits
# print(combined_batch)
# print()

# x=num.extend(fruits)
# print(x)
# print(num)


# nums=[1,2,3]
# nums1=[5,6]
# nums.append(nums1)
# # nums.extend(nums1)
# print(nums)



# c=(5)
# print(c)
# print(type(c))

# print()
# print()


# d=(5,)
# print(d)
# print(type(d))

# e=10,20,30
# print(e)
# print(type(e))

# output=(10,20,30)

# is clled  tuple packing


# e=10,20,30
# print(e)
# print(type(e))

# print()

# print(e[1])
# print(e[-1])

# print(e[1:3])



# prgm_lngue=("java","c","ruby","js","kotlin")
# print(prgm_lngue[0])
# print(prgm_lngue[-1])
# print()
# print()
# lenh=len(prgm_lngue)
# middle_index=lenh//2
# middle_word=prgm_lngue[middle_index]
# print(prgm_lngue[middle_index-1],prgm_lngue[middle_index],prgm_lngue[middle_index+1])




# nums = (1,2,3,4,5,7,3,2)
# # print(nums.count(2))
# # print(nums.count(3))
# # print(nums.count(7))
# # print(nums.count(9))

# print(nums.index(2))///reurn fis mching posiion


# suden=("jino","kiwi","jeslin")
# print(suden)
# print()
# suden_lis=list(suden)
# print(suden_lis)


# suden = (
# ("kiwi",4,3),
# ("jeslin",5,6)
# )
# print(suden[1][0])
# print(suden[0][2])



# sudn = ("jino",[3,4])
# # print(sudn)
# sudn[1].append(3)
# print(sudn)


# suden ={
# (1,"kiwi"):"pyon",
# (2,"joe"):"c++",
# (3,"mnu"):"js"

# }
# print(suden[(1,"kiwi")])




# e={}
# f=set()
# print(type(e))
# print(type(f))

# colors = {"RED","green","blue"}
# print(type(colors))
# for color in colors:
#     print(color)
# colors.add("yellow")
# print(colors)

# colors.update(["ornge","pink","black"])
# print(colors)

# colors.remove("pink")
# print(colors)

# colors.discard("whie")
# print(colors)

# removed=colors.pop()
# print(colors)
# print(removed)


# colors.clear()
# print(colors)

# print("RED" in colors)
# print("WHITE" in colors)


#------------------------------------

# batch05 = {"pawan","edwi","joshw","jax"}
# batch06 = {"jax","kiwi","nndn"}
# batch0506=batch05|batch06
# print(batch0506)


# batch0506=batch05.union(batch06)
# print(batch0506)

# resul = batch06.difference(batch05)
# print(resul)

# resul = batch06.symmetric_difference(batch05)
# print(resul)


# resul = batch06.symmetric_difference_update(batch05)
# print(resul)

#-------------------------------------------------
# forzenset


# colors={"RED","green","blue"}
# freezed_colors=frozenset(colors)
# freezed_colors.add("yellow")
# print(freezed_colors)



# batch={
#     frozenset({"anu","bhaya"}):"batch05",
#     frozenset({"jose","karthi"}):"batch05"
# }
# print(batch[frozenset({"anu","bhaya"})])


# student = {
# "name" :"hello",
# "name" : "kiwi",
# "age"  : 22,
# "course" : "Python",
# "email":"hello.com"
# }
# print(student)


# student1 = {}
# print(student1)


# print(type(student1))


# print(student["name"])
# print(student["course"])
# print(student["mon"] ==key error


# student["email"]="kiwi.com"
# print(student)

# student.update(
#     {

#      "mark":91,
#      "city":"cheeni"
#     }
#  )
# print(student)


# student.pop("mark")
# print(student)

# student.popitem()
# print(student)

# student.clear()
# print(student)

# print(student.keys())
# print(student.values())


# for key in student:
#     print(key)
# print()
# for value in student.values():
#     print(value)

print()
print()

print()


# for key,value in student.items():
#     print(key,":",value)


# print()
# print()

# print()


# print(22  in student.values())






# students = {
#     "student1": {
#         "name": "Jeslin",
#         "age": 22,
#         "course": "python"
#     },

#     "student2": {
#         "name": "Ansa",
#         "age": 21,
#         "course": "java"
#     }
# }

# print(students)


# data = {
#     1:"one",
#     "two":2,
#     (3,4):"3 nd 4"
# }

# print(data[1])





# modulues nd pckges 

-














