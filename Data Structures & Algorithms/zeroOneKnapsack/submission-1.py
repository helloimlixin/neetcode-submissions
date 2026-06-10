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
        column: capacity, range(capacity)

        stores: max profit attainable

        optimized time complexity: O(mn)
        '''
        m, n = len(profit), capacity
        memo = [[-1] * (n + 1) for _ in range(m)]

        return  self.memo_solver(0, profit, weight, capacity, memo)
    
    def memo_solver(self, i, profit, weight, capacity, memo):
        if i == len(profit):
            return 0
        
        if memo[i][capacity] != -1:  # havent computed since everything is non-negative
            return memo[i][capacity]
        
        # not include item i
        memo[i][capacity] = self.memo_solver(i + 1, profit, weight, capacity, memo)

        # include item i
        new_capacity = capacity - weight[i]

        if new_capacity >= 0:
            p = profit[i] + self.memo_solver(i + 1, profit, weight, new_capacity, memo)
            # new max
            memo[i][capacity] = max(memo[i][capacity], p)
        
        return memo[i][capacity]
