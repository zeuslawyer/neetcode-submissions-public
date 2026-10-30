class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0, len(nums)-1

        while l < r :
            # edge case. its already sorted.
            if nums[l] < nums[r]:
                return nums[l]

            mid = (l+r) // 2

            if nums[l] <= nums[mid]:
                # lhs is sorted order so pivot is on RHS
                l = mid + 1
            else:
                # pivot is on lhs
                r = mid

        return nums[l]

