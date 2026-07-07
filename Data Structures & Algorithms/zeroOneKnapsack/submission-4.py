class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        """
        dfs with memoization
        """
        n = len(profit)
        memo = [[-1] * (capacity + 1) for _ in range(n)]
        return self.dfs_memo(0, profit, weight, capacity, memo)
    
    def dfs_memo(self, i, profit, weight, capacity, memo):
        # base case 1: at capacity
        if i == len(profit):
            return 0
        
        # base case 2: current attainable max profit is already calculated
        if memo[i][capacity] != -1:
            return memo[i][capacity]
        
        # not including item i
        memo[i][capacity] = self.dfs_memo(i + 1, profit, weight, capacity, memo)

        # including item i
        updated_capacity = capacity - weight[i]
        if updated_capacity >= 0:
            profit = profit[i] + self.dfs_memo(i + 1, profit, weight, updated_capacity, memo)
            memo[i][capacity] = max(memo[i][capacity], profit)

        return memo[i][capacity]
