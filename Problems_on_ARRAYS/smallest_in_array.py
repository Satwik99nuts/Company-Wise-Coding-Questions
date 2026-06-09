arra = list(map(int, input("Write the array elements here: ").split()))

def smallest_in_array(arra):
    small = arra[0]
    for i in arra:
        if i<small:
            small = i 
            i+=1    
    return small

def largest_in_array(arra):
    large = arra[0]
    for j in arra:
        if j > large:
            large = j
            j+=1
    return large

print("Smallest in the array is: ",smallest_in_array(arra))
print("Largest in the array is : ",largest_in_array(arra))



# NOTE:-input().split()
# FOR SPACE SEPARATED NUMBERS
# AND input() FOR DIRECTLY DIGIT BY DIGIT INPUT