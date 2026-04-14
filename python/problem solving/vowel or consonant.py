def v_or_c():
    str = input("enter the single letter:")
    list1=["a","e","i","o","u","A","E","I","O","U"]
    if str in list1:
        print("given sentance is vowels")
    else:
        print("given sentance is consonant")
    return v_or_c()

v_or_c()
