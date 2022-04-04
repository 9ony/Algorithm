class Solution:
     def romanToInt(self, s: str) -> int:
        res = 0
        ind = 0
        Symbol = ("I","IV","V","IX","X","XL","L","XC","C","CD","D","CM","M")
        digit = (1,4,5,9,10,40,50,90,100,400,500,900,1000)
        def indexfind(s: str) -> int :
            i=Symbol.index(s)
            num = int(digit[i])
            return num
        while  ind < len(s) :
            try:
                if s[ind] == "I" and (s[ind+1] == "V" or s[ind+1] == "X") :
                    res += indexfind(s[ind]+s[ind+1])
                    ind += 2
                elif s[ind] == "X" and (s[ind+1] == "L" or s[ind+1] == "C") :
                    res += indexfind(s[ind]+s[ind+1])
                    ind += 2
                elif s[ind] == "C" and (s[ind+1] == "D" or s[ind+1] == "M") :
                    res += indexfind(s[ind]+s[ind+1])
                    ind += 2
                else :
                    res += indexfind(s[ind])
                    ind += 1
            except IndexError:
                res += indexfind(s[ind])
                ind +=1
        return res
print(Solution().romanToInt("MCMXCIV")) #1994