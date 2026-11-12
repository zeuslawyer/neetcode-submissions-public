
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        DP Intuition: for any given coin to make up the amount it is effectively:
        num[targetamount - coin] + num[coin]

        eg for to achieve $7 with $5 would be, the min ways to achieve $5 
        + min ways to get to ($7-$5) => $2.

        So we need to compute min ways to get to all sums from $0 to $amount
        """
        
        # since we are always checking for minium num we initialise with a high max value
        # which can be +inf or target amount + 1
        # indexes are the various target rangers from $0 to $amount, hence len is amount + 1
        minNumTo = [math.inf] * (amount+1)
        minNumTo[0] = 0

        # iterate over this array starting from Idx 1 and make the calculations
        # nested loop is to compute for EVERY coin denom
        for target in range(1, len(minNumTo)):
            for coin in coins:
                # we can only use coins less than target
                if coin > target: continue

                # we can reach current target using the current coin.  So that "1".
                # and we know the min coins need to reach the COMPLEMENT --> current target - current coin
                # so 1+ minNumTo[COMPLEMENT] is a valid way to get to this current target.
                # but we want min ways so we take min of CURRENT num to get to this target 
                # and the newly calculated way
                complement = target - coin
                minNumTo[target] = min(minNumTo[target], 1 + minNumTo[complement])

        # return -1 if there is no min mumber
        if minNumTo[amount]== math.inf: 
            return -1

        return int(minNumTo[amount])