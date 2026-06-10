class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
        s       X   Y   Y   X   Y   X       k = 2
                    l
                                    r
        
        win_len = r - l + 1 = 5
        char_map = {X:2, Y:3}
        max_freq = 3
        nrepls = win_len - max_freq = 3 <= k ? False
        longest = max(longest, win_len) = 5

        Time complexity: O(n).
        Space complexity: O(1).
        '''
        l, longest = 0, 0
        char_map, max_freq = {}, 0

        for r in range(len(s)):
            win_len = r - l + 1
            char_map[s[r]] = 1 + char_map.get(s[r], 0)
            max_freq = max(max_freq, char_map[s[r]])

            if win_len - max_freq <= k:
                longest = max(longest, win_len)
            else:
                char_map[s[l]] -= 1
                l += 1
        
        return longest
        