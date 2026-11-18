# with arguments,with return
def convert(s):
    s = input("Enter:")
    out = ""
    for i in s:
        if "A" <= i < "Z":
            out = out + chr(ord(i) + 32)
        else:
            out += i
    return out


print(convert(s))


# without argument,without return
def convert():
    s = input("Enter:")
    out = ""
    for i in s:
        if "A" <= i < "Z":
            out = out + chr(ord(i) + 32)
        else:
            out += i
    print(out)


convert()


# without argument,with return
def convert():
    s = input("Enter:")
    out = ""
    for i in s:
        if "A" <= i < "Z":
            out = out + chr(ord(i) + 32)
        else:
            out += i
    return out


print(convert(out))
