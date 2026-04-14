def cube_square(a,b):
    result=1
    for i in range(b):
        result=result * a
    return result
a=int(input("please enter base value:"))
b=int(input("please enter power value:"))
print(cube_square(a,b))
