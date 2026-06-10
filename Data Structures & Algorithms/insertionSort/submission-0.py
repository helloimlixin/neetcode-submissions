# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        '''
        pairs: (5, "apple"), (2, "banana"), (9, "cherry")

        main idea: break into subproblems

        step 1: (5, "apple") => sorted
        step 2: (5, "apple"), (2, "banana") => (2, "banana"), (5, "apple")
        step 3: (2, "banana"), (5, "apple"), (9, "cherry") => sorted

        iteration: swap (insertion) whenever a smaller element is found, to find
        the element to be swapped with, another inner while loop is needed

        Time complexity: O(N^2).
        Space complexity: O(1).
        '''
        states = []

        for i in range(len(pairs)):
            j = i - 1

            while j >= 0 and pairs[j + 1].key < pairs[j].key:
                pairs[j + 1], pairs[j] = pairs[j], pairs[j + 1]
                j -= 1
            
            states.append(pairs[:])
        
        return states