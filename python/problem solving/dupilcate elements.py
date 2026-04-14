lis = [1, 2, 1, 2, 3, 4, 5, 1, 1, 2, 5, 6, 7, 8, 9, 9]
x = list(set(lis))
print("no dupilcates in list:",x)
y = []
for i in x:
    if lis.count(i) > 1:
        y.append(i)
print("dulpicate in list:",y)
