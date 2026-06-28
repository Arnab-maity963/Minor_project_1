# # Take input
# marks = list(map(int, input("Enter 10 student marks: ").split()))

# # (a) Maximum
# maximum = marks[0]
# for mark in marks:
#     if mark > maximum:
#         maximum = mark

# # (b) Minimum
# minimum = marks[0]
# for mark in marks:
#     if mark < minimum:
#         minimum = mark

# # (c) Average
# total = 0
# for mark in marks:
#     total += mark
# average = total / len(marks)

# # (d) Count of students above average
# count = 0
# for mark in marks:
#     if mark > average:
#         count += 1

# # (e) Second highest mark
# highest = -1
# second_highest = -1

# for mark in marks:
#     if mark > highest:
#         second_highest = highest
#         highest = mark
#     elif mark > second_highest and mark != highest:
#         second_highest = mark

# # Display results
# print("Maximum:", maximum)
# print("Minimum:", minimum)
# print("Average:", average)
# print("Students above average:", count)

# if second_highest == -1:
#     print("Second highest mark does not exist.")
# else:
#     print("Second highest mark:", second_highest)


# Swiggy Analyzer

# review = input().lower().split()

# freq = {}

# for word in review:
#     freq[word] = freq.get(word, 0) + 1

# items = list(freq.items())

# for i in range(len(items)):
#     for j in range(i + 1, len(items)):
#         if items[j][1] > items[i][1]:
#             items[i], items[j] = items[j], items[i]

# for word, count in items:
#     print(word, ":", count)

# print("Most Frequent:", items[0][0], "-", items[0][1])


# ### Indian State CRUD

# d = {"Karnataka":"Bengaluru","Maharashtra":"Mumbai","Tamil Nadu":"Chennai","Gujarat":"Gandhinagar","West Bengal":"Kolkata"}

# while True:
#     c = int(input("1.Add 2.Update 3.Delete 4.Search 5.Display 6.Exit: "))

#     if c == 1:
#         d[input("State: ")] = input("Capital: ")
#     elif c == 2:
#         s = input("State: ")
#         if s in d:
#             d[s] = input("New Capital: ")
#     elif c == 3:
#         d.pop(input("State: "), None)
#     elif c == 4:
#         print(d.get(input("State: "), "Not found"))
#     elif c == 5:
#         for i in sorted(d):
#             print(i, "->", d[i])
#     elif c == 6:
#         break

# ## Set Opeartions

# A = {"Python", "Java", "C++", "SQL"}
# B = {"Java", "JavaScript", "Python", "Go", "SQL"}

# print("Both:", A & B)
# print("Only A:", A - B)
# print("Only B:", B - A)
# print("Unique:", A | B)
# print("Exclusive:", A ^ B)

# TCS Stock Price

# prices = (3845, 3902, 3878, 3955, 4012, 3998, 4055)
# days = ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun")

# mx = max(prices)
# mn = min(prices)

# print("Max:", mx, days[prices.index(mx)])
# print("Min:", mn, days[prices.index(mn)])
# print("Average:", sum(prices) / len(prices))

# gain = prices[1] - prices[0]
# d = 0
# vol = 0

# for i in range(1, len(prices)):
#     diff = prices[i] - prices[i - 1]
#     vol += abs(diff)
#     if diff > gain:
#         gain = diff
#         d = i

# print("Biggest Gain:", gain, days[d - 1], "to", days[d])
# print("Volatility:", vol)


# nums = [2,5,3,2,7,8,5,9,1,4,6,7,8,10,11,12,10,13,14,15]

# u = set(nums)
# dup = []
# once = []

# for i in u:
#     if nums.count(i) > 1:
#         dup.append(i)
#     else:
#         once.append(i)

# print("Unique:", u)
# print("Duplicates:", dup)
# print("Exactly Once:", once)