a = list(map(int, input().split()))
max_val = a[0]
min_val = a[0]

for i in range(len(a)):
    if a[i]>max_val:
        max_val = a[i]
    else:
        min_val= a[i]
print(f"max_val = {max_val},min_val = {min_val}")