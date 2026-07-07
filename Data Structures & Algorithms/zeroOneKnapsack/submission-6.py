class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        # bottom-up dynamic programming, O(mn) time and O(mn) space
        n = len(profit)
        dp = [[0] * (capacity + 1) for _ in range(n)]

        # initialize dp table
        for i in range(n):
            dp[i][0] = 0 # when capacity is 0, no profit
        for j in range(capacity + 1):
            if j >= weight[0]:
                dp[0][j] = profit[0]
        
        # fill the rest of the dp table
        for i in range(1, n):
            for j in range(1, capacity + 1):
                skip = dp[i - 1][j] # just use the top cell
                include = 0
                
                updated_capacity = j - weight[i]

                if updated_capacity >= 0:
                    include = dp[i - 1][updated_capacity] + profit[i]
                dp[i][j] = max(include, skip)
        
        return dp[n - 1][capacity]
