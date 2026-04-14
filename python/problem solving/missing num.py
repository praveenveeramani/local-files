n=4
arr=1,3,4
print((n*(n+1))//2-sum(arr))


#################################

list=[int(input("enter the sequence and miss one integer:")) for i in range(0,4)]
def miss_num():
    print(list)
    a=1
    while a in list:
        a+=1
    return a
    
print(miss_num())
