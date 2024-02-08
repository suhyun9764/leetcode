import heapq
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        largest_two = heapq.nlargest(2, nums)
        return self.multiply(largest_two)

    def multiply(self, nums: List[int]):
        answer = 1
        for num in nums:
            answer *= num-1

        return answer

