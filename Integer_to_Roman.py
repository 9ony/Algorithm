class Solution:
     def intToRoman(self, num: int) -> str:
        if 3999<num or 1>num :
            return "num over"
        Symbol = ("I","IV","V","IX","X","XL","L","XC","C","CD","D","CM","M")
        digit = (1,4,5,9,10,40,50,90,100,400,500,900,1000)
        res = ""
        index = len(Symbol)-1
        while num > 0:
            res = res + (Symbol[index] * (num // digit[index]))
            num = num % digit[index]
            index -= 1
        return res
print(Solution().intToRoman(1994))