#문자열이 주어지면 반복되지 않는 제일긴 문자열의 수를 출력.

class Solution:
    def lengthOfLongestSubstring(s: str) -> int:
        def check(start , end):
            chars = [0] * 128 #0부터 128까지 아스키코드 문자열에 해당되는 배열생성
            for i in range(start, end + 1):
                c = s[i]
                chars[ord(c)] += 1 # s[i]가 가지는 아스키코드 수만큼 문자열에 1추가
                if chars[ord(c)] > 1:
                    return False
                    #chars[ord(c)]가 1보다크면 2개이상 있는것으로 중복이므로 false 반환
            return True
        n = len(s) #s의 문자열길이를 저장
        res = 0 # init res
        for i in range(n):
            for j in range(i , n):
                if check(i , j):
                    res = max(res , j - i + 1)
        return res
    
    print(lengthOfLongestSubstring("pwppp"))