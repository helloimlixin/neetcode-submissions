import heapq
from typing import List


def get_reverse_sorted(nums: List[int]) -> List[int]:
    max_heap = []
    reverse_sorted = []

    for num in nums:
        heapq.heappush(max_heap, -num)
    
    while max_heap:
        reverse_sorted.append(-heapq.heappop(max_heap))
    
    return reverse_sorted

# do not modify below this line
print(get_reverse_sorted([1, 2, 3]))
print(get_reverse_sorted([5, 6, 4, 2, 7, 3, 1]))
print(get_reverse_sorted([5, 6, -4, 2, 4, 7, -3, -1]))
