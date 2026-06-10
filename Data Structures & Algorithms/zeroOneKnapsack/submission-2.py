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

        repeting calculations -> optimization (memoization)


        row: item selected, len(profit)
        column: capacity, len(capacity) + 1, because all possible
            values for capacity are 0, 1, 2, ..., capacity

        stores: max profit attainable

        optimized time complexity: O(mn), space O(mn)

        True Dynamic Programming

        dp table: storing max profit for (item, capacity)

                                capacity
        items       0   1   2   3   4   5   6   7   8
                0   0   0   0   0   0   4   4   4   4
                1   0   0   4    
                2   0
                3   0
        '''
        m, n = len(profit), capacity
        dp = [[0] * (n + 1) for _ in range(m)]

        # initialization: fill the first column and row for edge cases
        # for i in range(m):  # necessary for hashmap
        #     dp[i][0] = 0
        for c in range(n + 1):
            if weight[0] <= c:
                dp[0][c] = profit[0]
        
        for i in range(1, m):
            for c in range(1, n + 1):
                skip = dp[i - 1][c]  # use the previous dp value at capacity c
                include = 0
            
                if c - weight[i] >= 0:
                    include = profit[i] + dp[i - 1][c - weight[i]]
                dp[i][c] = max(include, skip)
        
        return dp[m - 1][n]

