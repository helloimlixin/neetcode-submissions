class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lptr, rptr = 0, len(nums) - 1

        while lptr <= rptr:
            mid = (lptr + rptr) // 2

            if nums[mid] > target:
                rptr = mid - 1
            elif nums[mid] < target:
                lptr = mid + 1
            else:
                return mid
        
        return -1

        