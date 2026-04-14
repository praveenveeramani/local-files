try:
    a=int(input("a;"))
    b=int(input("b;"))
    print(a+b)
    print(d)
except ValueError as e:
    print("value error:",e)
    print("type num") 

except NameError as e:
    print("name error",e)
    
except exception:
    print("someting worng")
finally:
    print("done")
