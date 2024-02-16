from collections import deque
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        nums = deque(nums)
        answer = []

        def dfs(num,path):
            answer.append(path[:])

            for i in range(num,len(nums)):
                path.append(nums[i])
                dfs(i+1,path)
                path.pop()


        dfs(0,[])

        return answer

sol = Solution()
nums = [1,2,3]
print(sol.subsets(nums))

