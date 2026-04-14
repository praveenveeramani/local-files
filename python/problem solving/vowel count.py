sentance = input("enter the sentance:")
convert_string = sentance.lower()
count = 0
list1=["a","e","i","o","u"]
for i in convert_string:
    if i in list1:
        count=count+1

print("number of vowels in given sentance :",count)
