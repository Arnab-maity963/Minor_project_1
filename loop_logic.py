# # Find Armstrong numbers from 1 to 9999

# count = 0

# for num in range(1, 10000):
#     s = 0
#     temp = num
#     n = len(str(num))

#     while temp > 0:
#         digit = temp % 10
#         s = s + digit ** n
#         temp = temp // 10

#     if s == num:
#         print(num, end=", ")
#         count += 1

# print("\nCount =", count)

# Input N
# N = int(input("Enter N: "))

# a = 0
# b = 1
# total = 0

# Print first N Fibonacci terms
# for i in range(N):
#     print(a, end=" ")
#     total = total + a
#     a, b = b, a + b

# # Print sum
# print("\nSum =", total)


# prime number check

# def isPrime(n):
#     if n < 2:
#         return False
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     return True

# N = int(input())

# print("Prime" if isPrime(N) else "Not Prime")

# s = 0
# for i in range(2, N + 1):
#     if isPrime(i):
#         s += i

# print("Sum =", s)


# Input
# num = int(input("Enter a number: "))

# # Negative numbers are not palindrome
# if num < 0:
#     print("Not Palindrome")
# else:
#     temp = num
#     rev = 0

#     while temp > 0:
#         digit = temp % 10
#         rev = rev * 10 + digit
#         temp = temp // 10

#     print("Reversed Number =", rev)

#     if num == rev:
#         print("Palindrome")
#     else:
#         print("Not Palindrome")


# Input two numbers
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))

# x = a
# y = b

# # Find HCF using Euclidean algorithm
# while y != 0:
#     x, y = y, x % y

# hcf = x
# lcm = (a * b) // hcf

# print("HCF =", hcf)
# print("LCM =", lcm)


# Input sentence
# s = input("Enter a sentence: ")

# chars = words = vowels = consonants = digits = spaces = special = 0
# in_word = False

# for ch in s:
#     chars += 1

#     if ch.isalpha():
#         if ch.lower() in "aeiou":
#             vowels += 1
#         else:
#             consonants += 1

#         if not in_word:
#             words += 1
#             in_word = True

#     elif ch.isdigit():
#         digits += 1
#         if not in_word:
#             words += 1
#             in_word = True

#     elif ch == " ":
#         spaces += 1
#         in_word = False

#     else:
#         special += 1
#         in_word = False

# print("Characters =", chars)
# print("Words =", words)
# print("Vowels =", vowels)
# print("Consonants =", consonants)
# print("Digits =", digits)
# print("Spaces =", spaces)
# print("Special Characters =", special)


