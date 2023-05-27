# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

def stock_transactions(prices):
    left = 0
    right = 1
    answer = 0
    for x in range(len(prices)):
        # cleft = prices[left]
        cright = prices[right]
        # curr = prices[right] - prices[left]
        if prices[left] < prices[left+1]: # if the next price is 
            left += 1
        
        print(curr)
        if curr > answer:
            answer = curr
        right += 1
    
    return answer

prices = [7,1,5,3,6,4]
print(stock_transactions(prices))