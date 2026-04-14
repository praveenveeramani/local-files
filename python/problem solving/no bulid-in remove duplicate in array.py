data=[10,20,30,30,40,40,50,60]
def remov_duplicate(duplist):
    noduplist =[]
    for i in duplist:
        if i not in noduplist:
            noduplist.append(i)
    return noduplist
        
print(remov_duplicate(data))
