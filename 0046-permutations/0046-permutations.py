from collections import deque
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        numsForExec = deque(nums)
        answer = []

        def dfs(path):
            if len(numsForExec) == 0:
                answer.append(path.copy())
                return

            for _ in range(len(numsForExec)):

                current_num = numsForExec.popleft()
                path.append(current_num)
                dfs(path)
                path.pop()
                numsForExec.append(current_num)

        dfs([])
        return answer

s = Solution()
nums = [1,2,3]
print(s.permute(nums))