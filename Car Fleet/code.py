class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position, speed))
        sortedCars = sorted(cars, key=lambda x:x[0], reverse=True)
        stack = []

        for p, s in sortedCars:
            x = (target-p)/s
            stack.append(x)

            while len(stack) > 1 and stack[-1] <= stack[-2]:
                stack.pop()

        
        return len(stack)

        