num=int(input("how many u num want;"))
list=[int(input("enter the num;"))for i in range(num)]
print(list)
rev_list=list[::-1]
print(rev_list)

################## anthor way #######################
print("next")
i=0
j=num-1
while i<j:
    temp=list[i]
    list[i]=list[j]
    list[j]=temp
    i=i+1
    j=j-1

print(list)
