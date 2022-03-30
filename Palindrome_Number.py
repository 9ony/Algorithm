class Solution:
    def isPalindrome(self, x: int) -> bool:
        valueanswer = str(x)
        x = len(valueanswer)
        halfnum = int(x/2)
        odd = [0,1][x == halfnum*2] #[거짓,참][조건]홀짝구분

        lstring = valueanswer[:halfnum:1]
        rstring = valueanswer[:halfnum-odd:-1]

        if lstring == rstring :
            return True
        else :
            return False