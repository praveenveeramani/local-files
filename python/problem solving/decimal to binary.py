num = int(input("enter the number:"))
string = str(bin(num))
b_num = string[2::1]
print(int(b_num))
