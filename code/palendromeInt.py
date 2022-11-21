from ast import List


class Solution:
    def isPalindrome(self, x: int) -> bool:
        ordered = [i for i in str(x)]
        rev = [i for i in ordered]
        rev.reverse()
        if ordered == rev: return True
        else: return False

    def kthPalindrome(self, queries: List[int], intLength: int) -> List[int]:
        for i in queries:
            print(i)



print(Solution.kthPalindrome(Solution,[101,111,121,131,141,999]))
# print(Solution.isPalindrome(Solution,121))
# print(Solution.isPalindrome(Solution,-121))
# print(Solution.isPalindrome(Solution,10))
# print(Solution.isPalindrome(Solution,1))