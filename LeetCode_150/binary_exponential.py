def power(x,n):
    if n<0:
        x, n = 1/x,-n
    result = 1
    
    while n:
        if n%2:
            result *= x
        x*=x
        n = n//2
    return result