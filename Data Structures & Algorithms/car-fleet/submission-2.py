class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # make tuples of pos/speed for the N cars. Initially this means N fleets of 1 car each

        zipped = [(p,s) for p, s in zip(position, speed)]

        fleets = len(position)
        prevFleetsTime = 0

        # sort in descending so that the car with highest pos (closest to dest) is first
        for pos, speed in sorted(zipped, reverse=True):
            timeToDest = (target - pos) / speed
            if timeToDest <= prevFleetsTime:
                # this car/fleet will catch up before dest which means fleets merge
                fleets -= 1
            else:
                prevFleetsTime = timeToDest
            
        return fleets
            




        