def largest(arr):
    largest = arr[0]
    for i in range(len(arr)):
        if arr[i]>largest:
            largest = arr[i]
    return largest

def sec_largest(arra):
    if len(arra)<2:
        return -2
    sec_largest = float('-inf')
    large = arra[0]
    for i in range(len(arra)):
        if arra[i] > large:
            large = arra[i]
            sec_largest = large
        elif large>arra[i]>sec_largest:
            sec_largest = arra[i]
        else:
            return -1
    return sec_largest if sec_largest!= float('-inf') else -1

def array_is_sorted_or_not(a):
    for i in range(len(a)):
        if arr[i]>arr[i+1]:
            return True
        else:
            return False

def el_appearing_once(ar):
    ar.sort()
    for i in range(len(ar)):
        if ar[i] == ar[i+1]:
            return False
        else:
            return True




arr = [10,28,39,938,83933,8292,9000000000000000]
a = [1,2,3,4-1]
ar = [1,2,1,11,3,4,5,6,4343,3,2,23,43,23,43,4,4,4444,332222,3463434,222223,3456,3,4,3445745645,5,5,555555,5555555555,5555,555555555,5555,5,5,5,5]
print(largest(arr))
print(sec_largest(arr))
print(array_is_sorted_or_not(a))
print(el_appearing_once(ar))