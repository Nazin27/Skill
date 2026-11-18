# To convert uppercase to lowercase using for loop
s = input("Enter a string:")
for i in s:
    if i.isupper():
        print(i.lower())

# To convert a string from uppercase to lowercase and vice versa using for loop
s = input("Enter a string:")
out = ""
for i in s:
    if "A" <= i <= "Z":
        out += chr(ord(i) + 32)
    elif "a" <= i <= "z":
        out += chr(ord(i) - 32)
else:
    out += i
print(out)

# To print the list into dictionary
s = [12, 10, "hello", "Good", 5j, "Bye"]
out = {}
for i in s:
    if type(i) == str:
        out[i] = i[0] + i[-1]
print(out)
