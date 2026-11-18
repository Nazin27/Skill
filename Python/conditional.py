# To check whether a string is palindrome or not
n = input("Enter a string: ")
if (n[::-1]) == n:
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")

# check whether a string has 5 characters or not
n = input("Enter a string: ")
if len(n) == 5:
    print("The string has 5 characters")
else:
    print("The string does not have 5 characters")

# To check whether a string is in uppercase or not
k = input("Enter a string:")
if k.isupper():
    print("The string is in uppercase")
else:
    print("The string is not in uppercase")

# To check whether a number has 2 digits or not
s = int(input("Enter a number: "))
if 10 <= s <= 99:
    print("The number has 2 digits")
else:
    print("The number does not have 2 digits")

# To check whether a character is an uppercase letter or not
ch = input("Enter a character: ")
if "A" <= ch <= "Z":
    print("True")
else:
    print("False")
