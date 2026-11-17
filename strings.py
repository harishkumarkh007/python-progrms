#--------------- set---------------
# sed={
#     1,3,4,1
# }
# print(sed)



# sr="PytHoN"
# resul=sr.swapcase()
# print(resul)


# sr = "PytHoN"
# resul = " "
# for ch in sr:
#     if ch.isupper():
#         resul=resul+ch.lower()
#     else:
#         resul=resul+ch.upper()
# print(resul)




# str1 = " P y t h o n "
# resul=" "
# for i in str1:
#     if i!=" ":
#         resul=resul+i
# print(resul)



# sr=input("ener he sring:")
# i=int(input("ener he index u wn o remove :"))
# resu=sr[:i] +  sr[i+1:]
# print(resu)


# sr=input("ener he sring:")
# i=int(input("ener he index u wn o remove :"))
# resul=""
# for ch in range(len(sr)):
#     if ch!=i:
#         resul+=sr[ch]
# print(resul)




# file_name = "report_final_v2.pdf"

# result = file_name.split(".")

# print(result[-1])

# str1 = "PyNaTive"
# upper=""
# lower=""

# for ch in str1:
#     if ch.isupper():
#         upper=upper+ch
#     else:
#         lower=lower+ch
# resul=lower+upper
# print(resul)


# str1 = "P@#yn26at^&i5ve"
# alpha = 0
# num = 0
# specil = 0

# for ch in str1:
#     if ch.isalpha():
#         alpha+=1
#     elif ch.isdigit():
#         num+=1
#     elif not ch.isalnum() and not ch.isspace():
#         specil+=1 

# print(f"Total counts of chars, digits, and symbols: Chars = {alpha} Digits = {num} Symbol ={specil}") 



# str1 = "PYnative29@#8496"
# str2=int(str1)
# num=""
# for ch in str2:
#     if ch.isdigit():
#         num+=ch

# sum_no=sum(num)
# avg=sum_no//len(num)
# print(sum_no)
# print(avg)


# s1="Abc"
# s2="Xyz"

# resul = ""

# for i in range(len(s1)):
#     resul  +=s1[i]
#     resul  +=s2[-(i+1)]
# print(resul)




# str1 = "PYnative29@#8496"


# resul  = " "
# leng =len(str1)

# for i in str1:
#     if i.isdigit():
#         resul+=i
# summ=sum(resul)
# avg=summ//leng
# print(summ)
# print(avg)




# 


str1 = "/*Jon is @developer & musician!!"
resul =  " "

for i in str1:
    if i.isalnum()  or i ==" ":
        resul+=i
print(resul)
