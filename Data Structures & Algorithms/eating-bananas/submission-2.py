class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        Intution: the slowest rate is 1 banana per hour. because no matter what
        we have to spend 1 hour per pile MINIMUM. thats our time constraint.
        if we have 100 bananas - doesnt matter we still have to spend the full hour on that pile.
        so that means that minimum k (rate) is 1 per hour and max is the max(arr) per hour.

        thats the range of the binary search space.  Left and right pointers get set accordingly.

        Since binary search returns the result when l == r, we can return either. 
        """
        l, r = 1, max(piles)

        while l <= r:
            # calculate rate k as mid index.  and then see if its faster or 
            # slower than it needs to be. If time to eat all bananas <= h then 
            # its faster so we make right pointer = k - 1
            k = (l + r) // 2

            totalTime = 0
            for p in piles:
                totalTime += math.ceil(float(p) / k)
            if totalTime <= h:

                r = k - 1
            else:
                l = k + 1
        return l