def pal_check(a):
    l = 0
    r = len(a) - 1
    while r>=0:
        if a[l] != a[r]:
            return False
        else:
            return True
    l+=1
    r-=1

print(pal_check("SasaS"))