class Solution:
    def intToRoman(self, num: int) -> str:
        roman_to_integer = {'I': 1,'V': 5,'X': 10,'L': 50,'C': 100,'D': 500,'M': 1000,}
        unpadded = ([str(a) for a in str(num)[::-1]])
        for i in range(len(unpadded)):
            unpadded[i] = unpadded[i].ljust(i+1,"0")
        print(unpadded)
        return num


#tests for intToRoman function

tests = {3: "III", 58:"LVIII",1994 : "MCMXCIV"}
print(f"\n GOT \t<---->\t WANT\n")
for test in tests:
    print(f" {Solution.intToRoman(Solution,test)} \t<---->\t {tests[test]}")