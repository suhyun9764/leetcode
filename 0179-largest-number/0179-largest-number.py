from functools import cmp_to_key
from typing import List

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def compare(x: int, y: int) -> int:
            # 두 숫자를 문자열로 변환하여 비교하여 더 큰 순서로 정렬
            if str(x) + str(y) < str(y) + str(x):
                return 1
            elif str(x) + str(y) > str(y) + str(x):
                return -1
            else:
                return 0
        
        nums.sort(key=lambda x: str(x), reverse=True) # 숫자를 문자열로 변환하여 정렬
        nums = sorted(nums, key=cmp_to_key(compare)) # 더 큰 숫자를 만들 수 있도록 정렬
        
        # 리스트를 문자열로 변환
        result = ''.join(map(str, nums))
        # 0이 여러 번 등장하는 경우 '0'으로 변환
        return str(int(result))
