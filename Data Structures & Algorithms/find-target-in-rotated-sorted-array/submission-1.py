class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1
        
        l, r = 0, len(nums)-1

        while l <= r:
            mid = (l+r) // 2

            if nums[mid] == target:
                return mid

            # Search in left side
            if nums[l] <= nums[mid]:  # LHS is sorted/ does not contain pivot
                if target < nums[l] or nums[mid] < target: # target is outside the range of LHS
                    l = mid + 1
                else: # target is in range of LHS
                    r = mid - 1 

            else:     
            # search in RHS
                if target < nums[mid] or target > nums[r]: # target outside range of RHS  
                    r = mid -1
                else: # target is within range of RHS
                    l = mid + 1
        
        return -1
