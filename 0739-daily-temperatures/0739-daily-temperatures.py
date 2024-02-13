from collections import deque
from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        deq = deque(enumerate(temperatures))
        stack_buffer = []
        answer = [0] * len(temperatures)
        while len(deq) > 0:
            curr = deq.popleft()
            while stack_buffer and stack_buffer[-1][1] < curr[1]:
                targetDay = stack_buffer.pop()
                answer[targetDay[0]] = curr[0] - targetDay[0]

            stack_buffer.append(curr)
        return answer

sol = Solution()
temperatures = [73,74,75,71,69,72,76,73]
print(sol.dailyTemperatures(temperatures))