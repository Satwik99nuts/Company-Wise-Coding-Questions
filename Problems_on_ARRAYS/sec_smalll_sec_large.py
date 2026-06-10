arra = list(map(int, input().split()))

def sec_largest(arra):
    for i in arra:
        largest = float("-inf")
        sec_largest = float("-inf")
        if i>largest:
            sec_largest = largest
            largest=i

        elif i> sec_largest and i!=largest:
            sec_largest = i
    return sec_largest
def sec_smallest(arra):
    smallest = float("inf")
    sec_smallest = float("inf")
    for j in arra:
        if j < smallest:
            sec_smallest = smallest
            smallest = j

        elif j< sec_smallest and j!= smallest:
            sec_smallest = j
    return sec_smallest

print("Second largest:", sec_largest(arra))
print("Second smallest:", sec_smallest(arra))
