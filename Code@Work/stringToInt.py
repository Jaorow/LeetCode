class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        final = ""

        if len(s)<1:
            return 0

        if s[0] == "-" or s[0] == "+":
            final = s[0]
            s = s[1:]

        for i in s:
            try:
                int(i)
                final += i
            except:
                break

        try:
            final = int(final)
        except ValueError:
            return 0

        if final <= -2147483649: return -2147483648
        if final >= 2147483648: return 2147483647
        return final

#tests for myAtoi function

tests = {'    -42': -42, "412 with words": 421, "-412 with words": -412, "0": 0, "": 0,"words and 987": 0,"+1":1,"   -42":-42}
print(f"\n GOT \t<---->\t WANT\n")
for test in tests:
    if test == "+1":
        print("w")
    print(f" {Solution.myAtoi(Solution,test)} \t<---->\t {tests[test]}")