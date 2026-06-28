# Q11.
# output
# matrix1 = [[99,0,0],[0,0,0],[0,0,0]]
# matrix2 = [[99,0,0],[99,0,0],[99,0,0]]
# why : matrix1 - seperate lists
#  #    matrix2 - samae list repeated

# Q12.
# output
# x = [1,2,3,4]
# y = [1,2,3]

# a = [1,2,3,4]
# b = [1,2,3,4]
# why : 
# x = x + [4] - new list created
# a += [4] - modified same list

# Q13.
# output
# 4 - nameError
# why : i keeps last value = 4
#      j never created(range 0)

# Q14.
# print("10" + "20") - 1020
# print(10 + 20) - 30
# print("10" * 3) - 101010
# print(10 * "3") - 3333333333
# print("10" + 20) - TypeError
# print(int("10") + 20) - 30

# Q15.
# print(0 or 5) - 5
# print(5 or 0)  - 5
# print(None or "hello") - hello 
# print(0 and 5) - 0
# print(5 and 10)  - 10
# print([] or "default") - default
# print([0] or "default")  - [0]