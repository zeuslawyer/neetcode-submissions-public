class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l < r:

            if nums[l] < nums[r]:
                return nums[l] # Edge case. array is already sorted. 

            mid = (l + r) // 2

            if nums[l] <= nums[mid]:
                # LHS is sorted, so rotation point is on the RHS
                l = mid + 1
            else:
                # rotation point is on the LHS
                r = mid

        return nums[l]