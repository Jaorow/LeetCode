class Solution:
    def longestCommonPrefix(self, strs):
        length = len(min(strs, key=len))
        stri = ""
        if strs.count(strs[0]) == len(strs):
            return strs[0]
        if len(strs) == 1:
            return strs[0]
        
        for i in range(length+1):
            if length == 1:
                i = 1
            temp = []
            for string in strs:
                temp.append(string[:i])

            if temp.count(temp[0]) == len(temp):
                stri = temp[0]
            else: break
        return stri
        

print(Solution.longestCommonPrefix(Solution,["aaa","aa","aaa"]))
print(Solution.longestCommonPrefix(Solution,["ab", "a"]))
print(Solution.longestCommonPrefix(Solution,["flower","flow","flight"]))
