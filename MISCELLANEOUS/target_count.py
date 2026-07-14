n = int(input("Write the length of the array: "))
arra = list(map(int,input().split()))
k = int(input("Write the target value : "))
arra.sort()

def target_count(arra):
    count = 0
    for i in range(1,len(arra)):
        if arra[i] - arra[i-1] == k:
            count+=1
    return count

print(target_count(arra))
