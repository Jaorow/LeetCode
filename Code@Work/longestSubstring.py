class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max = 0
        string = ""
        for i in range(len(s)):
            for j in range(len(s)):
                if s[j+1] in s[:j]:
                    if len(s[:j]) > max:
                        max = len(s[:j])
                        string = s[:j]
                    break
        return f"{max}-->{string}"


print(Solution.lengthOfLongestSubstring(Solution,"abcabcbb"))
print(Solution.lengthOfLongestSubstring(Solution,"bbbbb"))
print(Solution.lengthOfLongestSubstring(Solution,""))
print(Solution.lengthOfLongestSubstring(Solution,"pwwkew"))