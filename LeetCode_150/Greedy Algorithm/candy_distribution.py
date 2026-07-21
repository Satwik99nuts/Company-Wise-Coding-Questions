def candy_dist(rating):
    n = len(rating)
    candies = [1]*n
    
    for i in range(1,n):
        if rating[i]>rating[i-1]: #left to right
            candies[i] = candies[i-1]+1
    
    for i in range(n-2,-1,-1):
        if rating[i]>rating[i+1]: #right to left
            candies[i] = max(candies[i+1]+1,candies[i])
    return sum(candies)