num=int(input("enter the how many numbers want in the list:"))
list=[int(input("enter the numbers:"))for i in range(num)]
print(list)
list.sort()
print(list)
list.sort(reverse=True)# use to reverse
print(list)
