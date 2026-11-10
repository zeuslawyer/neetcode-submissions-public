class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        sortedArr = self.mergeSortedArrays(nums1, nums2)

        median = 0
        if len(sortedArr) % 2== 0:
            leftmid = (len(sortedArr)-1)//2
            rightmid = leftmid + 1

            median = (sortedArr[leftmid]+ sortedArr[rightmid]) / 2
        else:
            mid = (len(sortedArr)-1)//2
            median = sortedArr[mid]
        
        return median


    def mergeSortedArrays(self, arr1, arr2):
        i,j = 0, 0

        res = [0] * (len(arr1) + len(arr2))
        residx = 0

        # merge arrays while within bounds
        while i < len(arr1) and j < len(arr2):
            if arr1[i] <= arr2[j]:
                res[residx] = arr1[i]
                i+=1
            else:
                res[residx] = arr2[j]
                j+=1
            residx+=1

        # arr1 remains
        while i < len(arr1):
            res[residx] = arr1[i]
            i+= 1
            residx += 1
        
        # arr2 remains
        while j < len(arr2):
            res[residx] = arr2[j]
            j+= 1
            residx += 1
        
        return res
