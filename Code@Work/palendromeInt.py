class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]





#tests for isPalindrome function

tests = {'121': True, "-121":False,"10":False}
print(f"\n GOT \t<---->\t WANT\n")
for test in tests:
    print(f" {Solution.isPalindrome(Solution,test)} \t<---->\t {tests[test]}")