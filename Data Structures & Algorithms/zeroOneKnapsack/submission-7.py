class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        # bottom-up dynamic programming with memory optimization, O(mn) time and O(m) space
        n = len(profit)
        dp = [0] * (capacity + 1)

        # initialize dp table
        dp[0] = 0 # when capacity is 0, no profit
        for j in range(capacity + 1):
            if j >= weight[0]:
                dp[j] = profit[0]
        
        # fill the rest of the dp table
        for i in range(1, n):
            curr = [0] * (capacity + 1)
            for j in range(1, capacity + 1):
                skip = dp[j] # just use the top cell
                include = 0
                
                updated_capacity = j - weight[i]

                if updated_capacity >= 0:
                    include = dp[updated_capacity] + profit[i]
                curr[j] = max(include, skip)
            dp = curr
        
        return dp[capacity]
