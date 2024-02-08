from collections import defaultdict


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        dict = defaultdict(int)
        
        for stone in stones:
            dict[stone] += 1
        
        cnt = 0
        for jewel in jewels:
            cnt += dict[jewel]
            
        return cnt