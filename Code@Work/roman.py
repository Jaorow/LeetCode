class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_integer = {'I': 1,'V': 5,'X': 10,'L': 50,'C': 100,'D': 500,'M': 1000,}
        s = s.replace("IV", "IIII").replace("IX", "VIIII").replace("XL", "XXXX").replace("XC", "LXXXX").replace("CD", "CCCC").replace("CM", "DCCCC")
        
        sum = 0
        for i in s: 
            sum += roman_to_integer[i]

        return sum


print(Solution.romanToInt(Solution,"III"))
print(Solution.romanToInt(Solution,"LVIII"))
print(Solution.romanToInt(Solution,"MCMXCIV"))
print(Solution.romanToInt(Solution,"VIII"))


