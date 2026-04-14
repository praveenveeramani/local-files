def result():
     score=0
     count=0
     for i in range(1,6):
          mark=int(input("enter mark: "))
          if mark>=35:
               print("pass")
               score+=1
          else:
               print("fail")
               count+=1
     print("you are pass",score,"/","5 subject")
     if count>0:
          print( "you fail",count,"/" " 5 subject")

result()
