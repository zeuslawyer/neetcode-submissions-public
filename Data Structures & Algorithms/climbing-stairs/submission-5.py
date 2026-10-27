class Solution:
    def climbStairs(self, n: int) -> int:
        startToDestMap = {}

        def numStepsFrom(currentStep, target):
            if currentStep > target: return 0
            if currentStep == target: return 1
            if currentStep in startToDestMap:
                return startToDestMap[currentStep]
            
            startToDestMap[currentStep] = numStepsFrom(currentStep + 1, target) + numStepsFrom(currentStep + 2, target)
            return startToDestMap[currentStep]
        
        return numStepsFrom(0, n)