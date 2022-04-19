# 4개이상의 숫자와 타겟을 입력받고 입력받은 숫자 4개를 더하여 타겟과 동잏한 배열을 생성한다.
# ex) input = [1,0,-1,0,-2,2] target = 0
#     ouput = [-2,-1,1,2] , [-2,0,0,2] , [-1,0,0,1]
from typing import List
class Solution:    
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        answer = []
        nums.sort()
        l = len(nums)
        for i in range(l):
            for j in range(i + 1, l):
                sum4 = target - nums[i] - nums[j]
                m = j + 1
                r = l - 1

                while m < r:
                    if nums[m] + nums[r] < sum4:
                        m += 1
                    elif nums[m] + nums[r] > sum4:
                        r -= 1
                    else:
                        answer.append((nums[i], nums[j], nums[m], nums[r]))
                        m += 1
                        r -= 1
        return answer
print(Solution().fourSum([1,0,-1,0,2,-2],1))