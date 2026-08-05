def dist(nums):
    count = 0
    seen = []
    
    for num in nums:
        if num not in seen:
            seen.append(num)
            count+=1
    return count
nums = [1,2,34,7,3]
print(dist(nums))