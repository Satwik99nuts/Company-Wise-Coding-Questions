n = int(input("Write the number of elements in the array : "))
arr = list(map(int, input().split()))

count = 0
max_till_now = float('0-inf')

n = len(arr)
for i in range(0,n):
    if arr[i]>max_till_now:
        count+=1
        max_till_now=arr[i]
        
print(count)