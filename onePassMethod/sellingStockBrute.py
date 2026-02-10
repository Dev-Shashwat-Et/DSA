# leet code: 121, time to buy and sell a stock by brutte force method

class Solution:
    def maxProfit(self, prices):
        max_profit = 0
        for i in range(len(prices)):
            """
            # This code is of wrong identation, its only for the shake of understanding data flow in this code
             for j in range(i + 1, len(prices)):
                profit = prices[j] - prices[i]
            if profit > max_profit:
                max_profit = profit
            """
            for j in range(i + 1, len(prices)):
                profit = prices[j] - prices[i]
                if profit > max_profit:
                    max_profit = profit
        return max_profit

solution = Solution()
print("profit is:", solution.maxProfit([7, 1, 4, 6, 3]))
print("profit is:", solution.maxProfit([7, 1, 4, 6, 3]))



"""
Key Python Rule:
Lines with the same indentation are part of the same block

They execute in the order they appear

Inner blocks (more indented) must complete before outer blocks continue

So yes: Same indentation = same execution level = execute together in sequence!

thats why commented code is wrong logically considering this program


"""