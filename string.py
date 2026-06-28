# Smart Palindrome Checker

# sentence = input("Enter a sentence: ")

# # Build cleaned string (keep only letters and digits, convert to lowercase)
# clean = ""

# for ch in sentence:
#     if ch.isalnum():
#         clean += ch.lower()

# # Check palindrome
# if clean == clean[::-1]:
#     print("TRUE - The sentence is a palindrome.")
# else:
#     print("FALSE - The sentence is not a palindrome.")


# Manual Title Case

# sentence = input("Enter a sentence: ")

# result = ""
# new_word = True

# for ch in sentence:
#     if ch == " ":
#         result += ch
#         new_word = True
#     else:
#         if new_word:
#             result += ch.upper()
#             new_word = False
#         else:
#             result += ch.lower()

# print("Title Case:", result)


# Caesar Cipher Encryptor

# message = input("Enter the message: ")
# shift = int(input("Enter shift value: "))

# result = ""

# for ch in message:
#     if 'A' <= ch <= 'Z':
#         result += chr((ord(ch) - ord('A') + shift) % 26 + ord('A'))
#     elif 'a' <= ch <= 'z':
#         result += chr((ord(ch) - ord('a') + shift) % 26 + ord('a'))
#     else:
#         # Keep digits, spaces, and special characters unchanged
#         result += ch

# print("Encrypted Message:", result)