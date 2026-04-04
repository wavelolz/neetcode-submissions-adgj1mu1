class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0]*len(temperatures)

        for i in range(len(temperatures)):

            while len(stack)>0 and temperatures[i]>stack[-1][0]:
                days = i - stack[-1][1]
                result[stack[-1][1]] = days
                stack.pop()

            stack.append([temperatures[i], i])
        return result



        