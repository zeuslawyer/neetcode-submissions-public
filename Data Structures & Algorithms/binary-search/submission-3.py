class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.recursive(0, len(nums)-1, nums, target)
    

    def recursive(self, left, right, nums, t):
        if left > right:
            return -1
        
        mid = (left+right) // 2
        if nums[mid] == t:
            return mid
        
        
        if nums[mid] > t:
            return self.recursive(left, mid-1, nums, t)
        
        else:
            return self.recursive(mid+1, right, nums, t)


        
        