def rev(a):
    l,r = 0,len(a)-1
    while l<r: # or can be "for i in range(len(a)//2)"
        a[l],a[r] = a[r],a[l]
        l+=1
        r-=1
    return a

def rev01(b):
    return b[::-1]

a = [1,2,3,4,5]
b = [3,4,2,4,2]
print(rev(a))
print(rev01(b))