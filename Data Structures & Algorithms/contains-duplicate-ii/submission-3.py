class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if not nums or not k: return False
        
        left = 0
        seen = set()

        for right in range(0, len(nums)):
            if nums[right] in seen: return True

            # window len exceeds k
            if right - left + 1 > k:
                seen.remove(nums[left])
                left += 1 # drag the window along behind right

            # insert into seen set 
            seen.add(nums[right])
        
        return False


