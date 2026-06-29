def bubble_sort(arr):
    a = list(map(int,input().split()))
    n = int(input())
    
    for i in range(n-1):
        swapped = False
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                swapped = True
        if not swapped:
            break
arr = [1,2,34,21,344]
print(bubble_sort(arr))