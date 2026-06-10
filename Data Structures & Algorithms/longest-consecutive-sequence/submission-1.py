class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """input [2, 20, 4, 10, 3, 4, 5]
        sorting would be O(n log n)

        sequences: 2 3 4 5,     4,      10,     20
        use a hashset to save the numbers, then save
        the starts of the sequences first (sequences
        with no left neighbors, n - 1 not in set), and
        increment like hashing with chaining

        Time complexity: O(n).
        Space complexity: O(n).
        """
        nums_set = set(nums)
        longest = 0

        for num in nums:
            # check if the start of a sequence (no left neighbors)
            if (num - 1) not in nums_set:
                length = 0
                while (num + length) in nums_set:
                    length += 1
                longest = max(length, longest)

        return longest
        