# To check the greater number among two numbers
"""a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
if a > b:
    print(f"{a} is greater than {b}")
elif a < b:
    print(f"{b} is greater than {a}")
else:
    print(f"{a} is equal to {b}")"""

# To check whether a character is an uppercase, lowercase, digit or special character
s = input("Enter a character: ")
if "A" <= s <= "Z":
    print("The character is an uppercase letter")
elif "a" <= s <= "z":
    print("The character is a lowercase letter")
elif 0 <= int(s) <= 99999:
    print("The character is a digit")
else:
    print("The character is a special character")

# To check a number is a single,double,triple or four digit number
e = int(input("Enter a number: "))
if 0 <= e <= 9:
    print(f"{e} is a single digit")
elif 10 <= e <= 99:
    print(f"{e} is a two digit number")
elif 100 <= e <= 999:
    print(f"{e} is a three digit number")
else:
    print(f"{e} is a four or more digit number")
