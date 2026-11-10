class Solution:
    def arrangeCoins(self, n: int) -> int:
        i = 1
        
        # we need n couns to complete another row
        # since ith row needs i coins to complete  n needs to be greater than = i
        while n >= i:
            n-= i
            i += 1
        
        # i-1 because i was increemented but then the while condition broke.  so we need to decrement again
        return i-1
