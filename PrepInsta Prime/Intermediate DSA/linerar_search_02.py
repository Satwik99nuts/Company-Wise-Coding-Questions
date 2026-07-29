def lin_sear(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return the index
    return -1  # Target not found


arr = [1, 2, 3, 4, 5, 6, 7]

target = 5
result = lin_sear(arr, target)

if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")
