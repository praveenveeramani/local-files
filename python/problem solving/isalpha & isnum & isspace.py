s = "geeks for geeks 1212 165 665"
string = ""
integer = ""
space = ""
for i in s:
    if i.isalpha():
        string += i
    if i.isdigit():
        integer +=i
    if i.isspace():
        space+=i
print(string)
print(space)
print(integer)
