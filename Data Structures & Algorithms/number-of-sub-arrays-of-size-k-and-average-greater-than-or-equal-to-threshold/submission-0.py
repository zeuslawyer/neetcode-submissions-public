class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        # if not arr or not k or not threshold: return 0

        left = 0
        count = 0

        windowSum = 0
        windowAvg = 0

        for right in range(0, len(arr)):
            windowSize = right - left + 1
            
            # condition 1 - expand till window = 3
            if windowSize  < k:
                windowSum += arr[right]
                continue

            if windowSize == k:
                windowSum += arr[right]
                windowAvg = windowSum/k
                
                
            if windowSize > k:
                windowSum = windowSum - arr[left] + arr[right]
                windowAvg = windowSum/k
                left += 1

            if windowAvg >= threshold:
                    count += 1


        return count
        

    