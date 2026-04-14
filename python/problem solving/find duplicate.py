string = input("enter the sentance:")
duplicate =[]
for i in string:
    if string.count(i)>1:
        if i not in duplicate:
            duplicate.append(i)
            print(i, end="")
print()
print(duplicate)

