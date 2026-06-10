# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        '''
        MergeSort Procedure.

        Time complexity: O(nlogn).
        Space Complexity: O(n)
        '''
        self.mergeSortHelper(pairs, 0, len(pairs) - 1)

        return pairs

    def mergeSortHelper(self, pairs: List[Pair], start: int, end: int) -> List[Pair]:
        # Base case.
        if end - start <= 0:
            return
        
        # Compute the middle location.
        mid = start + (end - start) // 2

        # Sort the left half.
        self.mergeSortHelper(pairs, start, mid)

        # Sort the rigth half.
        self.mergeSortHelper(pairs, mid + 1, end)

        # Merge the two sorted halfs.
        self.merge(pairs, start, mid, end)
    
    def merge(self, arr: List[Pair], start: int, mid: int, end: int) -> None:
        '''
        Merge with the two-pointer technique.
        '''

        # Copy the left and right sorted half arrays into two temporary arrays.
        left = arr[start: mid + 1]
        right = arr[mid + 1: end + 1]

        lptr, rptr = 0, 0 # index pointers for left and right arrays, respectively
        i = start # index pointer for the arr

        # Merge
        while lptr < len(left) and rptr < len(right):
            if left[lptr].key <= right[rptr].key:
                arr[i] = left[lptr]
                lptr += 1
            else:
                arr[i] = right[rptr]
                rptr += 1
            
            i += 1
        
        while lptr < len(left):
            arr[i] = left[lptr]
            lptr += 1
            i += 1
        
        while rptr < len(right):
            arr[i] = right[rptr]
            rptr += 1
            i += 1
    
