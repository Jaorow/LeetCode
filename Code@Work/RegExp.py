class Solution:
    def isMatch(self, s: str, p: str) -> bool: 
        return True


#tests for isMatch function


print(f"\n GOT \t<---->\t WANT\n")

print(f" {Solution.isMatch(Solution,'aa','a')} \t<---->\t {False}")
print(f" {Solution.isMatch(Solution,'aa','a*')} \t<---->\t {True}")
print(f" {Solution.isMatch(Solution,'aa','.*')} \t<---->\t {True}")