from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0]*len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            while stack and temperatures[i]>temperatures[stack[-1]]:
                pre_idx = stack.pop()
                answer[pre_idx] = i - pre_idx

            stack.append(i)

        return answer