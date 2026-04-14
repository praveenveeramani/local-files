################## string type ##################

string = input("enter the string:")
rev_string = string[::-1]  ##slicing methed" var_name = [strat:end:step] " ...step means "if 1  step print ordinary and if 2 print 1 2 4"
print("reversed:",rev_string)
if string==rev_string:
    print("given string is palindrome")
else:
    print("given string is not palindrome")


################### integer type ################

number = int(input("enter the number:"))
string = str(number)
rev_string = string[::-1]
print("reversed:",rev_string)
if string==rev_string:
    print("given number is palindrome")
else:
    print("given number is not palindrome")

###################################################
revstring = ""
for i in string[::-1]:
    revstring += i
if string==revstring:
    print("given string is palindrome")
else:
    print("given string is not palindrome")

