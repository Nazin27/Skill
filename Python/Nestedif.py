# To check whether a character is a vowel or consonant
"""b = input("Enter a character:")
if b.isalpha():
    if b in "aeiouAEIOU":
        print("The character is a vowel")
    else:
        print("The character is a consonant")
else:
    print("The character is not an alphabet")"""

# To check whether a list has even or odd number of elements
i = eval(input("Enter a list: "))
if type(i) == list:
    if len(i) % 2 == 0:
        print("The list has even number of elements")
    else:
        print("The list has odd number of elements")
else:
    print("The input is not a list")
