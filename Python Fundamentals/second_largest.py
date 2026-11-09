def sec_largest_number(arr):
    largest = float('-inf')
    sec_largest = float('-inf')

    for i in range(len(arr)):
        if arr[i] > largest and arr[i] > sec_largest:
            sec_largest = largest 
            largest = arr[i]

        elif arr[i] >sec_largest and arr[i]<largest:
            sec_largest = arr[i]

    if sec_largest == float('-inf'):
        return None

    return sec_largest

a = [5,5,5,4]
print(sec_largest_number(a))
print(sec_largest_number([10]))
print(sec_largest_number([5, 5, 5]))
print(sec_largest_number([10, 5, 20, 8, 20, 15])) 
print(sec_largest_number([5, 5, 5, 4]))           
print(sec_largest_number([1, 2]))                 
print(sec_largest_number([10]))                   
print(sec_largest_number([5, 5, 5]))              
