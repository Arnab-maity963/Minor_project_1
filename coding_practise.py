# # Arithmetic Operation
# a = 10
# b = 20
# a = a + b
# b = a - b
# a = a - b
# print("Arithmetic Operation",a,b)

# # XOR Opeartion
# x = 10
# y = 20
# x = x + y
# y = x - y
# x = x - y
# print("XOR Opeartion",x,y)

# # Tuple Unpacking
# t = 10
# u = 20
# t, u = u,t
# print("Tuple Unpacking",t,u)  ## That is Most Pythonic

# Swiggy Order Calculator
# price = float(input("Enter the price: "))
# quantity = int(input("Enter the quantity: "))
# subtotal = price * quantity
# gst = subtotal * 0.18
# if subtotal < 500:
#     delivery = 40
# else:
#     delivery = 0

# total = subtotal + gst + delivery
# print("Subtotal {:.2f}".format(subtotal))
# print("gst {:.2f}".format(gst))
# print("Delivery {:.2f}".format(delivery))
# print("_" * 25)
# print("total {:.2f}".format(total))

# # Temperature Converter
# temp = float(input("Enter the float value: "))
# unit = input("Enter the unit: ")
# if unit == "C":
#     result = (temp * 9/5) + 32
#     print("Temperature in Fraenheit {:.2f}".format(result))
# elif unit == "F":
#     result = (temp - 32) * 5/9
#     print("Temperature in celcius {:.2f}".format(result))
# else:
#     print("Error ! Invalid Input")

# # Print the Sum Of Digits
# num = int(input("Enter the 4 - number: "))
# d1 = num // 1000
# d2 = (num // 100) % 10
# d3 = (num // 10) % 10
# d4 = num % 10
# total = d1 + d2 + d3 + d4
# print("The sum of digits are = ",total)

# Smart Input Parser
# value = input("Enter a value: ")
# try:
#     num = int(value)
#     print("value",num)
#     print("Type: int")
# except ValueError:
#     try:
#         num = float(value)
#         print("Value",num)
#         print("Type : float")
#     except ValueError:
#         print("Value:",value)
#         print("Type : str")