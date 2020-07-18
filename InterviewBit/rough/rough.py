li = [1,2,3,4,5]

def rev(a):
    mid = len(a)//2
    for i in range(mid):
        a[i], a[-(i+1)] = a[-(i+1)], a[i]

rev(li)
print(li)
