class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        lptr, hptr = 0, m * n - 1

        while lptr <= hptr:
            mid = (lptr + hptr) // 2

            if matrix[mid // n][mid % n] < target:
                lptr = mid + 1
            elif matrix[mid // n][mid % n] > target:
                hptr = mid - 1
            else:
                return True
        
        return False

        