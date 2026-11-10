class Solution:
    def arrangeCoins(self, n: int) -> int:
        i = 1
        
        while n >= i:
            n-= i
            i += 1
        
        # i-1 because i was increemented but then the while condition broke.  so we need to decrement again
        return i-1
