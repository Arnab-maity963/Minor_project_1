# income = float(input("Enter the income value: "))
# tax = 0
# if income > 300000:
#     tax += min(income - 300000, 400000) * 0.5
# if income > 700000:
#     tax += min(income - 700000, 300000) * 0.10
# if income > 1000000:
#     tax += min(income - 1000000, 200000 ) * 0.15
# if income > 1200000:
#     tax += min(income - 1200000, 300000) * 0.20
# if income > 1500000:
#     tax += min(income - 1500000) * 0.30

# print("Total payable tax",tax)

# Valid PAN Card Number:

# pan = input("Enter PAN number: ")

# # Check length
# if len(pan) != 10:
#     print("Invalid PAN — Length must be exactly 10 characters")

# # Check first 5 uppercase letters
# elif not all('A' <= ch <= 'Z' for ch in pan[:5]):
#     for i in range(5):
#         if not ('A' <= pan[i] <= 'Z'):
#             print(f"Invalid PAN — Character {i+1} must be an uppercase letter")
#             break

# # Check next 4 digits
# elif not all('0' <= ch <= '9' for ch in pan[5:9]):
#     for i in range(5, 9):
#         if not ('0' <= pan[i] <= '9'):
#             print(f"Invalid PAN — Character {i+1} must be a digit")
#             break

# # Check last uppercase letter
# elif not ('A' <= pan[9] <= 'Z'):
#     print("Invalid PAN — Last character must be an uppercase letter")

# # Valid PAN
# else:
#     print("Valid PAN")

# units = int(input("Enter units consumed: "))

# energy_charge = 0

# if units <= 50:
#     energy_charge = units * 4.10

# elif units <= 100:
#     energy_charge = (50 * 4.10) + ((units - 50) * 5.55)

# elif units <= 200:
#     energy_charge = (50 * 4.10) + (50 * 5.55) + ((units - 100) * 7.10)

# else:
#     energy_charge = (50 * 4.10) + (50 * 5.55) + (100 * 7.10) + ((units - 200) * 8.15)

# fixed_charge = 110

# subtotal = energy_charge + fixed_charge

# tax = subtotal * 0.06

# total_bill = subtotal + tax

# print("\n------ BESCOM Electricity Bill ------")
# print(f"Units Consumed : {units}")
# print(f"Energy Charges : ₹{energy_charge:.2f}")
# print(f"Fixed Charge   : ₹{fixed_charge:.2f}")
# print(f"Subtotal       : ₹{subtotal:.2f}")
# print(f"Govt Tax (6%)  : ₹{tax:.2f}")
# print(f"Total Bill     : ₹{total_bill:.2f}")
# print("------------------------------------")

# Cricket Strike Rate Faced
# runs = int(input("Enter the runs: "))
# balls = int(input("Enter balls faced: "))
# if balls == 0:
#     print("Cannot Calculate strike rate !! ")
# else:
#     strike_rate = (runs / balls) / 100
#     print(f"Strike Rate = {strike_rate:.2f}")

# if strike_rate > 150:
#     print("Explosive T20 Finishser ")
# elif strike_rate > 100:
#     print("Aggresive top order ")
# elif strike_rate >= 75:
#     print("Steady ODI Anchor")
# else:
#     print("Defensive Test match")


# BMI Calculator
# weight = float(input("Enter the weight: "))
# height = float(input("Enter the height: "))
# height = height / 100
# bmi = weight / (height * height)
# print("BMI = ",round (bmi, 2))
# if bmi < 18.5:
#     print("Underweight")
# elif bmi <= 22.9:
#     print("Normal")
# elif bmi <= 24.9:
#     print("Overweight")
# elif bmi <= 29.9:
#     print("Obese class I")
# elif bmi <= 30:
#     print("Obese class II")
# else:
#     print("Default weight")