class Solution:
    def maxArea(self, height : list) -> int:
        length = len(height)
        left = 0
        right = length-1
        high =0
        while left<right :
            leftHeight = height[left]
            rightHeight = height[right]
            area = min(leftHeight,rightHeight) * (right - left)

            high = [high,area][area>high]

            if leftHeight>rightHeight :
                right -= 1
            else :
                left += 1
        return high
print(Solution().maxArea([1,8,6,2,5,4,8,3,7]))