#Letter Combination of a Phone Number
#2~9번까지 숫자가 input되면 그에 해당하는 문자열의 조합을 출력
from typing import List
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits)<=4 and len(digits)>0:
            answer=[]
            letter = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno',
                    '7':'pqrs','8':'tuv','9':'wxyz'}
            for digit in digits:
                try:
                    if not answer:
                        answer = letter[digit]
                    else:
                        temp = []
                        for i in answer:
                            for j in letter[digit]:
                                temp.append(i+j)
                        answer = temp
                except KeyError:
                    return "please input number(2~9)"
        else :
            answer=[]
        return answer
print(Solution().letterCombinations("s"))

        