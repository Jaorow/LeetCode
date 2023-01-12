class Solution:
    def longestValidParentheses(self, s: str) -> int:
        biggest = 0
        stack = [-1]
        
        for i in range(len(s)) :
            if s[i] == "(" : 
                stack.append(i)
            else :
                stack.pop()
                if len(stack) == 0 : 
                    stack.append(i)
                else:
                    biggest = max(biggest, i - stack[-1])
        
        return biggest



tests = {
     
        ')' : 6
        }
print(f"\nGOT \t<---->\t WANT\n")
for test in tests:
    print(f" {Solution.longestValidParentheses(Solution,test)} \t<---->\t {tests[test]}")

