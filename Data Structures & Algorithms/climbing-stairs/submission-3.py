class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}

        def numStepsFrom(currentStep, target):
            if currentStep > target: return 0
            if currentStep == target: return 1
            if currentStep in memo:
                return memo[currentStep]
            
            memo[currentStep] = numStepsFrom(currentStep + 1, target) + numStepsFrom(currentStep + 2, target)
            return memo[currentStep]
        
        return numStepsFrom(0, n)