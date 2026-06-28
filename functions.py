# Calculate GST
# def calculate_gst(amount, gst_rate=18, gst_inclusive=False):
#     if gst_inclusive:
#         base = amount / (1 + gst_rate / 100)
#         gst = amount - base
#         total = amount
#     else:
#         base = amount
#         gst = base * gst_rate / 100
#         total = base + gst
#     return round(base, 2), round(gst, 2), round(total, 2)

# # Test cases
# print(calculate_gst(1000))
# print(calculate_gst(1180, gst_inclusive=True))
# print(calculate_gst(500, gst_rate=5))

## Recuesive Function

# def power(base, exp):
#     if exp == 0:
#         return 1
#     if exp < 0:
#         return 1 / power(base, -exp)
#     return base * power(base, exp - 1)

# # Test cases
# print(power(2, 10))   # 1024
# print(power(5, 0))    # 1
# print(power(3, -2))   # 0.1111111111111111