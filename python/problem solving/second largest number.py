list=[10,20,38,74,82,99,28,77]
list.sort()
print(list)
print("1st largest number is;",list[-1])
print("2nd largest number is;",list[-2])

print()#space
################# remove duplicate ######################

list1=[10,10,20,30,44,77,67,88,94,94]
new_list=set(list1)
new_list.remove(max(new_list))
print("no more duplicate:",max(new_list))


################## no build-in function ####################
print()
      
num=[9,8,3,2]
n=len(num)                      #<--must use for all-->
for i in range(0,n):            #use to sort, reverse sort 
    for j in range(i+1,n):      #no-build fun
        if num[i]>num[j]:
            temp=num[i]
            num[i]=num[j]
            num[j]=temp
            print(num)

print(num[-2])
