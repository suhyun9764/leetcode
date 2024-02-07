from collections import defaultdict
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        dict = defaultdict(int)
        for num in nums :
            dict[num] += 1

        answer = sorted(dict.keys(),key = lambda x : dict[x] ,reverse=True)[:k]
        return answer