def lin_search(arr,target):
    n = len(arr)
    for i in range(n):
        if arr[i]==target:
            return i

arr = list(map(int,input().split()))
target = int(input("Write the number to be found: "))
print(lin_search(arr,target))