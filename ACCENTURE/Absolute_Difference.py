# Given an array arr, a number num, and a value diff, count how many elements
# of arr have an absolute difference with num that is less than or equal to diff.
# If no element qualifies, return -1.
# Example: arr=[12,3,14,56,77,13], num=13, diff=2 -> Output: 3
# (12, 13, 14 are all within 2 of 13)

def abs_diff(arr, n, diff):
    count = 0
    al = len(arr)
    for i in range(al):
        if abs(arr[i]-n)<=diff:
            count+=1
    return count if count>0 else -1
if __name__ == "__main__":
    arr = [12,3,14,56,77,13]
    print(abs_diff(arr,13,2))