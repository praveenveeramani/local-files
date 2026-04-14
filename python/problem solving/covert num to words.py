number=int(input("enter the number in 1 to 100;"))
names={1:"one", 2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine",10:"ten",11:"eleven",12:"twelve",13:"thriteen",14:"fourteen",15:"fifteen",
       16:"sixteen",17:"seventeen",18:"eighteen",19:"nineteen",20:"twenty",30:"thrity",40:"fourty",50:"fifty",60:"sixty",70:"seventy",80:"eighty",90:"ninety",100:"hundred"}
if number<100:
    if number in names:
        a=names.get(number)
        print(a)
    else:
        r=number%10
        r=names.get(r)
        q=number//10
        q=q*10
        q=names.get(q)
        print(q,r)
else:
    print("error! please provide valid numbers")


