class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        n = len(temperatures)-1
        result = []
        for day in range(n, -1, -1):
            while stack and temperatures[day] >= temperatures[stack[-1]]:
                stack.pop()
            if not stack:
                result.append(0)
            else:
                result.append(stack[-1] - day )
            stack.append(day)

        result.reverse()
        return result
            


#### OPTIMIZED 
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        n = len(temperatures)
        result = [0] * n
        for day in range(n):
            while stack and temperatures[day] > temperatures[stack[-1]]:
                poppedDay = stack.pop()
                result[poppedDay] = day - poppedDay
            stack.append(day)

        return result
            
