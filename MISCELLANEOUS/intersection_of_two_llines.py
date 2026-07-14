# given 
# two lines having starting and ending points, I have to determine whether they will intersect or not?

def lines(a1,b1,c1,d1,a2,b2,c2,d2):
    a1 = int(input.split()) #A
    a2 = int(input.split()) #A
    b1 = int(input.split()) #B
    b2 = int(input.split()) #B
    c1 = int(input.split()) #C
    c2 = int(input.split()) #C
    d1 = int(input.split()) #D
    d2 = int(input.split()) #D
    
    isTrue = True
    
    if (b1-a1)*(b2-a2) == -1:
        return isTrue
    if 