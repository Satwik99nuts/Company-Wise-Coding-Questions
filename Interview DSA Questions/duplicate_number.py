# Floyd's Cycle Detection -----> see once 
def dup_number(arr):
    fast = slow = arr[0]

    while True:
        slow = arr[slow]
        fast = arr[arr[fast]]

        if slow == fast:
            break

    slow = arr[0]

    while slow != fast:
        slow = arr[slow]
        fast = arr[fast]

    return slow

arr = [3, 4, 4, 4, 4, 4]
print(dup_number(arr))