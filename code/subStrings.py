class Solution(object):
    """ does not work as it takes much to long ): """
    def lengthOfLongestSubstring(self, s):
        largest = 0
        for i in range(len(s)+1):
            for j in range(len(s)+1):
                sub = s[i:j]
                try:
                    if s[j] in sub:
                        if len(sub) > largest:
                            largest = len(sub)
                        break
                except IndexError:
                    if len(sub) > largest:
                            largest = len(sub)
        
        return largest
        

print(Solution.lengthOfLongestSubstring(Solution,""))
print(Solution.lengthOfLongestSubstring(Solution,"abcabcbb"))
print(Solution.lengthOfLongestSubstring(Solution,"bbbbb"))
