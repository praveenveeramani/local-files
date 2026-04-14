
str1=input("enter 1st sentance:")
str2=input("enter 2nd sentance:")
s_str1=sorted(str1)
s_str2=sorted(str2)
if len(s_str1)==len(s_str2):
    if s_str1==s_str2:
        print("given sentance is anagram")
    else:
        print("given sentance is not a anagram")
else:
    print("given sentance is not a anagram")
