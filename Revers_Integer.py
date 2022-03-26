class Solution:
    def reverse(self, x: int) -> int:
        left_max = -1*2**31
        right_max = 2**31-1
        sign = [1,-1][x<0]
        if left_max<x<right_max :
            answer = [str(x)[::-1],str(x)[:0:-1]][sign==-1]
            while answer[0] == 0:
                answer.remove(0)
            return int(answer)*sign
        else :
            return 0
        
x = -1230090000
print(Solution().reverse(x))