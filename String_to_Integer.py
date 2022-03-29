class Solution:
    def myAtoi(self, s: str) -> int:
        sign = ('-','+')
        digit = ('0','1','2','3','4','5','6','7','8','9')
        index = 0
        start = 0
        if 0 >= len(s) or len(s) >= 200:
            return 0
        else:
            answer = s.lstrip(' ')
            if answer == '' :
                return 0
            else :
                if answer[0] in sign:
                        start +=1
                        index +=1
                        if len(answer) == 1 :
                            return 0
                elif answer[0] in digit:
                        start = 0
                else :
                    return 0
                while index < len(answer):
                    if answer[index] not in digit:
                        answer = answer[:index]
                        if answer[index-1] not in digit:
                            return 0
                        else :
                            break
                    index+=1
        
        return max(-2**31,min(int(answer),2**31-1))
print(Solution().myAtoi(" "))