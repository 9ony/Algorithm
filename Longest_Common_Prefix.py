class Solution:
    def longestCommonPrefix(self, strs : list) -> str:
        strs.sort(key=lambda x : len(x))
        if len(strs) == 0 :
            return ''
        else :
            for i in range(len(strs[0])):
                for j in range(1,len(strs)):
                    if strs[0][i] != strs[j][i]:
                        return strs[0][:i]
            return strs[0]

l = ["star","stay","tailer"]
print(Solution().longestCommonPrefix(l))