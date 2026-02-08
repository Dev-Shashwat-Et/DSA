# Leet code question 121:
class Solution:
    def max_profit(self, prices):
        if not prices and len(prices) < 2:
            return 0

        min_price = float('inf')
        max_profit = 0
        for price in prices:
            min_price = min(min_price, price)
            profit = price - min_price
            max_profit = max(max_profit, profit)

            # Alternative way using if statement
            """"if price < min_price:
                min_price = price              
            else:
                current_profit = price - min_price
                if current_profit > max_profit:
                    max_profit = current_profit
                    """
        return max_profit

solution  = Solution()
print("MaxProfit is: ", solution.max_profit([7,1,5,3,6,4]))
print("MaxProfit is: ", solution.max_profit([7,6,4,3,1]))

    

# Time complexity: O(n)
# Space complexity: O(1)


"""
The logic in plain English:
Look at today's price.

Is it the lowest I've ever seen? If yes, I'll remember this as my potential "Buy" day.

If I sold today using the lowest "Buy" day I found earlier, how much would I make? 4. Is that amount more than I've ever made before? If yes, keep that number as the record profit.

"""