class Solution:
    def isValid(self, s: str) -> bool:
        symbol = {")":"(","]":"[","}":"{"}
        temp = []
        for i in s:
            print(i)
            if temp and (i in symbol and temp[-1] == symbol[i]):
                # 현재 i가 오른쪽괄호이고 temp의 마지막값과 dict(Symbol)에 
                # i의키를 가지는 값과 일치할때 temp의 마지막값 삭제 
                temp.pop()
            else:
                # i가 왼쪽괄호면 temp에 i값 저장
                temp.append(i)
        return not temp #temp가 False면 True 즉, temp안에 데이터가없으면 Ture 반대면  False
print(Solution().isValid("[()]{}"))