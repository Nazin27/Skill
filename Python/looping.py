# To print Hello using while loop 5 times
i = 1
while i <= 5:
    print("Hello")
    i += 1

# To print the values of list
l = eval(input("Enter a list:"))
i = 0
while i < len(l):
    print(l[i])
    i += 1

# Reverse a number using while loop
n = int(input("Enter a number:"))
rev = 0
while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n = n // 10
print("Reverse of the number is:", rev)
