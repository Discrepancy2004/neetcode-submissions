class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        for i,num in enumerate(temperatures):
            if not stack or temperatures[stack[-1]] >= num:
                stack.append(i)

            else:
                while len(stack) > 0 and temperatures[stack[-1]] < num :
                    a = stack.pop()
                    res[a] = i - a

                stack.append(i)

        return res

