class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position,speed))
        res = reversed(cars)
        fleets = 0
        last_time = 0
        for pos,speed in res:
            time = (target - pos)/speed

            if time > last_time:
                fleets += 1
                last_time = time
        
        return fleets





