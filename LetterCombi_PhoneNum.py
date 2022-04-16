#Letter Combination of a Phone Number
#2~9번까지 숫자가 input되면 그에 해당하는 문자열의 조합을 출력
from typing import List
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits)<=4 and len(digits)>0:
            answer=[]
            letter = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno',
                    '7':'pqrs','8':'tuv','9':'wxyz'}
            all_com = [''] if digits else []
            for digit in digits:
                for i in letter[digit]:
                    for com in all_com:
                        answer.append(com+i)
        else :
            answer=[]
        return answer
print(Solution().letterCombinations("67"))

        