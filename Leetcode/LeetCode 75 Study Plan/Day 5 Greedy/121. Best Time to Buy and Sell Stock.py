#1st approach with time limit exceed 
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
                mx=0
                for idx , curr_pr in enumerate(prices):
                    for  next_pr in prices[idx:]:
                        diff=next_pr - curr_pr
                        mx=max(mx,diff)
                return mx

'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0
        
        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)
        
        return max_profit