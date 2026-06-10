class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        '''
        index       0   1   2   3
        profit      4   4   7   1
        weight      5   2   3   1
        capacity    8

        goal: maximize profit

        brute-force

                        C=8
                4 /           0 \
                C=3             C=8
            4 /    0 \         4 /  0 \
            C=1     C=3        C=6    c=8
            ...
        
        size of tree: O(2^n), two branches each level

        0/1 knapsack: to include or not to include
        '''
        return self.dfs(0, profit, weight, capacity)
    
    def dfs(self, i, profit, weight, capacity):
        if i == len(profit):
            return 0
        
        # not include item i
        max_profit = self.dfs(i + 1, profit, weight, capacity)

        # include item i
        new_capacity = capacity - weight[i]

        if new_capacity >= 0:
            p = profit[i] + self.dfs(i + 1, profit, weight, new_capacity)
            # new max
            max_profit = max(max_profit, p)
        
        return max_profit
