class Solution:
    s = "ABCDEFGHIJKLMNOPQRSTU"
    num =15
    def convert(s: str, numRows: int) -> str:
        L = [""]*numRows
        i=0
        index = 0
        tn = numRows-1
        space = tn-1
        if numRows == 1:
            return s
        else:
            while i<len(s):
                L[index]+=s[i]
                L[index]+=" "*space
                if index==0:
                    tp = 1
                elif index==tn:
                    tp = -1
                if space == 0:
                    space = tn
                space += -1
                index += tp
                i+=1
        answer = L
        return answer
    for i in convert(s,num) :
        print(i)