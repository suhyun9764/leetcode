from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        answer = []
        for i in range(len(nums) - 2):
            if i>0 and nums[i-1] == nums[i]:
                continue
            left = i+1
            right = len(nums) - 1
            while left<right:
                s = nums[i] + nums[left] + nums[right]
                if s == 0 :
                    sum_zero = [nums[i], nums[left], nums[right]]
                    answer.append(sum_zero)
                    while left<right and nums[left] == nums[left+1]:
                        left+=1
                    while left<right and nums[right-1] == nums[right] :
                        right-=1

                    left+=1
                    right-=1


                elif s > 0 :
                    right-=1
                else :
                    left +=1

        return answer
