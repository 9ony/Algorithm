from typing import List
#배열에서 3개의숫자를 더해서 0이되는 3개의 정수를 포함하는 배열을 생성
#[x1+x2+x3] = 0
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        print(nums)
        answer = []
        l = len(nums)
        i = 0
        while i < l:
            if nums[i] > 0: #nums[i]가 음수가 아닐경우에 반복을멈춘다
                break  
            m = i + 1 #middle index
            r = l - 1 #right index
            while m < r:
                sum3 = nums[i] + nums[m] + nums[r]
                if sum3 == 0:
                    answer.append([nums[i], nums[m], nums[r]])
                    while m+1 < l and nums[m+1] == nums[m]: 
                        m += 1  
                    m += 1
                    r -= 1
                elif sum3 < 0: 
                    m += 1
                else: 
                    r -= 1
                #sum3이 0보다작을때 midindex +1 클때 rightindex를 -1줄여서 0을 찾는다 
            while i+1 < l and nums[i+1] == nums[i]: i += 1 
            i += 1
        return answer
print(Solution().threeSum([10,-10,0,1,5,2,-5-2,7]))