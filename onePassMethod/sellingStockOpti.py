# Leet code question 121:
class Solution:
    def max_profit(self, prices):
        if not prices and prices < 2:
            return 0

        min_price = float('inf')
        max_profit = 0
        for price in prices:
            min_price = min(min_price, price)
            profit = price - min_price
            max_profit = max(max_profit, profit)
        return max_profit

solution  = Solution()
print("MaxProfit is: ", solution.max_profit([7,1,5,3,6,4]))
print("MaxProfit is: ", solution.max_profit([7,6,4,3,1]))

    

# Time complexity: O(n)
# Space complexity: O(1)