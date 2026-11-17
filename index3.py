# marks = 75

# if marks >= 90:
#     print("Grade A")
# elif marks >= 75:
#     print("Grade B")
# elif marks >= 50:
#     print("Grade C")
# else:
#     print("Fail")


# marks=90
# if marks >= 50:
#     print("Grade C")
# elif marks >= 75:
#     print("Grade B")
# elif marks >= 90:
#     print("Grade A")
# else:
#     print("fail")

# for i in range(5):
#         print("Hello")



# for i in range(5):
#     print(i)

# n = 1234
# count = 0

# while n > 0:
#     n = n // 10
#     count += 1

# print("Number of digits:", count)


# num=1234
# count=0
# while(num>0):
#     emp=num%10
#     count=count+1
#     num=num//10
# print(count)


Customer_Name=input("enter the Customer Name: ")
Food_Item_Name=input("enter the  Food Item Name: ")
Quantity=int(input("enter the Quantity: "))
Price_Per_Item=float(input("enter the Price_Per_Item:"))
Delivery_Distance = float(input("enter the  Delivery Distance in KM:"))
print("--------------------------------------------------------------")
print("---------------------ORDER DETAILS---------------------------")

print("Customer Name:",Customer_Name)
print(type(Customer_Name))
print("Memory Address:",id(Customer_Name))

print()

print("Food Item:",Food_Item_Name)
print("Type",type(Food_Item_Name))

print()

print("Quantity:",Quantity)
qty=float(Quantity)
print("Type:",type(qty))

print()


print("Price Per Item:",Price_Per_Item)
print("Type",type(Price_Per_Item))

print()



total_food_cost = Quantity*Price_Per_Item
Delivery_Charge = int(input("Enter Delivery Charge: "))
print()
Final_Bill_Amount= total_food_cost + Delivery_Charge
print("Final Bill Amount:",Final_Bill_Amount)
print("Type:",type(Final_Bill_Amount))

print()
print("Checking Data Types:")
print("Quantity is integer:",isinstance(Quantity,int))
print("Price is float:",isinstance(Price_Per_Item,float))
print("Price is float:",isinstance(Final_Bill_Amount,float))