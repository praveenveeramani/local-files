############read file################
f=open("file handling.txt","r")
print(f.read())

########## wite file#################(write func overight the file)

f=open("file handling.txt","w")
f.write("banana\n""apple\n")
f.close()

f=open("file handling.txt","r")
print(f.read())
f.close()

############ read and write #########

f=open("file handling.txt","r+")
print(f.read())
f.write("banana1\n""apple2\n")
f.close()


################## append ###################(add txt)

f=open("file handling.txt","a")
f.write("orange\n""graps\n")
f.close()

f=open("file handling.txt","r+")
print(f.read())
f.close()
