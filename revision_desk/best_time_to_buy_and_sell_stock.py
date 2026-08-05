def besttime(prices):
    maxprofit = 0
    min_price = float('inf')
    
    for i in range(len(prices)):
        min_price = min(min_price,prices[i])
        maxprofit = max(maxprofit, prices[i]-min_price)
    return maxprofit