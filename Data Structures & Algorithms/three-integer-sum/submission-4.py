class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        if len(nums) == 0: return res

        visited = set()
        nums.sort()

        for i, num in enumerate(nums):
            # since it sorted, dupes will be contiguous
            if i > 0 and nums[i-1] == num:
                continue
            
            l, r = i+1, len(nums)-1
            while l < r:
                sum = num + nums[l] + nums[r]
                if sum == 0:
                    res.append([num, nums[l], nums[r]])
                    l+=1
                    r-=1
                    while nums[l] == nums[l-1] and l < r:
                        l+=1
                elif sum < 0:
                    l+=1
                else:
                    r -= 1
        
        return res 

