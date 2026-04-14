s_captcha="abcd123"
def captcha():
    count=0
    for i in range(1,4):
        cc=input("enter captcha:")
        if(s_captcha==cc):
            print("login")
            break
        else:
            count= count+1
            if(count<3):
                print("retry")
                print("remaining", 3-count,"attempt")
            else:
                print("sorry for inconvience")
                print("<---please retry after 30 seconds--->")
       
captcha()
