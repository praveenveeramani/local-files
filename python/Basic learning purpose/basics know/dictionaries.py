
print(dict()) #-----------------> inbliud key to create the dictionary
print()

num={1:"one",2:"two",3:"three"}
numbers = dict(num) #-----------> use to copy the dictionary
print(numbers)
print()


del numbers[2]  #---------------> use to delete the dict
print(numbers)
print()


print(num[1])  #----------------> use to print the value
print()

list={}.fromkeys(range(1,6),10) #--------> use to 
print(list)
