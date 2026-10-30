class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1

        while l <= r:

            mid = (l + r) // 2
            if nums[mid] == target: return mid

            if nums[l] <= nums[mid]:
                # LHS is sorted so check if target is within it. if not target is in RHS.
                if nums[l] <= target < nums[mid]:
                    # target is on LHS
                    r = mid - 1
                else:
                    # target is on RHS
                    l = mid + 1

            else:
                # RHS is sorted so check if target is within it.  If not, its not in RHS
                if nums[mid] < target <= nums[r]:
                    # target is on RHS
                    l = mid + 1
                else:
                    # target is on LHS
                    r = mid - 1
            
        return -1
