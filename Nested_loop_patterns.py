# Print this pattern for N = 5
# n = 5
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j,end="")
#     print()

# print this number diamond for N = 5 (the digits go up to N in the middle row):

# n = 5
# Upper Half
# for i in range(1, n + 1):
#     print(" " * (n - i), end="")
    
#     for j in range(1, i + 1):
#         print(j, end=" ")
    
#     for j in range(i - 1, 0, -1):
#         print(j, end=" ")
    
#     print()

# Lower Half

# for i in range(n - 1, 0, -1):
#     print(" " * (n - i), end="")
    
#     for j in range(1, i + 1):
#         print(j, end=" ")
    
#     for j in range(i - 1, 0, -1):
#         print(j, end=" ")
    
#     print()

#  Print a hollow square of size N (only the border is *, inside is blank). For N = 5:
# n = 5
# for i in range(n):
#     for j in range(n):
#         if i == 0 or i == n - 1 or j == 0 or j == n - 1:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()

#  Print the first 5 rows of Pascal's Triangle:
# n = 5
# for i in range(n):
#     num = 1
#     print(" " * (n - i), end="")

#     for j in range(i + 1):
#         print(num, end=" ")
#         num = num * (i - j) // (j + 1)

#     print()


# Number of rows
# N = 5
# # Loop through each row
# for i in range(1, N + 1):
    
#     # Loop to print characters from 'A' up to the current row
#     for j in range(i):
#         # chr(65) is 'A', chr(66) is 'B', and so on
#         print(chr(65 + j), end="")
    
#     # Move to the next line after each row
#     print()