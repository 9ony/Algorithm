from typing import List
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if not nums:
            return None
        
        diff=float('inf') #양수 무한대
        nums.sort()
        
        for i in range(len(nums)-2):
            m=i+1
            l=len(nums)-1
            
            while m<l:
                sum3=nums[i]+nums[m]+nums[l]
                #abs()절대값변환
                if abs(sum3-target) < diff:
                    diff=abs(sum3-target)
                    output=sum3
                
                if sum3<target:
                    m+=1
                elif sum3>target:
                    l-=1
                else:
                    return target
        return output
print(Solution().threeSumClosest([1,-1,3,-4],1))