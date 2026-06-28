# import numpy as np

# #  Create a 5×5 identity matrix
# identity_matrix = np.eye(5)
# print("Step (a): 5×5 Identity Matrix")
# print(identity_matrix)

# # Multiply every element by 10
# scaled_matrix = identity_matrix * 10
# print("\nStep (b): Identity Matrix after multiplying by 10")
# print(scaled_matrix)

# #  Transpose the matrix
# transpose_matrix = scaled_matrix.T
# print("\nStep (c): Transposed Matrix")
# print(transpose_matrix)


# #  Compute the sum of diagonal elements
# diagonal_sum = np.trace(transpose_matrix)
# print("\nStep (d): Sum of diagonal elements =", diagonal_sum)

# # Compute the sum of all elements
# total_sum = np.sum(transpose_matrix)
# print("Step (e): Sum of all elements =", total_sum)




# # 7-day Zomato Bengaluru sales (in ₹)
# sales = np.array([12000, 18500, 14200, 22100, 19800, 35200, 28400])

# days = np.array(["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"])

# print("Sales:", sales)

# #  Total weekly sales
# total_sales = np.sum(sales)
# print("\n(a) Total Weekly Sales: ₹", total_sales)

# #  Daily average
# average_sales = np.mean(sales)
# print("(b) Daily Average Sales: ₹", average_sales)

# #  Day with maximum sales
# max_day = days[np.argmax(sales)]
# print("(c) Day with Maximum Sales:", max_day)

# #  Number of days with sales above the weekly average
# days_above_avg = np.sum(sales > average_sales)
# print("(d) Number of Days Above Weekly Average:", days_above_avg)

# # Percentage growth from Monday to Sunday
# growth = ((sales[-1] - sales[0]) / sales[0]) * 100
# print("(e) Percentage Growth (Mon to Sun): {:.2f}%".format(growth))

# #  Day-on-day percentage changes
# daily_change = ((sales[1:] - sales[:-1]) / sales[:-1]) * 100
# print("(f) Day-on-Day Percentage Changes (%):")
# print(np.round(daily_change, 2))



# # Create a 5×5 array of zeros
# arr = np.zeros((5, 5), dtype=int)

# # Set the border elements to 1
# arr[0, :] = 1      # Top row
# arr[-1, :] = 1     # Bottom row
# arr[:, 0] = 1      # Left column
# arr[:, -1] = 1     # Right column

# # Display the array
# print(arr)