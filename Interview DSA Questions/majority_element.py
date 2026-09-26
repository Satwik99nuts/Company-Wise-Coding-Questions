# Boyer Moore Voting -----> Majority Element
def maj_el(a):
    cand = count = 0

    for i in range(len(a)):
        if count == 0:
            cand = a[i]
        count +=1 if cand==a[i] else -1
    return cand
a = [1,2,2,2,2,2,4]
print(maj_el(a))