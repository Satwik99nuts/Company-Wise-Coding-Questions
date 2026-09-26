def interesection(a,b):
    return list(set(a) & set(b))

def interesection2(a,b):
    res = []
    for i in a:
        if i in b:
            res.append(i)
    return res

a = [1,2,3,4]
b = [3,4,5]
print(interesection(a,b))
print(interesection2(a,b))