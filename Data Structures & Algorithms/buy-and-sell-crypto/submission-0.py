class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0 # buy
        r = 1 # sell
        max_prof = 0

        while r < len(prices): # iterate over all in bounds    
            if prices[l] < prices[r]: # found the min w. left
                profit = prices[r] - prices[l] # check profit
                max_prof = max(max_prof, profit) # max profitable checked
            else:     # the min is actually w. right
                l = r   # update left to be right now
            r += 1 # continue down the array
        return max_prof       
        