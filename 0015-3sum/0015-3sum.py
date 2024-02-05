from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        # 오름차순으로 정렬
        nums.sort()

        # 결과값 리스트
        result = []

        # 순서대로 기준점(i)를 잡고 start_idx와 end_idx의 중복을 피하기 위해 -2를 해준다.
        for i in range(len(nums) - 2):
            # 만약 지금의 기준점이 전 단계와 같다면 skip
            if i>0 and nums[i] == nums[i-1]:
                continue

            #  i+1의 위치를 start_idx, 오른쪽 맨 끝의 위치를 end_idx로 정한다
            start_idx = i+1
            end_idx = len(nums)-1

            while start_idx<end_idx :
                if(nums[i]+nums[start_idx]+nums[end_idx]>0) :
                    end_idx-=1 # 세 수의 합이 양수라면 0이 되기 위해 값을 줄여야 하므로 end_idx를 왼쪽으로 한칸 이동 시킨다
                elif(nums[i]+nums[start_idx]+nums[end_idx]<0) :
                    start_idx+=1 # 세 수의 합이 음수라면 0이 되기 위해 값을 늘려야 하므로 start_idx를 오른쪽으로 한칸 이동 시킨다.
                else :
                    correct_list = [nums[i],nums[start_idx],nums[end_idx]]
                    result.append(correct_list) # 세 수의 합이 0이면 해당 값들을 리스트에 저장

                    while start_idx<end_idx and nums[start_idx]==nums[start_idx+1]:
                        start_idx+=1 # 증복 방지
                    while start_idx<end_idx and nums[end_idx]==nums[end_idx-1]:
                        end_idx-=1 # 중복 방지
                    start_idx+=1
                    end_idx-=1

        return result


