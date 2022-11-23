

class Solution:
    def longestCommonPrefix(self, strs):
        length = len(min(strs, key=len))
        stri = ""
        for i in range(length):
            temp = []
            for string in strs:
                temp.append(string[:i])
            if temp.count(temp[0]) == len(temp):
                stri = temp[0]
            else: break
        return stri
        



print(Solution.longestCommonPrefix(Solution,["flower","flow","flight"]))
print(len(Solution.longestCommonPrefix(Solution,["dog","racecar","car"])))
