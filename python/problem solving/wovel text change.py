def transalte(wovels):
    empty=""
    for i in wovels:
        if i.upper() in "AEIOU":
            if i.islower():
                empty=empty+"g"
            else:
                empty=empty+"G"
        else:
            empty=empty+i
    return empty
print(transalte(input("any wovels use: ")))
