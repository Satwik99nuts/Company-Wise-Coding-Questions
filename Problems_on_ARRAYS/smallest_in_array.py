arra = list(map(int, input().split()))

def smallest_in_array(arra):
    small = arra[0]
    for i in arra:
        if i<small:
            small = i 
            i+=1    
    return small

print(smallest_in_array(arra))
# NOTE:-input().split()
# FOR SPACE SEPARATED NUMBERS
# AND input() FOR DIRECTLY DIGIT BY DIGIT INPUT