# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        '''
        use rightmost element as the pivot every time,
        greater than or equal to the right of the pivot
        '''
        self.quickSortHelper(pairs, 0, len(pairs) - 1)

        return pairs
    
    def quickSortHelper(self, pairs, start, end):
        # if only one element, consider sorted
        if end - start + 1 <= 1:
            return
        
        pivot = pairs[end] # rightmost as pivot
        left = start # elements smaller than the pivot

        for i in range(start, end):
            # partition
            if pairs[i].key < pivot.key:
                # swap
                pairs[left], pairs[i] = pairs[i], pairs[left]
                left += 1 # good and shift
        
        # swap with the pivot
        pairs[left], pairs[end] = pairs[end], pairs[left]
        # pairs[end] = pairs[left]
        # pairs[left] = pivot

        self.quickSortHelper(pairs, start, left - 1) # left
        self.quickSortHelper(pairs, left + 1, end) # right


        
