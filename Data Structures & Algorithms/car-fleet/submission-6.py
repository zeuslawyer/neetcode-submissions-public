class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # make tuples of pos/speed for the N cars. Initially this means N fleets of 1 car each

        zipped = [(p,s) for p, s in zip(position, speed)]

        fleets = len(position)
        prevTimeToDest = 0

        # sort in descending so that the car with highest pos (closest to dest) is first
        for pos, spd in sorted(zipped, reverse=True):
            timeToDest = (target - pos) / spd
            if timeToDest <= prevTimeToDest:
                # this car/fleet is faster => will catch up before dest which means fleets merge
                # and  the prevFleetTime to remains as bottleneck
                fleets -= 1
            else:
                # this longer time is the bottleneck for cars that come after
                # since the zipped list is sorted descending, all remaining tuples are further away 
                # which means this fleets time will become THEIR bottleneck
                prevTimeToDest = timeToDest
            
        return fleets
            
