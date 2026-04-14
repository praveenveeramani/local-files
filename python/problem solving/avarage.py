
def f_avg (val):
    s=0
    for i in val:
        s = s+i
    return s/len(val)
print(f_avg([1,2,3,4,5]))


l=1,2,3,4,5
avg = sum(l)/len(l)
print(avg)
