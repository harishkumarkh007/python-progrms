Write a program to find the factorial of a number.


num=int(input("ener he numer:"))
fact= 1
for i in range(1,num+1):
    fact=fact*i

print("factorial is :",fact)


Write a program to find the sum of digits of a number.

num = int(input("ener he numer:"))
sum=0

while num>0:
    digi=num%10
    sum=sum+digi
    num=num//10
print("sum is:",sum)



Write a program to count the number of digits in a number.

num = int(input("ener he numer:"))

count=0
while num>0:
    digi = num%10
    count=count+1
    num=num//10

print(count)


Write a program to reverse a number.

num=int(input("ener he numer:"))
rev=0

while num>0:
    digi =  num%10
    rev= rev*10+digi
    num=num//10
print("reverse no:",rev)


Write a program to check whether a number is a palindrome.


num = int(input("ener henumer:"))
rev=0
originl=num
while num>0:
     digi =  num%10
     rev= rev*10+digi
     num=num//10
if originl==rev:
     print("plindrome")
else:
     print("no plindrome")


Write a program to check whether a number is an Armstrong number.
 

num=int(input("ener he numer:"))
sum=0
originl=num
while num>0:
    digi=num%10
    sum=sum+digi**3
    num=num//10
if originl==sum:
    print(" Armstrong number")
else:
    print("no Armstrong number")



Write a program to check whether a number is a prime number.

num=int(input("ener  numer:"))
for i in range(2,num+1):
    if num%i==0:
     print("no prime numer")
     break
else:
    print("prime numer")


Write a program to print all prime numbers between 1 and 100.
    
start = int(input("Enter start: "))
limit = int(input("Enter limit: "))

count = 0

for num in range(start, limit + 1):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            count += 1

print("Total prime numbers:", count)



Count the number of factors of a given number


num = int(input("Enter a number: "))
count = 0

for i in range(1, num + 1):
    if num % i == 0:
        count += 1

print("Number of factors:", count)

. Find the sum of all factors of a number


num = int(input("Enter a number: "))
total = 0

for i in range(1, num + 1):
    if num % i == 0:
        total = total + i

print("Sum of factors:", total)









