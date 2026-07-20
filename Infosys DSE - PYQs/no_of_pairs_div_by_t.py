# Brute Force
# def no_of_pairs_div(nums,t):
#     used = [False] * len(nums)
#     pairs = []
    
#     for i in range(len(nums)):
#         if used[i]:
#             continue
#         for j in range(i+1,len(nums)):
#                 if used[j]:
#                     continue
                
#                 if (nums[i]+nums[j])%t == 0:
#                     pairs.append((nums[i],nums[j]))
#                     used[i] = True
#                     used[j] = True
#                     break
#     return len(pairs),pairs

# Optimal Solution
def optimal_no_of_div(nums,t):
    pairs = []
    for i,n in enumerate(nums):
        need = n%t
        if need in pairs:
            return [pairs[need],i]
        
            




# nums = list(map(int, input().split()))
# t = int(input())
# print(no_of_pairs_div(nums,t))